import nonebot

import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugin(
        'plugins.group_manager')
    nonebot.run()
