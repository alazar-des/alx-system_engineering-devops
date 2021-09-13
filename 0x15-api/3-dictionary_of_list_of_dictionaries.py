#!/usr/bin/python3
"""
Return a todo list of employee form RESTful API.
"""
import json
import requests


if __name__ == "__main__":
    resp = requests.get('https://jsonplaceholder.typicode.com/todos')
    resp_json = resp.json()
    file_name = "todo_all_employees.json"
    empl_json = {}

    for emp in resp_json:
        emp_dic = {"username": emp.get("id"),
                   "task": emp.get("title"),
                   "completed": emp.get("completed")}
        if str(emp["userId"]) not in empl_json:
            empl_list = [emp_dic]
            empl_json[str(emp.get("userId"))] = empl_list
        else:
            empl_json[str(emp.get("userId"))].append(emp_dic)

    with open(file_name, mode='w') as empl:
        json.dump(empl_json, empl)
