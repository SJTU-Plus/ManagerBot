import nonebot

import config

nonebot.init(config)
nonebot.load_plugin(
    'plugins.group_manager')
bot = nonebot.get_bot()
app = bot.asgi

if __name__ == '__main__':
    nonebot.run()
