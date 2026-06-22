from flask import Blueprint,redirect,render_template,session,url_for

teacher_dashboard_bp = Blueprint(
    "teacher_dashboard",
    __name__,
    url_prefix="/teacher_dashboard"
)

@teacher_dashboard_bp.route("/")
def teacher_dashboard():
    if not session.get("teacher"):
        return redirect(url_for("login.login"))
    
    return render_template("teacher/teacher_dashboard.html")