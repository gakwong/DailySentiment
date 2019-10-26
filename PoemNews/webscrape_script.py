#! usr/bin/python3

# python libraries for web scraping
import json
import praw
import pandas as pd
import datetime as dt

# time stamp for json table
def get_date(created):
    return dt.datetime.fromtimestamp(created)

def main( sub ):
    # reddit credentials
    reddit = praw.Reddit(client_id='FAt640gb4SzfuA', \
                         client_secret='TVEfEsSyoBS_lWNoQWpEikr968Q', \
                         user_agent='PoemNews', \
                         username='mlh-throwaway', \
                         password='mlh-throwaway');



    # subreddit
    subreddit = reddit.subreddit(sub)
    #subreddit = next(x for x in reddit.subreddit(sub).hot() if not x.stickied)
    #hot_subreddit = subreddit.hot(limit=10)

    # ignores pinned posts
    hot_subreddit = []
    stickied_post = []

    for sticky in subreddit.hot(limit=10):
        if sticky.stickied:
            stickied_post.append(sticky.id)

    for submission in subreddit.hot(limit=10):
        if submission.id not in stickied_post:
            hot_subreddit.append(submission)
    #

    for submission in subreddit.hot(limit=1):
        print(submission.title, submission.id)

    # headline dictionaries
    topics_dict = { "title":[], \
                    #"score":[], \
                    #"id":[], \
                    "url":[], \
                    #"comms_num": [], \
                    "created": []}
                    #"body":[]}

    for submission in hot_subreddit:
        topics_dict["title"].append(submission.title)
        #topics_dict["score"].append(submission.score)
        #topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        #topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        #topics_dict["body"].append(submission.selftext)

    topics_data = pd.DataFrame(topics_dict)

    _timestamp = topics_data["created"].apply(get_date)
    topics_data = topics_data.assign(timestamp = _timestamp)

    topics_data.to_json(r'reddit_data.json')

    return topics_data;
