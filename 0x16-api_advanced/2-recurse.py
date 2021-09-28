#!/usr/bin/python3
""" query reddit api and return of subscribers.
"""
import requests


def append_title(child_list, hot_list=[]):
    """ append list recursively.
    """
    if len(child_list) == 0:
        return hot_list
    else:
        hot_list.append(child_list[0]['data']['title'])
        return append_title(child_list[1:], hot_list)


def recurse(subreddit, hot_list=[], after=""):
    """ Print the titles of the 10 hot posts.
    """
    endpoint = "https://www.reddit.com/r/" + subreddit +\
        "/hot.json?after=" + after
    headers = {'User-Agent': 'Holberton/0.0.1'}
    res = requests.get(endpoint, headers=headers)
    if res.status_code == 200:
        res_json = res.json()
        hottest = res_json['data']
        append_title(hottest['children'], hot_list)
        # hot_list.append(hottest['children'][0]['data']['title'])
        if hottest['after'] is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, hottest['after'])
    else:
        return None
