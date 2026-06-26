from flask import Blueprint,redirect,render_template,session,url_for
from app.models.teacher import AddStudentInfo

teacher_dashboard_bp = Blueprint(
    "teacher_dashboard",
    __name__,
    url_prefix="/teacher_dashboard"
)

@teacher_dashboard_bp.route("/")
def teacher_dashboard():
    if not session.get("teacher"):
        return redirect(url_for("login.login"))

    teacher_id = session.get("teacher_id") 
    total_student = AddStudentInfo.query.filter_by(teacher_id=teacher_id).count()
    
    return render_template("teacher/teacher_dashboard.html",total_student=total_student)