import os

class Config(object):
    # Matrix server URL
    BOT_SERVER_URL = os.environ.get("BOT_SERVER_URL", "")
    # Create an account on matrix.org
    BOT_USER_NAME = os.environ.get("BOT_USER_NAME", "")
    BOT_PASS_WORD = os.environ.get("BOT_PASS_WORD", "")
