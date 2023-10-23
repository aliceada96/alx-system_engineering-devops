#!/usr/bin/python3
"""this script exports data to csv"""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]

    username = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}").json()[
            'username']

    to_dos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")

    completed = [i for i in to_dos.json() if i['completed'] is True]

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, i['completed'], i['title']]
         ) for i in to_dos.json()]
