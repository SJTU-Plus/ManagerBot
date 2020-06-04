import os
from datetime import timedelta, datetime

from nonebot import RequestSession, on_request

from plugins.group_manager.attestation.cmac_attestation import CmacAttestation

secret = os.environ.get('ATTESTATION_SECRET', default=None)
if secret is None:
    print('未设置ATTESTATION_SECRET环境变量')
    exit()
attestation = CmacAttestation(secret=bytes.fromhex(secret))


def verify(comment: str, user_id: int) -> bool:
    code = comment.split('\n')[-1].split('：')[-1]
    timestamp = attestation.verify(str(user_id), code)
    if timestamp is None:
        return False
    now = datetime.now()
    return timestamp < now < timestamp + timedelta(days=30)


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
    await session.reject()
