from app.extensions import db
from datetime import datetime

class AddStudentInfo(db.Model):
    __tablename__ = "student_data"

    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_roll = db.Column(db.Integer, unique=True, nullable=False)
    student_full_name = db.Column(db.String(250), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    group = db.Column(db.String(1))

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.department_id"),
        nullable=False
    )

    principal_id = db.Column(
        db.Integer,
        db.ForeignKey("principal_info.principal_id")
    )
    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teacher_info.teacher_id")
    )

