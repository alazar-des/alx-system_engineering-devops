#!/usr/bin/python3
""" query reddit api and return of subscribers.
"""
import requests


def top_ten(subreddit):
    """ Print the titles of the 10 hot posts.
    """
    endpoint = "https://www.reddit.com/r/" + subreddit +\
        "/hot.json?limit=10"
    headers = {'User-Agent': 'Holberton/0.0.1'}
    res = requests.get(endpoint, headers=headers)
    res_json = res.json()
    if res.status_code == 200:
        hottest = res_json['data']['children']
        for i in range(len(hottest)):
            print(hottest[i]['data']['title'])
    else:
        print(None)
