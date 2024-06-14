import sqlite3
from flask import jsonify
from config import CONFIG

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def get_db_connection():
    db_conn = sqlite3.connect(CONFIG["database"]["name"])
    db_conn.row_factory = dict_factory
    return db_conn

def read_all():
    ALL_EMPLOYEES = "SELECT * FROM employees"
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(ALL_EMPLOYEES)
    result = cursor.fetchall()
    db_conn.close()
    return jsonify(result)

def create(employee):
    INSERT_EMPLOYEE = "INSERT INTO employees (name, surname, position, phone, email) VALUES (?, ?, ?, ?, ?)"
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(INSERT_EMPLOYEE, (employee["name"], employee["surname"], employee["position"], employee["phone"], employee["email"]))
    db_conn.commit()
    new_employee_id = cursor.lastrowid
    cursor.close()
    return new_employee_id, 201

def read_employeeById(id):
    ONE_EMPLOYEE = "SELECT * FROM employees WHERE id = ?"
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(ONE_EMPLOYEE, (id,))
    result = cursor.fetchall()
    db_conn.close()
    if len(result) < 1:
        return "Not found", 404
    return jsonify(result[0])

def read_employeeByName(name):
    NAME_EMPLOYEE = "SELECT * FROM employees WHERE name = ?"
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(NAME_EMPLOYEE, (name,))
    result = cursor.fetchall()
    return jsonify(result)

def update_employeeById(id, employee):
    UPDATE_EMPLOYEE = """
    UPDATE employees
    SET name = ?, surname = ?, position = ?, phone = ?, email = ?
    WHERE id = ?
    """
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(UPDATE_EMPLOYEE, (employee['name'], employee['surname'], employee['position'], employee['phone'], employee['email'], id))
    db_conn.commit()
    return read_employeeById(id)

def delete_employeeById(id):
    DELETE_EMPLOYEE = "DELETE FROM employees WHERE id = ?"
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(DELETE_EMPLOYEE, (id,))
    db_conn.commit()
    return "Successfully deleted", 204
