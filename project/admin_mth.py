import json
import requests
from config import CONFIG


def add_employee(name, surname, position, phone, email):
    arguments = locals()
    new_employee = {}
    print(arguments)
    for arg in arguments:
        new_employee.update({arg: arguments[arg]})

    print(new_employee)

    response = requests.post(f"{CONFIG['api']['url']}/employees", json=new_employee)
    return int(response.text)


def list_of_employees():
    response = requests.get(f"{CONFIG['api']['url']}/employees")
    employees = json.loads(response.text)

    return employees


def get_employee_by_id(id):
    response = requests.get(f"{CONFIG['api']['url']}/employees/{id}")
    employee = json.loads(response.text)

    return employee


def get_employee_by_name(name):
    response = requests.get(f"{CONFIG['api']['url']}/employees/{name}")
    employee = json.loads(response.text)

    return employee


def update_employee(employee):
    print(employee)
    response = requests.put(f"{CONFIG['api']['url']}/employees/{employee['id']}", json=employee)
    employee = json.loads(response.text)

    return employee['id']


def delete_employee(id):
    requests.delete(f"{CONFIG['api']['url']}/employees/{id}")