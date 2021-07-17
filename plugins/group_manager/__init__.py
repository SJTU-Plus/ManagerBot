import httpx
from nonebot import RequestSession, on_request, on_command

from config import *

headers = {'Api-Key': api_key}
client = httpx.AsyncClient()


async def verify(comment: str, user_id: int) -> bool:
    code = comment.split('\n')[-1].split('：')[-1]
    data = {
        "qq_number": str(user_id),
        "token": code
    }
    resp = await client.post('https://plus.sjtu.edu.cn/attest/verify', headers=headers, json=data)
    result = resp.json()
    return result['success']


@on_request('group')
async def _(session: RequestSession):
    if session.event.sub_type == 'add':
        res = await verify(session.event.comment, session.event.user_id)
        if res:
            await session.approve()


@on_command('state', aliases=('状态',), privileged=SUPERUSERS)
async def _(session: RequestSession):
    await session.send('正常工作')
