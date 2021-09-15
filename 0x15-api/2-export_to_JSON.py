#!/usr/bin/python3
"""
Return a todo list of employee form RESTful API.
"""
import json
import requests
import sys


if __name__ == "__main__":
    emp_path = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    resp_emp = requests.get(emp_path)
    resp_empj = resp_emp.json()
    name = resp_empj.get("username")

    resp = requests.get('https://jsonplaceholder.typicode.com/todos')
    resp_json = resp.json()
    file_name = sys.argv[1] + ".json"
    empl_list = []
    for emp in resp_json:
        if emp["userId"] == int(sys.argv[1]):
            emp_dic = {}
            emp_dic["task"] = emp.get("title")
            emp_dic["completed"] = emp.get("completed")
            emp_dic["username"] = name
            empl_list.append(emp_dic)
    empl_json = {}
    empl_json[sys.argv[1]] = empl_list
    with open(file_name, mode='w') as empl:
        json.dump(empl_json, empl)
