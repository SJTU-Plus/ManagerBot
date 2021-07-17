import os
import re

from nonebot.log import logger
from nonebot.default_config import *

DEBUG = False

SUPERUSERS = {0}
COMMAND_START = ['', re.compile(r'[/!]+')]
HOST = '0.0.0.0'
PORT = 8080

super_user = int(os.environ.get('SUPER_USER', default=0))
if super_user:
    SUPERUSERS.add(super_user)
api_key = os.environ.get('API_KEY', default='')
if api_key == '':
    logger.warning('Please provide Api-Key in environment variables')
