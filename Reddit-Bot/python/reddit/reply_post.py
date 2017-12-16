#!/usr/bin/env python

"""reply_post.py: reply in reddit."""

import praw
import pdb
import re
import os

__author__      = "Asdf"
__copyright__   = "Copyright 2017, Planet Earth"


class Reply:

    def reply(self, bot_name, subreddit_name, number_of_submissions):

        reddit = praw.Reddit(bot_name)
        subreddit = reddit.subreddit(subreddit_name)

        # check already replied posts
        posts_replied_to = Reply().read_post()

        limit = 1

        for submission in subreddit.hot(limit=number_of_submissions):
            print(submission.title)

            # if limit:
            #     if submission.title == "fake news":
            #         submission.reply("here I am")
            #     limit = 0

            if submission.id not in posts_replied_to:
                print("here first")
                if re.search("Test Bot Scheduler", submission.title, re.IGNORECASE):
                    print("here second")
                    submission.reply("Me too!!")

        print("Bot replying to : ", submission.title)

        # write to file which post was replied to
        Reply().write_post(posts_replied_to, submission)


        posts_replied_to.append(submission.id)
        with open("posts_replied_to.txt", "w") as f:
            for post_id in posts_replied_to:
                f.write(post_id + "\n")

    def read_post(self):
        if not os.path.isfile("posts_replied_to.txt"):
            posts_replied_to = []
        else:
            with open("posts_replied_to.txt", "r") as f:
               posts_replied_to = f.read()
               posts_replied_to = posts_replied_to.split("\n")
               posts_replied_to = list(filter(None, posts_replied_to))

        return posts_replied_to

    def write_post(self, posts_replied_to, submission):
        posts_replied_to.append(submission.id)
        with open("posts_replied_to.txt", "w") as f:
            for post_id in posts_replied_to:
                f.write(post_id + "\n")
