#! usr/bin/python3

import json
import praw
import pandas as pd
import datetime as dt

def main():
    reddit = praw.Reddit(client_id='FAt640gb4SzfuA', \
                         client_secret='TVEfEsSyoBS_lWNoQWpEikr968Q', \
                         user_agent='PoemNews', \
                         username='mlh-throwaway', \
                         password='mlh-throwaway');

    subreddit = reddit.subreddit('WorldNews')

    top_subreddit = subreddit.hot(limit=10)

    for submission in subreddit.hot(limit=1):
        print(submission.title, submission.id)

    topics_dict = { "title":[], \
                    "score":[], \
                    "id":[], "url":[], \
                    "comms_num": [], \
                    "created": [], \
                    "body":[]}

    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)

    topics_data = pd.DataFrame(topics_dict)

    topics_data.to_json(r'reddit_data.json')

if __name__ == '__main__':
    main()
