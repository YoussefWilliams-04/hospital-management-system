from models.db import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    department = db.Column(db.String(100))
