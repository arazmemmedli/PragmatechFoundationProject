from flask import Blueprint,render_template,redirect,request
from admin.forms import EducationForm
from app.models import Education
from app import app,db
education_bp=Blueprint('education',__name__,static_folder='static',template_folder='templates')

@education_bp.route('/admin/education/',methods=['GET','POST'])
def admin_education():
    form=EducationForm()
    educations=Education.query.all()
    if request.method=='POST':
        education=Education(
            ed_date=form.ed_date.data,
            ed_name=form.ed_name.data,
            ed_subject=form.ed_subject.data
        )
        db.session.add(education)
        db.session.commit()
        return redirect('/admin/education/')
    return render_template('admin/education.html',form=form,educations=educations)

@education_bp.route('/education/delete/<id>')
def education_delete(id):
    silinecekOlanEducation=Education.query.get(id)
    db.session.delete(silinecekOlanEducation)
    db.session.commit()
    return redirect('/admin/education/')

@education_bp.route('/education/update/<id>')
def education_update(id):
    form=EducationForm()
    deyisdirilecekOlanEducation=Education.query.get(id)
    if request.method=='POST':
        ed_date=form.ed_date.data
        ed_name=form.ed_name.data
        ed_subject=form.ed_subject.data
        deyisdirilecekOlanEducation.ed_date=ed_date
        deyisdirilecekOlanEducation.ed_name=ed_name
        deyisdirilecekOlanEducation.ed_subject=ed_subject
        db.session.commit()
        return redirect('/admin/education/')
    return render_template('admin/ed_update.html',form=form,education=deyisdirilecekOlanEducation)
