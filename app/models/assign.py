from app.extensions import db
from datetime import datetime

class Department(db.Model):
    __tablename__ = "departments"
    department_code = db.Column(db.Integer, nullable=False,primary_key=True)
    department_name = db.Column(db.String(150), nullable=False, unique=True)
    principal_id = db.Column(
        db.Integer,
        db.ForeignKey("principal_info.principal_id"),
        nullable=False
    )

class Subjects(db.Model):
    __tablename__ = "subjects"

    subject_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_code = db.Column(db.String(10), nullable=False)
    subject_name = db.Column(db.String(150), nullable=False)
    principal_id = db.Column(
        db.Integer,
        db.ForeignKey("principal_info.principal_id"),
        nullable=False
    )

class Curriculum(db.Model):
    
    __tablename__ = "curriculum"

    curriculum_id = db.Column(
        db.Integer,
        primary_key=True
    )

    department_code = db.Column(
        db.String(20),
        db.ForeignKey(
            "departments.department_code"
        )
    )

    semester = db.Column(
        db.Integer
    )

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "subjects.subject_id"
        )
    )

    subject = db.relationship(
        "Subjects"
    )

class TeacherAssignment(db.Model):
    
    __tablename__ = "teacher_assignments"

    assignment_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    teacher_id = db.Column(
        db.String(20),
        db.ForeignKey(
            "teacher_info.teacher_id"
        ),
        nullable=False
    )

    department_code = db.Column(
        db.String(20),
        db.ForeignKey(
            "departments.department_code"
        ),
        nullable=False
    )

    semester = db.Column(
        db.Integer,
        nullable=False
    )

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "subjects.subject_id"
        ),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )