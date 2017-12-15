#!/usr/bin/env python

"""read_post.py: read basic stuff in reddit an dprint it to the console."""

import praw

__author__      = "Asdf"
__copyright__   = "Copyright 2017, Planet Earth"

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=10):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")