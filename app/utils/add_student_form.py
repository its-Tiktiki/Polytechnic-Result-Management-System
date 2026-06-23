from flask_wtf import FlaskForm
from wtforms import SelectField,IntegerField,StringField,SubmitField,DateTimeField
from wtforms.validators import DataRequired

class AddStudentForm(FlaskForm):
    student_roll = IntegerField(
        "Student Roll",
        validators=[DataRequired()]
    )
    student_full_name = StringField(
        "Student Full Name",
        validators=[DataRequired()]
    )
    semester = SelectField(
        "Select Semester",
        choices=[
            ("1","Semester 1"),
            ("2","Semester 2"),
            ("3","Semester 3"),
            ("4","Semester 4"),
            ("5","Semester 5"),
            ("6","Semester 6"),
            ("7","Semester 7"),
        ]
    )
    group = SelectField(
        "If exit. Select group",
        choices=[
            ("None"),
            ("A"),
            ("B")
        ]
    )
    submit = SubmitField("Add Student")


    