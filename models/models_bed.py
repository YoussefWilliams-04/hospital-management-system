from models.db import db 

class Bed (db.Model):
    id =db.Column(db.Integer, primary_key=True)
    patient = db.Column(db.String(100))
    status= db.Column(db.String(20))