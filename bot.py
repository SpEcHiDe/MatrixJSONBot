#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

from matrix_bot_api.matrix_bot_api import MatrixBotAPI
from matrix_bot_api.mregex_handler import MRegexHandler
from matrix_bot_api.mcommand_handler import MCommandHandler

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import json

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


def echo_callback(room, event):
    # Somebody said something, let's respond with the event
    room.send_text(json.dumps(event, ensure_ascii=False, indent=2))
    # https://stackoverflow.com/a/4547331/4723940


def main():
    # Create an instance of the MatrixBotAPI
    bot = MatrixBotAPI(
        Config.BOT_USER_NAME,
        Config.BOT_PASS_WORD,
        Config.BOT_SERVER_URL
    )

    # Add a regex handler waiting for the user text
    bot.add_handler(MRegexHandler(".*", echo_callback))

    # Start polling
    bot.start_polling()

    # Infinitely read stdin to stall main thread while the bot runs in other threads
    while True:
        input()


if __name__ == "__main__":
    main()
