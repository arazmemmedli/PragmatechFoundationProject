from flask import Blueprint,render_template,redirect,request
from admin.forms import CodingSkillsForm
from app.models import CodingSkills
from app import app,db
codingskills_bp=Blueprint('codingskills',__name__,static_folder='static',template_folder='templates')

@codingskills_bp.route('/admin/codingskills/',methods=['GET','POST'])
def coding_skills():
    form=CodingSkillsForm()
    codingskills=CodingSkills.query.all()
    if request.method=='POST':
        codingskill=CodingSkills(
            cs_percent=form.cs_percent.data,
            cs_number=form.cs_number.data,
            cs_name=form.cs_name.data,
            cs_subject=form.cs_subject.data
        )
        db.session.add(codingskill)
        db.session.commit()
        return redirect('/admin/codingskills/')
    return render_template('admin/codingskills.html',form=form,codingskills=codingskills)

@codingskills_bp.route('/codingskills/delete/<id>')
def codingskills_delete(id):
    silinecekOlanCodingSkills=CodingSkills.query.get(id)
    db.session.delete(silinecekOlanCodingSkills)
    db.session.commit()
    return redirect('/admin/codingskills/')

@codingskills_bp.route('/codingskills/update/<id>',methods=['GET','POST'])
def codingskills_update(id):
    form=CodingSkillsForm()
    deyisdirilecekOlanCodingSkills=CodingSkills.query.get(id)
    if request.method=='POST':
        cs_percent=form.cs_percent.data
        cs_number=form.cs_number.data
        cs_name=form.cs_name.data
        cs_subject=form.cs_subject.data
        deyisdirilecekOlanCodingSkills.cs_percent=cs_percent
        deyisdirilecekOlanCodingSkills.cs_number=cs_number
        deyisdirilecekOlanCodingSkills.cs_name=cs_name
        deyisdirilecekOlanCodingSkills.cs_subject=cs_subject
        db.session.commit()
        return redirect('/admin/codingskills/')
    return render_template('admin/cs_update.html',form=form,codingskill=deyisdirilecekOlanCodingSkills)
