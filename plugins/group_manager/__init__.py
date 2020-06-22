from datetime import datetime
from typing import Tuple

from nonebot import RequestSession, on_request, on_command, CommandSession, on_notice, NoticeSession

from config import *
from plugins.group_manager.attestation.cmac_attestation import CmacAttestation
from plugins.group_manager.email import EmailSender

smtp_server = os.environ.get('SMTP_SERVER', default=None)
if smtp_server is None:
    print('未设置SMTP_SERVER环境变量')
    exit()
smtp_port = int(os.environ.get('SMTP_PORT', default=0))
if smtp_port == 0:
    print('未设置SMTP_PORT环境变量')
    exit()
username = os.environ.get('SMTP_USER', default=None)
if username is None:
    print('未设置SMTP_USER环境变量')
    exit()
passwd = os.environ.get('SMTP_PASSWD', default=None)
if passwd is None:
    print('未设置SMTP_PASSWD环境变量')
    exit()
secret = os.environ.get('ATTESTATION_SECRET', default=None)
if secret is None:
    print('未设置ATTESTATION_SECRET环境变量')
    exit()

attestation = CmacAttestation(secret=bytes.fromhex(secret))
sender = EmailSender(smtp_server, smtp_port, username, passwd)
email_pattern = re.compile(r'\w+([-+.]\w+)*@sjtu\.edu\.cn')
qq_pattern = re.compile(r'[1-9]\d{4,}')


def verify(comment: str, user_id: int) -> bool:
    code = comment.split('\n')[-1].split('：')[-1]
    timestamp = attestation.verify(str(user_id), code)
    if timestamp is None:
        return False
    now = datetime.now()
    return timestamp < now < timestamp + timedelta(days=30)


async def send_email(email_addr: str, qq: str) -> Tuple[bool, str]:
    if email_addr == '' or qq == '':
        return False, '填写错误，请输入正确的SJTU邮箱。'
    if email_pattern.match(email_addr) is not None and qq_pattern.match(qq) is not None:
        code = attestation.generate(qq)
        res = await sender.send_email(email_addr, qq, code)
        if res:
            return True, '已发送邮件，请及时查收！'
        else:
            return False, '发送邮件失败。请之后重试。'
    else:
        return False, '填写错误，请输入正确的SJTU邮箱。'


@on_request('group')
async def _(session: RequestSession):
    if session.event.sub_type == 'add':
        if verify(session.event.comment, session.event.user_id):
            await session.approve()
        else:
            await session.reject('验证码错误')
    else:
        await session.approve()


@on_request('friend')
async def _(session: RequestSession):
    await session.approve()


@on_notice('friend_add')
async def _(session: NoticeSession):
    msg = '向我发送“验证码”获得加群验证码。'
    await session.send(msg)


# 这里 code 为命令的名字，同时允许使用别名
@on_command('code', aliases=('验证码',), only_to_me=True)
async def code(session: CommandSession):
    mail = session.get('email', prompt='请输入你的SJTU邮箱')
    res, msg = await send_email(mail, str(session.event.user_id))
    await session.send(msg)
    if not res:
        await session.send('请重新发送“验证码”获得加群验证码。')


# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@code.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            session.state['email'] = stripped_arg
        return

    if not stripped_arg:
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('邮箱不能为空，请重试！')

    # 如果当前正在向用户询问更多信息，且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg
