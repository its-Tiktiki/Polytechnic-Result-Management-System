from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,IntegerField,SubmitField
from wtforms.validators import DataRequired,Length

class SearchForm(FlaskForm):
    roll = IntegerField(
        "Enter Roll Number", validators=[DataRequired(), Length(min=1, max=10)]
    )
    submit = SubmitField("Search")
    

class LoginForm(FlaskForm):
    username = StringField(
        "Enter username ",validators=[DataRequired(),Length(min=1,max=50)]
    )
    password =PasswordField(
        "Password",validators=[DataRequired(),Length(min=1,max=32)]
    )
    submit = SubmitField("Login")
    
