#!/usr/bin/python3

# Write a Python script that, using this REST API,
# for a given employee ID, returns information about his/her TODO list progress.
import sys
import requests
import json

# Base url
BASE_URL = 'https://jsonplaceholder.typicode.com/'


def getUser(employee_id):

    try:
        # Fetch employee data
        userResponse = requests.get(BASE_URL + "users/{}".format(employee_id)).json()
        todoResponse = requests.get(BASE_URL + "todos", params={"userId": sys.argv[1]}).json()

        completed = [t.get("title") for t in todoResponse if t.get("completed") is True ]
        print("Employee {} is done with tasks({}/{}):".format(
            userResponse.get('name'), len(completed), len(todoResponse)))
        [print("\t {}".format(c)) for c in completed]

        # print(todoResponse)
    except Exception as err:
        print(str(err))


if __name__ == '__main__':
    getUser(int(sys.argv[1]))
