from flask_wtf import FlaskForm
from wtforms import SelectField,IntegerField,StringField,SubmitField
from wtforms.validators import DataRequired

class AddStudentForm(FlaskForm):
    student_roll = IntegerField(
        "Student Roll",
        validators=[DataRequired()]
    )
    student_reg_number = IntegerField(
        "Registration Number",
        validators=[DataRequired()]
    )
    