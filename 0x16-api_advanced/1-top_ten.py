#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed
for a given subreddit."""

import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyUserAgent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print(None)

        if response.status_code == 200:
            top_ten = [
                    (child["data"]["name"],
                        child["data"]["title"],
                        child["data"]["ups"])
                    for child in response.json()["data"]["children"]
                    ][:10]
            [print(post[1]) for post in top_ten]

    except requests.exceptions.RequestException as e:
        print(None)
