#!/usr/bin/python3
""" query reddit api and return of subscribers.
"""
import re
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


def check_title(title, word_list, dic_keyword):
    """ check tilte if keywords exist and increment if so."""
    if len(word_list) == 0:
        return dic_keyword
    else:
        if re.search(r'\b({0})\b'.format(word_list[0]),
                     title, flags=re.IGNORECASE):
            if word_list[0] in dic_keyword:
                dic_keyword[word_list[0]] += 1
            else:
                dic_keyword[word_list[0]] = 1
        return check_title(title, word_list[1:], dic_keyword)


def check_keywords(title_list, word_list, dic_keyword):
    """ check word lists exist in title."""
    if len(title_list) == 0:
        return dic_keyword
    else:
        check_title(title_list[0], word_list, dic_keyword)
        return check_keywords(title_list[1:], word_list, dic_keyword)


def print_occ(title_list, keys):
    """ print occurence of keyword with their count."""
    if len(keys) == 0:
        return
    else:
        print('{}: {}'.format(keys[0], title_list[keys[0]]))
        print_occ(title_list, keys[1:])


def count_words(subreddit, word_list):
    """ count title with word_list.
    """
    title_list = recurse(subreddit, hot_list=[])
    if title_list is not None:
        word_dic = check_keywords(title_list, word_list, dic_keyword={})
        sorted_word = dict(sorted(word_dic.items(),
                                  key=lambda item: item[1], reverse=True))
        print_occ(sorted_word, list(sorted_word.keys()))
