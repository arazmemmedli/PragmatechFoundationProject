from flask import Blueprint,render_template,redirect,request
from admin.forms import LanguageSkillsForm
from app.models import LanguageSkills
from app import app,db
languageskills_bp=Blueprint('languageskills',__name__,static_folder='static',template_folder='templates')

@languageskills_bp.route('/admin/languageskills/',methods=['GET','POST'])
def language_skills():
    form=LanguageSkillsForm()
    languageskills=LanguageSkills.query.all()
    if request.method=='POST':
        languageskill=LanguageSkills(
            ls_name=form.ls_name.data,
            ls_subject=form.ls_subject.data,
            ls_percent=form.ls_percent.data
        )
        db.session.add(languageskill)
        db.session.commit()
        return redirect('/admin/languageskills/')
    return render_template('admin/languageskills.html',form=form,languageskills=languageskills)

@languageskills_bp.route('/languageskills/delete/<id>')
def languageskills_delete(id):
    silinecekOlanLanguageSkills=LanguageSkills.query.get(id)
    db.session.delete(silinecekOlanLanguageSkills)
    db.session.commit()
    return redirect('/admin/languageskills/')

@languageskills_bp.route('/languageskills/update/<id>',methods=['GET','POST'])
def languageskills_update(id):
    form=LanguageSkillsForm()
    deyisdirilecekOlanLanguageSkills=LanguageSkills.query.get(id)
    if request.method=='POST':
        ls_name=form.ls_name.data
        ls_subject=form.ls_subject.data
        ls_percent=form.ls_percent.data
        deyisdirilecekOlanLanguageSkills.ls_name=ls_name
        deyisdirilecekOlanLanguageSkills.ls_subject=ls_subject
        deyisdirilecekOlanLanguageSkills.ls_percent=ls_percent
        db.session.commit()
        return redirect('/admin/languageskills/')
    return render_template('admin/ls_update.html',form=form,languageskill=deyisdirilecekOlanLanguageSkills)