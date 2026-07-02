from flask import Blueprint, render_template, flash, redirect, url_for,session
from app.extensions import db
from app.models.assign import Department, TeacherAssignment, Curriculum
from app.models.principal import TeacherAddInfo
from app.utils.assign_form import TeacherAssignmentForm

assign_teacher_bp = Blueprint(
    "assign_teacher",
    __name__,
    url_prefix="/assign_teacher"
)

@assign_teacher_bp.route(
    "/assign-teacher",
    methods=["GET", "POST"]
)
def assign_teacher():
    
    form = TeacherAssignmentForm()

    principal_id = session.get("principal_id")
    shift = session.get("shift")

    teachers = TeacherAddInfo.query.filter_by(
        principal_id=principal_id,
        shift=shift
    ).all()

    form.teacher_id.choices = [
        (t.teacher_id, f"{t.teacher_id} - {t.first_name} {t.last_name}")
        for t in teachers
    ]

    departments = Department.query.filter_by(
        principal_id=principal_id
    ).all()

    form.department_id.choices = [
        (d.department_id, d.department_name)
        for d in departments
    ]

    if form.department_id.data and form.semester.data:

        curriculum_rows = Curriculum.query.filter_by(
            department_id=form.department_id.data, 
            semester=int(form.semester.data)
        ).all()

        form.subject_id.choices = [
            (
                row.subject.subject_id,
                f"{row.subject.subject_code} - {row.subject.subject_name}"
            )
            for row in curriculum_rows
        ]

    if form.validate_on_submit():

        aassignment = TeacherAssignment(
            teacher_id=form.teacher_id.data,
            department_id=form.department_id.data,
            semester=form.semester.data,
            subject_id=form.subject_id.data
        )

        db.session.add(aassignment)
        db.session.commit()

        flash("Teacher Assigned Successfully", "success")

        return redirect(url_for("assign_subject_dashboard.assign_subject_dashboard"))

    return render_template(
        "principal/subject_and_department/assign_teacher.html",
        form=form
    )