#!/usr/bin/python3

# Write a Python script that, using this REST API,
# for a given employee ID, returns information about his/her TODO list progress.
import sys
import requests
import json

# Base url


if __name__ == '__main__':
    BASE_URL = 'https://jsonplaceholder.typicode.com/'
    userResponse = requests.get(BASE_URL + "users/{}".format(sys.argv[1])).json()
    todoResponse = requests.get(BASE_URL + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todoResponse if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        userResponse.get('name'), len(completed), len(todoResponse)))
    [print("\t {}".format(c)) for c in completed]
