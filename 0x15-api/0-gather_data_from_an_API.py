#!/usr/bin/python3

# Write a Python script that, using this REST API,
# for a given employee ID, returns information about his/her TODO list progress.
import sys
import requests
import json

# Base url
BASE_URL = 'https://jsonplaceholder.typicode.com/'


def getUser(id):
    print(id)
    try:
        # Fetch employee data
        userResponse = requests.get('{}/users/{}'.format(BASE_URL, id)).json()
        todoResponse = requests.get('{}/users/{}/todos'.format(BASE_URL, id)).json()

        # Extract employee name
        employee_name = userResponse['name']

        # completed task and total tasks
        completed_tasks = [todo for todo in todoResponse if todo['completed']]
        total_tasks = userResponse

        num_of_done_task = len(completed_tasks)
        total_num_of_tasks = len(total_tasks)

        # Display the TODO list progress
        print(f"Employee {employee_name} is done with tasks({num_of_done_task}/{total_num_of_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")

        # print(todoResponse)
    except Exception as err:
        print(str(err))


if __name__ == '__main__':
    getUser(int(sys.argv[1]))
