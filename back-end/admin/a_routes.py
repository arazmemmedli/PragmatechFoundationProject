from flask import Blueprint,render_template,redirect,request
from admin.forms import AboutForm
from app.models import AboutMe
from app import app,db
about_bp=Blueprint('about',__name__,static_folder='static',template_folder='templates')

@about_bp.route('/admin/about/',methods=['GET','POST'])
def about():
    form=AboutForm()
    abouts=AboutMe.query.all()
    if request.method=='POST':
        about=AboutMe(
            a_subject=form.a_subject.data,
            a_age=form.a_age.data,
            a_freelance=form.a_freelance.data,
            a_phone=form.a_phone.data,
            a_residence=form.a_residence.data,
            a_address=form.a_address.data,
            a_e_mail=form.a_e_mail.data
        )
        db.session.add(about)
        db.session.commit()
        return redirect('/admin/about/')
    return render_template('admin/about.html',form=form,abouts=abouts)

@about_bp.route('/delete/<id>')
def about_delete(id):
    silinecekOlanAbout=AboutMe.query.get(id)
    db.session.delete(silinecekOlanAbout)
    db.session.commit()
    return redirect('/admin/about/')

@about_bp.route('/update/<id>',methods=['GET','POST'])
def about_update(id):
    form=AboutForm()
    deyisdirilecekAbout=AboutMe.query.get(id)
    if request.method=='POST':
        a_subject=form.a_subject.data
        a_age=form.a_age.data
        a_freelance=form.a_freelance.data
        a_phone=form.a_phone.data
        a_residence=form.a_residence.data
        a_address=form.a_address.data
        a_e_mail=form.a_e_mail.data
        deyisdirilecekAbout.a_subject=a_subject
        deyisdirilecekAbout.a_age=a_age
        deyisdirilecekAbout.a_freelance=a_freelance
        deyisdirilecekAbout.a_phone=a_phone
        deyisdirilecekAbout.a_residence=a_residence
        deyisdirilecekAbout.a_address=a_address
        deyisdirilecekAbout.a_e_mail=a_e_mail
        db.session.commit()
        return redirect('/admin/about/')
    return render_template('admin/a_update.html',form=form,about=deyisdirilecekAbout)