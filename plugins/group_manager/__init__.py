from datetime import datetime

from nonebot import RequestSession, on_request

from config import *
from plugins.group_manager.attestation.cmac_attestation import CmacAttestation

secret = os.environ.get('ATTESTATION_SECRET', default=None)
if secret is None:
    print('未设置ATTESTATION_SECRET环境变量')
    exit()

attestation = CmacAttestation(secret=bytes.fromhex(secret))
email_pattern = re.compile(r'\w+([-+.]\w+)*@sjtu\.edu\.cn')
qq_pattern = re.compile(r'[1-9]\d{4,}')


def verify(comment: str, user_id: int) -> bool:
    code = comment.split('\n')[-1].split('：')[-1]
    timestamp = attestation.verify(str(user_id), code)
    if timestamp is None:
        return False
    now = datetime.now()
    return timestamp < now < timestamp + timedelta(days=30)


def check_email(email_addr: str) -> bool:
    return True if email_pattern.match(email_addr) else False


def check_qq(qq: str) -> bool:
    return True if qq_pattern.match(qq) else False


@on_request('group')
async def _(session: RequestSession):
    if session.event.sub_type == 'add':
        if verify(session.event.comment, session.event.user_id):
            await session.approve()
        else:
            await session.reject('验证码错误')
    else:
        await session.reject()
