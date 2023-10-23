#!/usr/bin/python3
"""This script exportd data to json"""
from sys import argv
import json
import requests


if __name__ == "__main__":

    user_id = argv[1]

    username = requests.get(
          f"https://jsonplaceholder.typicode.com/users/{argv[1]}").json()
    ['username']

    to_dos = requests.get(
          f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")

    completed = [i for i in to_dos.json() if i['completed'] is True]

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": i['title'],
                "completed": i['completed'],
                "username": username
            } for i in to_dos.json()]}, jsonfile)
