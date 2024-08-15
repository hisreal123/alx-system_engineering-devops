#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns the numbes of subreddits fmor a given sub"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # headers =  {'User-Agent': 'custom-user-agent'}


    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0
