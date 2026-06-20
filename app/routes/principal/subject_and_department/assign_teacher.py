from flask import Blueprint, redirect, url_for, render_template, session, flash, request, jsonify
from app.utils.assign_form import AssignTeacherForm # Updated spelling
from app.models.principal import TeacherAddInfo
from app.models.assign import Department, AssignTeacher, Curriculum
from app.extensions import db

# ---- HTML Route ----
assign_teacher_bp = Blueprint("assign_teacher", __name__, url_prefix="/assign_teacher")

@assign_teacher_bp.route("/", methods=["GET", "POST"])
def assign_teacher():
    if not session.get("principal"):
        return redirect(url_for("login.login"))
    
    form = AssignTeacherForm()
    
    # Populate Teacher Choices
    teachers = TeacherAddInfo.query.all()
    form.teacher_id.choices = [
        (t.teacher_id, f"{t.teacher_id} - {t.first_name} {t.last_name}") 
        for t in teachers
    ]

    # Populate Department Choices (Using department_id, NOT department_code)
    departments = Department.query.all()
    form.department_id.choices = [
        (d.department_id, f"{d.department_code} - {d.department_name}") 
        for d in departments
    ]
    
    if form.validate_on_submit():
        # Ensure a subject was actually selected by the user
        if not form.subject_id.data:
            flash("Please select a subject before assigning.", "danger")
            return render_template("principal/subject_and_department/assign_teacher.html", form=form)

        assign = AssignTeacher(
            teacher_id=form.teacher_id.data,
            department_id=form.department_id.data, # Fixed mismatch here
            semester=form.semester.data,
            subject_id=form.subject_id.data
        )
        
        db.session.add(assign)
        db.session.commit()
        flash("Teacher assigned successfully", "success")

        return redirect(url_for("assign_subject_dashboard.assign_subject_dashboard"))
    
    # Optional: If you want to see validation errors in your console for debugging
    if form.errors:
        print("Form Errors:", form.errors)
    
    return render_template("principal/subject_and_department/assign_teacher.html", form=form)