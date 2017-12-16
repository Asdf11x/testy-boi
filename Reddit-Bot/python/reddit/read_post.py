#!/usr/bin/env python

"""read_post.py: read basic stuff in reddit an dprint it to the console."""

import praw

__author__      = "Asdf"
__copyright__   = "Copyright 2017, Planet Earth"


class Read():

    def read_post(self, bot_name, subreddit_name, number_of_submissions):

        reddit = praw.Reddit(bot_name)
        subreddit = reddit.subreddit(subreddit_name)

        for submission in subreddit.hot(limit=number_of_submissions):
            print("Title: ", submission.title)
            print("Text: ", submission.selftext)
            print("Score: ", submission.score)
            print("---------------------------------\n")