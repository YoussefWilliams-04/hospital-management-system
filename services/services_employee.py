from models.models_employee import Employee
from models.db import db
def add_employee_service(data):

    employee = Employee(
        name=data["name"],
        role=data["role"],
        phone=data["phone"],
        department=data["department"]
    )
    db.session.add(employee)
    db.session.commit()
