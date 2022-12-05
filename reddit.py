import praw
import time

reddit = praw.Reddit(client_id='p5qoOX_9X83J0gZQaJjk5w',
                     client_secret='HSJm4JXYArA3GoElueROt37A5u4IfA',
                     username='zubastilla',
                     password='Pukunqazwsxqazwsx1',
                     user_agent='MyAPI/0.0.1')

def get_images(subreddit, number_of_posts):
    subreddit = reddit.subreddit(subreddit)

    hot_python = subreddit.hot(limit=number_of_posts)

    # post_dict = {}
    post_list = []
    for sub in hot_python:
        if not sub.stickied and (int(time.time())-int(sub.created)<86400):
            # post_dict[sub.id] = {'title':sub.title,
            # 'url':sub.url,'ups':sub.ups,'created':int(sub.created)}
            print(sub)
            post_list.append(sub.url)
    # return post_dict
    return post_list

get_images('greentext',5)