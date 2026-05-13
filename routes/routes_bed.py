from flask import  render_template, request, Blueprint 
from services.services_bed import add_bed_service
from models.db import db
from models.models_bed import Bed
from models.models_patient import  Patient

bed_bp= Blueprint('bed',__name__)

@bed_bp.route('/add_bed',methods=['GET','POST'])
def add_bed():
    if request.method=="POST":
        data={
            "patient": request.form["patient"],
            "status": request.form["status"]
        }
        add_bed_service(data)
        
        return "bed Data saved successfully"

    patient=Patient.query.all()
    return render_template('add_bed.html',  patient=patient)

@bed_bp.route('/view_update_bed',methods=['GET','POST'])
def view_update_bed():
    beds=Bed.query.all()
    return render_template('view_update_bed.html', beds=beds)

@bed_bp.route('/edit_bed/<int:bed_id>', methods=['GET', 'POST'])
def edit_bed(bed_id):
    bed=Bed.query.get(bed_id)
    if request.method == "POST":
        bed.patient = request.form["patient"]
        bed.status = request.form["status"]
        db.session.commit()

        return "UPDATED SUCCESSFULLY"
    return render_template('edit_bed.html', bed=bed)

