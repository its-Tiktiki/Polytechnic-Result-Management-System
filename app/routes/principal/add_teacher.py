from flask import Blueprint,request,redirect,url_for,session,render_template,flash
from app.utils.principalForm import AddTecaherForm
from app.models.principal import TeacherAddInfo
from app.extensions import db

add_teacher = Blueprint(
    "add_teacher",
    __name__,
    url_prefix="/add_teacher"
)

@add_teacher.route("/",methods=["GET","POST"])
def add_teachers():

    if not session.get("principal"):
        return redirect(url_for('auth.login'))
    
    add_teacher_form = AddTecaherForm()

    if add_teacher_form.validate_on_submit():

        teacher_id = add_teacher_form.teacher_id.data
        first_name = add_teacher_form.first_name.data
        last_name = add_teacher_form.last_name.data
        institute = add_teacher_form.institute.data
        institute_code = add_teacher_form.institute_code.data
        phone = add_teacher_form.phone.data
        email = add_teacher_form.email.data
        username = add_teacher_form.username.data
        password = add_teacher_form.data
        retype_password = add_teacher_form.retype_password.data

        teacher_data_info = AddTecaherForm(
            teacher_id=teacher_id,
            first_name=first_name,
            last_name=last_name,
            institute=institute,
            institute_code = institute_code,
            phone = phone,
            email=email,
            username=username,
            password=password
        )


        db.session.add(teacher_data_info)
        db.session.commit()

        flash("Teacher add successfully","success")
        return redirect(url_for('principal_dashboard.principal_dashboard'))
    
    return render_template(
        "principal/add_principal.html",
        add_teacher_form=add_teacher_form,
    )







