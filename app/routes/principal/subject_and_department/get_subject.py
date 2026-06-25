from flask import Blueprint, request, jsonify
from app.models.assign import Curriculum

get_subject_bp = Blueprint(
    "get_subject",
    __name__,
    url_prefix="/api/get-subjects"
)


@get_subject_bp.route("/", methods=["GET"])
def get_subjects():
    
    # --------------------------
    # Get query params safely
    # --------------------------
    department_id = request.args.get("department_id", type=int)
    semester = request.args.get("semester", type=int)

    # --------------------------
    # Validation
    # --------------------------
    if not department_id or not semester:
        return jsonify([])

    # --------------------------
    # IMPORTANT FIX:
    # use department_id NOT department_code
    # --------------------------
    curriculum_rows = Curriculum.query.filter_by(
        department_id=department_id,
        semester=semester
    ).all()

    # --------------------------
    # Build response
    # --------------------------
    data = [
        {
            "subject_id": row.subject.subject_id,
            "subject_name": row.subject.subject_name,
            "subject_code": row.subject.subject_code,
        }
        for row in curriculum_rows
        if row.subject
    ]

    return jsonify(data)