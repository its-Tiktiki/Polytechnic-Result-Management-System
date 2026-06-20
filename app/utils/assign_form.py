from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired

class CurriculamForm(FlaskForm):
    department_id = SelectField(
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
            ("7","Semester 7"),
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


class AssignTeacherForm(FlaskForm): # Fixed spelling here
    teacher_id = SelectField(
        "Select teacher",
        choices=[],
        coerce=int,
        validators=[DataRequired()]
    )
    department_id = SelectField(
        "Select Department",
        choices=[],
        coerce=int,
        validators=[DataRequired()]
    )
    semester = SelectField(
        "Semester",
        coerce=int,
        choices=[
            (1, "Semester 1"), (2, "Semester 2"), (3, "Semester 3"),
            (4, "Semester 4"), (5, "Semester 5"), (6, "Semester 6"),
            (7, "Semester 7")
        ],
        validators=[DataRequired()]
    )
    
    # CRITICAL FIX: Set validate_choice=False because JS populates this dynamically.
    # Otherwise, WTForms will block the submission thinking it's an invalid choice.
    subject_id = SelectField(
        "Subject",
        choices=[],
        coerce=int,
        validate_choice=False
    )
    
    submit = SubmitField("Assign Teacher")