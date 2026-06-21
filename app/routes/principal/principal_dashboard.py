from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session

from app.models.principal import TeacherAddInfo

principal_dashboard_bp = Blueprint(
    "principal_dashboard",
    __name__,
    url_prefix="/principal_dashboard"
)

@principal_dashboard_bp.route("/")
def principal_dashboard():

    if not session.get("principal"):
        return redirect(
            url_for("login.login")
        )

    principal_id = session.get(
        "principal_id"
    )

    shift = session.get(
        "shift"
    )

    total_teachers = TeacherAddInfo.query.filter_by(
        principal_id=principal_id,
        shift=shift
    ).count()

    return render_template(
        "principal/principal_dashboard.html",
        total_teachers=total_teachers,
        shift=shift
    )