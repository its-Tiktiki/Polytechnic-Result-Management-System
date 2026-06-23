from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired

class CurriculamForm(FlaskForm):
    department_code = SelectField(
        "Departments",
        choices=[],
        validators=[DataRequired()]
    )

    semester = SelectField(
        "semester",
        choices=[
            ("0","Select"),
            ("1","Semester 1"),
            ("2","Semester 2"),
            ("3","Semester 3"),
            ("4","Semester 4"),
            ("5","Semester 5"),
            ("6","Semester 6"),
            ("7","Semester 7")
        ]
    )

    subject_id = SelectField(
        "Subject",
        choices=[],
        coerce=int
    )

    submit = SubmitField(
        "Assign Subject"
    )

class DepartmentForm(FlaskForm):
    department_code = IntegerField(
        "Department code",
        validators=[DataRequired()]
    )
    department_name = StringField(
        "Department Name",
        validators=[DataRequired()]
    )

    submit = SubmitField("Save Department")
class SubjectForm(FlaskForm):
    subject_code = StringField(
        "Subject Code",
        validators=[DataRequired()]
    )
    subject_name = StringField(
        "Subject Name",
        validators=[DataRequired()]
    )
    submit = SubmitField("Save Subject")


class TeacherAssignmentForm(FlaskForm):
    
    teacher_id = SelectField(
        choices=[]
    )

    department_code = SelectField(
        choices=[]
    )

    semester = SelectField(

        choices=[

            ("1","Semester 1"),
            ("2","Semester 2"),
            ("3","Semester 3"),
            ("4","Semester 4"),
            ("5","Semester 5"),
            ("6","Semester 6"),
            ("7","Semester 7"),
            ("8","Semester 8")
        ]
    )

    subject_id = SelectField(

        choices=[],

        coerce=int
    )

    submit = SubmitField(
        "Assign Teacher"
    )