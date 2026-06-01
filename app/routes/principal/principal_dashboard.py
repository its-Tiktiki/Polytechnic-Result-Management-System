from flask import Blueprint,redirect,url_for,render_template,session,flash

principal_dashboard_bp = Blueprint("principal_dashboard",__name__,url_prefix="/ptincipal_dashboard")

def principal_dashboard():
    
    if not session.get("principal"):
        return redirect(url_for('auth.login'))
    
    return render_template("principal/principal_dashboard.html")