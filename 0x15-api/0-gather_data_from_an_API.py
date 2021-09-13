#!/usr/bin/python3
"""
Return a todo list of employee form RESTful API.
"""
import requests
import sys


if __name__ == "__main__":
    resp = requests.get('https://jsonplaceholder.typicode.com/todos')
    resp_json = resp.json()
    empl = []
    comp_tasks = []
    for emp in resp_json:
        if emp.get("userId") == int(sys.argv[1]):
            empl.append(emp)
    for tasks in empl:
        if tasks.get("completed"):
            comp_tasks.append(tasks.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(sys.argv[1],
                                                          len(comp_tasks),
                                                          len(empl)))
    for task in comp_tasks:
        print("\t {}".format(task))
