from flask import Blueprint,request
from flask import jsonify
from app.models.assign import Curriculum

get_subject_bp = Blueprint(
    "get_subject",
    __name__,
    "/get_subject"
)

@get_subject_bp.route(
    "/api/get-subjects"
)
def get_subjects():
    department_id = request.args.get("department_id")
    semester = request.args.get("semester")

    if not department_id or not semester:
        return jsonify([])

    curriculum_rows = Curriculum.query.filter_by(
        department_code=department_id,   
        semester=int(semester)          
    ).all()

    data = [
        {
            "subject_id": row.subject.subject_id,
            "subject_name": row.subject.subject_name,
            "subject_code": row.subject.subject_code,
        }
        for row in curriculum_rows
    ]

    return jsonify(data)