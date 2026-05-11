
from flask import  render_template, request, Blueprint 
from services.services_patient import add_patient_service
from models.db import db
from models.models_patient import Patient

patient_bp= Blueprint('patient',__name__)

@patient_bp.route('/add_patient',methods=['GET','POST'])
def add_patient():
    if request.method=="POST":
        
        data={
            "name": request.form["name"],
            "age": request.form["age"],
            "phone": request.form["phone"],
            "address": request.form["address"]
        }
        print(data)
        add_patient_service(data)
        print("Data saved successfully")
        return "Data saved successfully"

    return render_template('add_patient.html')


@patient_bp.route('/view_update_patient',methods=['GET','POST'])
def view_update_patient():
    if request.method=="POST":
        pass
    patients=Patient.query.all()
    # debugging
    if not patients:
        return "No patients found"
    for i in patients:
        print(i.name)
    # debugging
    return render_template('view_update_patient.html', patients=patients)

@patient_bp.route('/edit_patient/<int:patient_id>', methods=['GET', 'POST'])
def edit_patient(patient_id):
    patient=Patient.query.get(patient_id)
    if request.method == "POST":
        patient.name = request.form["name"]
        patient.age = request.form["age"]
        patient.phone = request.form["phone"]
        patient.address = request.form["address"]
        db.session.commit()

        return "UPDATED SUCCESSFULLY"
    return render_template('edit_patient.html', patient=patient)
