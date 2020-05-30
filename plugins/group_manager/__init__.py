from hashlib import sha256

from nonebot import RequestSession, on_request


def verify(comment: str, group_id: int, user_id: int) -> bool:
    comment = comment.split('\n')[-1]
    comment = comment.split('：')[-1]
    ans = sha256(f'{group_id}{user_id}'.encode(encoding='utf-8')).hexdigest()[0:7]
    return ans == comment


@on_request('group')
async def _(session: RequestSession):
    if session.event.sub_type == 'add':
        if verify(session.event.comment, session.event.group_id, session.event.user_id):
            await session.approve()
        else:
            await session.reject('验证码错误')
    else:
        await session.approve()


@on_request('friend')
async def _(session: RequestSession):
    await session.reject()
