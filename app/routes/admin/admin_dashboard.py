from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app.utils.form import PrincipalDataForm
from app.models.admin import PrincipalDataInfo

admin_bp = Blueprint("admin_dashboard",__name__,url_prefix="/admin_dashboard")
@admin_bp.route("/admin_dashboard",methods=["GET","POST"])
def admin_dashboard():

    if not session.get("admin"):
        return redirect(url_for("auth.login"))
    
    principal_data_form = PrincipalDataForm()
    total = PrincipalDataInfo.query.count()

    return render_template(
        "admin/admin_dashboard.html",
        principal_data_form=principal_data_form,
        total=total
    )
    
@admin_bp.route("/views_principals")
def view_principals():

    principals = PrincipalDataInfo.query.all()

    return render_template(
        "admin/view_principals.html",
        principals = principals
    )



