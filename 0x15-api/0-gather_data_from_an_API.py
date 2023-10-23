#!/usr/bin/python3
"""This script gathers data from an api"""

from sys import argv
import requests

if __name__ == "__main__":

    users = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}").json()['name']

    to_dos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")

    completed = [i for i in to_dos.json() if i['completed'] is True]

    print(f"Employee {users} is done
          with tasks({len(completed)}/{len(to_dos.json())}): ")
    for i in completed:
        print(f"\t{i['title']}")
