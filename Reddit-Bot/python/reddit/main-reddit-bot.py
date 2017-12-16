#!/usr/bin/env python

"""main-reddit-bot.py: main activities of the reddit bot are here"""

import reddit.read_post
import reddit.reply_post

__author__      = "Asdf"
__copyright__   = "Copyright 2017, Planet Earth"

SUBREDDIT = "learnpython"
SUBREDDIT_REPLY = "pythonforengineers"
NUMBER_OF_SUBMISSIONS = 10
BOT_NAME_INI = "bot1"

class Main:

    def main_function(self):
        read_obj = reddit.read_post.Read()
        read_obj.read_post(BOT_NAME_INI, SUBREDDIT, NUMBER_OF_SUBMISSIONS)

        reply_obj = reddit.reply_post.Reply()
        reply_obj.reply(BOT_NAME_INI, SUBREDDIT_REPLY, NUMBER_OF_SUBMISSIONS)


if __name__ == '__main__':
    Main().main_function()


