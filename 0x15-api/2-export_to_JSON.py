#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    response = requests.get(url)
    user = response.json()
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1])
    response = requests.get(url)
    todos = response.json()
    with open('{}.json'.format(argv[1]), 'w') as jsonfile:
        json.dump({argv[1]: [{"task": todo.get('title'),
                              "completed": todo.get('completed'),
                              "username": user.get('username')}
                             for todo in todos]}, jsonfile)
