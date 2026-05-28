from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,IntegerField,SubmitField
from wtforms.validators import DataRequired,Length

class SearchForm(FlaskForm):
    roll = IntegerField(
        "Enter Roll Number", 
         validators=[DataRequired(), Length(min=1, max=10)]
    )
    submit = SubmitField("Search")
    

class LoginForm(FlaskForm):
    username = StringField(
        "Enter username ",
         validators=[DataRequired(),Length(min=1,max=50)]
    )
    password =PasswordField(
        "Password",
         validators=[DataRequired(),Length(min=1,max=32)]
    )
    submit = SubmitField("Login")



class PrincipalDataForm(FlaskForm):
    id = IntegerField(
        "Enter id",
         validators=[DataRequired(),Length(min=3,max=10)]
    )
    first_name = StringField(
        "Enter First name", 
         validators=[DataRequired(),Length(min=1,max=50)]
    )
    last_name = StringField(
        "Enter last name", 
         validators=[DataRequired(),Length(min=1,max=50)]
    )
    mobile_number = StringField(
        "Enter Phone number",
         validators=[DataRequired(),Length(min=11,max=20)]     
    )
    email = StringField(
        "Enter email",
         validators=[DataRequired(),Length(min=1,max=50)]
    )
    institute = StringField(
        "Enter Institute Name",
         validators=[DataRequired(),Length(min=1,max=200)]
    )
    institute_code = IntegerField(
        "Enter institute Code",
         validators=[DataRequired(),Length(min=1,max=20)]
    )
    password = PasswordField(
        "Enter a Strong Pasword",
         validators=[DataRequired(),Length(min=6,max=32)]
    )
    retype_password = PasswordField(
        "Retype password",
         validators=[DataRequired(),Length(min=6,max=32)]
    )