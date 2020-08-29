from datetime import datetime

from nonebot import RequestSession, on_request

from config import *
from plugins.group_manager.attestation import Blake2Attestation
from plugins.group_manager.attestation import CmacAttestation
from plugins.group_manager.attestation.base import AttestationBase

secret = os.environ.get('ATTESTATION_SECRET', default=None)
if secret is None:
    print('未设置ATTESTATION_SECRET环境变量')
    exit()

cmac_attestation = CmacAttestation(secret=bytes.fromhex(secret))
blake2_attestation = Blake2Attestation(secret=bytes.fromhex(secret))


def verify(comment: str, user_id: int, attest: AttestationBase) -> bool:
    code = comment.split('\n')[-1].split('：')[-1]
    timestamp = attest.verify(str(user_id), code)
    if timestamp is None:
        return False
    now = datetime.now()
    return timestamp < now < timestamp + timedelta(days=30)


@on_request('group')
async def _(session: RequestSession):
    if session.event.sub_type == 'add' and \
            (verify(session.event.comment, session.event.user_id, blake2_attestation) or
             verify(session.event.comment, session.event.user_id, cmac_attestation)):
        await session.approve()
