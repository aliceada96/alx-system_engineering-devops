#!/usr/bin/python3
"""This script exportd data to json"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    to_dos = requests.get(
          f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": i['title'],
                "completed": i['completed'],
                "username": username
            } for i in to_dos.json()]}, jsonfile)
