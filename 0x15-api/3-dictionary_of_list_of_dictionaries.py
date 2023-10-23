#!/usr/bin/python3

import requests
import json

if __name__ == "__main":
    # Make a request to get the user data
    users = requests.get("https://jsonplaceholder.typicode.com/users")

    if users.status_code == 200:
        users_data = users.json()

        # Create a dictionary to store tasks for each user
        todo_dict = {}

        # Iterate through each user
        for user in users_data:
            user_id = user['id']
            username = user['username']

            # Make a request to get the user's tasks
            tasks = requests.get(
                f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")

            if tasks.status_code == 200:
                tasks_data = tasks.json()

                user_tasks = []

                # Iterate through the tasks and create task dictionaries
                for task in tasks_data:
                    task_dict = {
                        "username": username,
                        "task": task['title'],
                        "completed": task['completed']
                    }
                    user_tasks.append(task_dict)

                todo_dict[user_id] = user_tasks

        # Write the data to a JSON file
        with open('todo_all_employees.json', 'w') as jsonfile:
            json.dump(todo_dict, jsonfile, indent=4)
    else:
        print(
            f"Failed to retrieve user data. Status code: {users.status_code}")
