import praw
import time

import constants

reddit = praw.Reddit(client_id=constants.REDDIT_CLIENT_ID,
                     client_secret=constants.REDDIT_CLIENT_SECRET,
                     username=constants.REDDIT_USERNAME,
                     password=constants.REDDIT_PASSWORD,
                     user_agent=constants.REDDIT_USER_AGENT)

def get_images(subreddit, number_of_posts):
    subreddit = reddit.subreddit(subreddit)

    hot_python = subreddit.hot(limit=number_of_posts)

    # post_dict = {}
    post_list = []
    for sub in hot_python:
        if not sub.stickied and (int(time.time())-int(sub.created)<86400):
            # post_dict[sub.id] = {'title':sub.title,
            # 'url':sub.url,'ups':sub.ups,'created':int(sub.created)}
            post_list.append(sub.url)
    # return post_dict
    return post_list