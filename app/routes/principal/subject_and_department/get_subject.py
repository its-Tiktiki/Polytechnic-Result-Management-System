from flask import jsonify
from flask import Blueprint,request
from app.models.assign import Curriculum

get_subject_bp = Blueprint("get_subject", __name__, url_prefix="/api/get_subject")

@get_subject_bp.route("/")
def get_subjects():
    department_id = request.args.get("department_id", type=int)
    semester = request.args.get("semester", type=int)

    if not department_id or not semester:
        return jsonify([])

    curriculum_rows = Curriculum.query.filter_by(
        department_id=department_id,
        semester=semester
    ).all()

    data = [
        {
            "subject_id": row.subject.subject_id,
            "subject_name": row.subject.subject_name,
            "subject_code": row.subject.subject_code
        }
        for row in curriculum_rows if row.subject is not None
    ]

    return jsonify(data)