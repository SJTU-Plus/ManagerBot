import logging
from os import path

import nonebot
from nonebot import logger

import config

nonebot.init(config)
nonebot.load_plugins(path.join(path.dirname(__file__), 'plugins'), 'plugins')
logging.basicConfig(level=logging.WARNING, filename='data/bot.log')
logger.setLevel(logging.WARNING)
bot = nonebot.get_bot()
app = bot.asgi

if __name__ == '__main__':
    bot.run()
