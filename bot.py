import nonebot

import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugin(
        'plugins.group_manager')
    # logging.basicConfig(level=logging.WARNING, filename='bot.log')
    # logger.setLevel(logging.WARNING)
    nonebot.run()
