#!/usr/bin/env python

"""reply_post.py: reply in reddit."""

import praw
import pdb
import re
import os

__author__      = "Asdf"
__copyright__   = "Copyright 2017, Planet Earth"


# Create the Reddit instance
reddit = praw.Reddit('bot1')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

with open("posts_replied_to.txt", "r") as f:
    posts_replied_to = f.read()
    posts_replied_to = posts_replied_to.split("\n")
    posts_replied_to = list(filter(None, posts_replied_to))


limit = 1

subreddit = reddit.subreddit('pythonforengineers')


for submission in subreddit.hot(limit=10):
    print(submission.title)

    if limit:
        if submission.title == "fake news":
            submission.reply("here I am")
        limit = 0

    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Botty bot says: Me too!!")



print("Bot replying to : ", submission.title)
posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
