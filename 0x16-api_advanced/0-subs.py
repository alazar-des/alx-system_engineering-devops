#!/usr/bin/python3
""" query reddit api and return of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """ Return number of subscribers of subreddit.
    """
    endpoint = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {'User-Agent': 'Holberton/0.0.1'}
    res = requests.get(endpoint, headers=headers)
    res_json = res.json()
    if res.status_code == 200:
        return res_json['data']['subscribers']
    return 0
