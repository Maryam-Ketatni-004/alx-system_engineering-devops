#!/usr/bin/python3
"""Module to query number of subscribers of a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Function to query number of subscribers of a subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    after = response.json().get('data').get('after')
    if after is None:
        return hot_list
    for i in response.json().get('data').get('children'):
        hot_list.append(i.get('data').get('title'))
    return recurse(subreddit, hot_list, after)
