#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """ returns the number of subscribers (not active users, total subscribers) for a given subreddit. """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'custom-user-agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    return data.get('subscribers')
