#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'custom-user-agent'}

    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    [print(c.get("data").get("title")) for c in data.get("children")]
