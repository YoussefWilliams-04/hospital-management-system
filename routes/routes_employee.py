from models.models_employee import Employee
from flask import Blueprint, render_template, request
from models.db import db
from services.services_employee import add_employee_service

employee_bp = Blueprint('employee', __name__)

@employee_bp.route("/add_employee", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        data = request.form
        add_employee_service(data)
        return "Employee added successfully"
    return render_template("add_employee.html")

@employee_bp.route('/view_update_employee')
def view_update_employee():
    employees = Employee.query.all()
    return render_template("view_update_employee.html", employees=employees)

@employee_bp.route('/edit_employee/<int:id>', methods=["GET", "POST"])
def edit_employee(id):
    employee = Employee.query.get(id)
    if request.method == "POST":
        employee.name = request.form["name"]
        employee.role = request.form["role"]
        employee.phone = request.form["phone"]
        employee.department = request.form["department"]
        db.session.commit()
        return "UPDATED SUCCESSFULLY"
    return render_template("edit_employee.html", employee=employee)