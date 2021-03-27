from flask import Blueprint,render_template,redirect,request
from admin.forms import ExperienceForm
from app.models import Experience
from app import app,db
experience_bp=Blueprint('experience',__name__,static_folder='static',template_folder='templates')

@experience_bp.route('/admin/experience/',methods=['GET','POST'])
def experience():
    form=ExperienceForm()
    experiences=Experience.query.all()
    if request.method=='POST':
        experience=Experience(
            e_date=form.e_date.data,
            e_name=form.e_name.data,
            e_subject=form.e_subject.data
        )
        db.session.add(experience)
        db.session.commit()
        return redirect('/admin/experience/')
    return render_template('admin/experience.html',form=form,experiences=experiences)

@experience_bp.route('/experience/delete/<id>')
def experience_delete(id):
    silinecekOlanExperience=Experience.query.get(id)
    db.session.delete(silinecekOlanExperience)
    db.session.commit()
    return redirect('/admin/experience/')

@experience_bp.route('/experience/update/<id>',methods=['GET','POST'])
def experience_update(id):
    form=ExperienceForm()
    deyisdirilecekOlanExperience=Experience.query.get(id)
    if request.method=='POST':
        e_date=form.e_date.data
        e_name=form.e_name.data
        e_subject=form.e_subject.data
        deyisdirilecekOlanExperience.e_date=e_date
        deyisdirilecekOlanExperience.e_name=e_name
        deyisdirilecekOlanExperience.e_subject=e_subject
        db.session.commit()
        return redirect('/admin/experience/')
    return render_template('admin/ex_update.html',form=form,experience=deyisdirilecekOlanExperience)


