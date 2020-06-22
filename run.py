import logging

import nonebot
from nonebot import logger

import config

nonebot.init(config)
nonebot.load_plugin(
    'plugins.group_manager')
logging.basicConfig(level=logging.WARNING, filename='bot.log')
logger.setLevel(logging.WARNING)
bot = nonebot.get_bot()
app = bot.asgi

if __name__ == '__main__':
    bot.run()
