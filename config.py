import re

DEBUG = False

SUPER_USERS = {}
COMMAND_START = ['', re.compile(r'[/!]+')]
HOST = '0.0.0.0'
PORT = 8080
