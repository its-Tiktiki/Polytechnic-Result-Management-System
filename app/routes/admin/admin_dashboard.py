from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app.utils.form import PrincipalDataForm

admin_bp = Blueprint("admin_dashboard",__name__,url_prefix="/admin_dashboard")
@admin_bp.route("/admin_dashboard",methods=["GET","POST"])
def admin_dashboard():

    if not session.get("admin"):
        return redirect(url_for("auth.login"))
    
    principal_data_form = PrincipalDataForm()

    return render_template("admin/admin_dashboard.html",principal_data_form=principal_data_form)
    





