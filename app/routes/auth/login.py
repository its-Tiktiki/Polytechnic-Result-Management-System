from flask import Blueprint,redirect,render_template,request,url_for,flash
from app.utils.form import LoginForm
from app.extensions import db
from app.models.admin import Admin

# save default password
DEFUALT_USERNAME = "admin"
DEFUALT_PASSWORD = "admin123"

#admin = Admin(
   # DEFUALT_USERNAME=DEFUALT_USERNAME,
  #  DEFUALT_PASSWORD=DEFUALT_PASSWORD
#)

#db.session.add(admin)
#db.session.commit()

# make blueprint and route
login_bp = Blueprint("login",__name__,url_prefix="/login")

@login_bp.route("/login",methods=["GET","POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
          username = login_form.username.data
          password = login_form.password.data

          print("username:",username)

          if username == DEFUALT_USERNAME and password == DEFUALT_PASSWORD:
                return "Login success"
          else:
                return "invalid username or password"

          

    return render_template("/auth/login.html",login_form=login_form)

@login_bp.route("/admin")
def admin_dashboard():
     return "login success"