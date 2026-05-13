from models.db import db
from models.models_bed import Bed
def add_bed_service(data):
    bed=Bed(
        patient=data["patient"],
        status=data["status"]
    )

    db.session.add(bed)
    db.session.commit()