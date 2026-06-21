from flask import Blueprint, redirect, render_template, request, url_for, flash, session
from app.utils.form import LoginForm
from app.models.admin import Admin
from app.models.admin import PrincipalDataInfo
from app.utils.form import ShiftSelectForm

login_bp = Blueprint(
    "login",
    __name__,
    url_prefix="/login"
)

DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin123"


@login_bp.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Admin Login
        if (
            username == DEFAULT_USERNAME
            and password == DEFAULT_PASSWORD
        ):
            session.clear()

            session["admin"] = True

            flash(
                "Admin Login Successful",
                "success"
            )

            return redirect(
                url_for(
                    "admin_dashboard.admin_dashboard"
                )
            )

        # Principal Login
        principal = PrincipalDataInfo.query.filter_by(
            username=username,
            password=password
        ).first()

        if principal:

            session.clear()

            session["temp_principal_id"] = principal.principal_id

            return redirect(
                url_for(
                    "login.select_shift"
                )
            )

        flash(
            "Invalid Username Or Password",
            "danger"
        )

    return render_template(
        "auth/login.html",
        login_form=form
    )

@login_bp.route("/logout")
def logout():
    session.pop("admin", None)  # Remove admin session
    flash("Logged out successfully!", "success")
    return redirect(url_for("login.login"))


@login_bp.route(
    "/select_shift",
    methods=["GET", "POST"]
)
def select_shift():

    if "temp_principal_id" not in session:
        return redirect(
            url_for("login.login")
        )

    form = ShiftSelectForm()

    if form.validate_on_submit():

        session["principal"] = True

        session["principal_id"] = session[
            "temp_principal_id"
        ]

        session["shift"] = form.shift.data

        session.pop(
            "temp_principal_id",
            None
        )

        flash(
            f"{form.shift.data} Shift Selected",
            "success"
        )

        return redirect(
            url_for(
                "principal_dashboard.principal_dashboard"
            )
        )

    return render_template(
        "auth/select_shift.html",
        form=form
    )