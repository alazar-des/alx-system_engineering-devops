#!/usr/bin/python3
""" query reddit api and return of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """ Return number of subscribers of subreddit.
    """
    auth = requests.auth.HTTPBasicAuth('G9u68I7sbiR7wBXzQlM30A',
                                       'ViWkBYcAYOQbdh4T-HExgE5L4T4bfw')
    data = {'grant_type': 'password',
            'username': 'AlazarDes',
            'password': 'password'}
    headers = {'User-Agent': 'Holberton/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    endpoint = "https://oauth.reddit.com/r/" + subreddit
    res = requests.get(endpoint, headers=headers)
    res_json = res.json()
    if res.status_code == 200:
        return res_json['data']['children'][0]['data']['subreddit_subscribers']
    return 0
