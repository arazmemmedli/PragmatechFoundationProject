from flask import Blueprint,render_template,redirect,request
from admin.forms import DesignSkillsForm
from app.models import DesignSkills
from app import app,db
designskills_bp=Blueprint('designskills',__name__,static_folder='static',template_folder='templates')

@designskills_bp.route('/admin/designskills/', methods=['GET','POST'])
def design_skills():
    form=DesignSkillsForm()
    designskills=DesignSkills.query.all()
    if request.method=='POST':
        designskill=DesignSkills(
            ds_name=form.ds_name.data,
            ds_subject=form.ds_subject.data,
            ds_percent=form.ds_percent.data,
            ds_number=form.ds_number.data
        )
        db.session.add(designskill)
        db.session.commit()
        return redirect('/admin/designskills/')
    return render_template('admin/designskills.html',form=form,designskills=designskills)

@designskills_bp.route('/designskills/delete/<id>')
def designskills_delete(id):
    silinecekOlanDesignSkills=DesignSkills.query.get(id)
    db.session.delete(silinecekOlanDesignSkills)
    db.session.commit()
    return redirect('/admin/designskills/')

@designskills_bp.route('/designskills/update/<id>',methods=['GET','POST'])
def designskills_update(id):
    form=DesignSkillsForm()
    deyisdirilecekOLanDesignSkills=DesignSkills.query.get(id)
    if request.method=='POST':
        ds_name=form.ds_name.data
        ds_subject=form.ds_subject.data
        ds_percent=form.ds_percent.data
        ds_number=form.ds_number.data
        deyisdirilecekOLanDesignSkills.ds_name=ds_name
        deyisdirilecekOLanDesignSkills.ds_subject=ds_subject
        deyisdirilecekOLanDesignSkills.ds_percent=ds_percent
        deyisdirilecekOLanDesignSkills.ds_number=ds_number
        db.session.commit()
        return redirect('/admin/designskills/')
    return render_template('admin/ds_update.html',form=form,designskill=deyisdirilecekOLanDesignSkills)