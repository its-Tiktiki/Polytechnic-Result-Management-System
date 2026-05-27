from flask import Blueprint, render_template
from app.utils.form import SearchForm

home_bp = Blueprint('home', __name__,url_prefix="/")
@home_bp.route('/')
def home():
    search = SearchForm()
    return render_template("home/home.html", search=search)

