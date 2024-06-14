"The admin dashboard"
from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
import os
from config import CONFIG
from admin_mth import *

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

# User credentials for login
users = {
    "admin": "123456"  
}

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session['username'] = username
            print(f"Logged in as {username}")  # Debug statement
            return redirect(url_for("index"))
        else:
            error = "Invalid Credentials. Please try again."
            return render_template("login.html", error=error)
    return render_template("login.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.pop('username', None)
    print("Logged out")  # Debug statement
    return redirect(url_for("login"))

def login_required(f):
    def wrap(*args, **kwargs):
        if 'username' in session:
            print(f"Access granted to {session['username']}")  # Debug statement
            return f(*args, **kwargs)
        else:
            print("Access denied. Redirecting to login.")  # Debug statement
            return redirect(url_for('login'))
    wrap.__name__ = f.__name__
    return wrap

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    employees = list_of_employees()
    return render_template("index.html", employees=employees)

@app.template_global()
def static_include(filename):
    fullpath = os.path.join(app.static_folder, filename)
    with open(fullpath, 'r') as f:
        return f.read()

@app.route("/new/", methods=["GET", "POST"])
@login_required
def newemployee():
    if request.method == "GET":
        return render_template("new_employee.html")
    elif request.method == "POST":
        newemployee = {}
        for key, value in request.form.items():
            newemployee[key] = value.strip()

        newemployee["id"] = add_employee(newemployee["name"], newemployee["surname"], newemployee["position"], newemployee["phone"], newemployee["email"])
        return render_template("new_employee.html", employee=newemployee)
    return make_response("Invalid request", 400)

@app.route("/deleteemployee/<int:id>", methods=["POST"])
@login_required
def deleteemployee(id):
    delete_employee(id)
    return redirect(url_for('index'))

@app.route("/edit_employee/<int:id>", methods=["GET", "POST"])
@login_required
def editemployee(id):
    if request.method == "GET":
        employee = get_employee_by_id(id)
        return render_template("edit_employee.html", employee=employee)
    elif request.method == "POST":
        employee = {"id": id}
        for key, value in request.form.items():
            employee[key] = value.strip()
        update_employee(employee)
        return redirect(url_for('index'))
    return make_response("Invalid request", 400)

if __name__ == "__main__":
    app.run(host=CONFIG["frontend"]["listen_ip"], port=CONFIG["frontend"]["port"], debug=CONFIG["frontend"]["debug"])
