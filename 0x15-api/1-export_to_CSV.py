#!/usr/bin/python3
"""
Return a todo list of employee form RESTful API.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    resp = requests.get('https://jsonplaceholder.typicode.com/todos')
    resp_json = resp.json()
    file_name = sys.argv[1] + ".csv"
    with open(file_name, mode='w') as empl:
        empl_write = csv.writer(empl, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for emp in resp_json:
            if emp.get("userId") == int(sys.argv[1]):
                empl_write.writerow([emp.get("userId"), emp.get("id"),
                                     emp.get("completed"), emp.get("title")])
