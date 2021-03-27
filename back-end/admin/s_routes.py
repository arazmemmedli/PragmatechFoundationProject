from flask import Blueprint,render_template,redirect,request
from admin.forms import ServicesForm
from app.models import Services
from app import app,db
services_bp=Blueprint('services',__name__,static_folder='static',template_folder='templates')

@services_bp.route('/admin/services/', methods=['GET','POST'])
def services():
    form=ServicesForm()
    S_Services=Services.query.all()
    if request.method=='POST':
        s_services=Services(
            s_icon=form.s_icon.data,
            s_name=form.s_name.data,
            s_subject=form.s_subject.data
        )
        db.session.add(s_services)
        db.session.commit()
        return redirect('/admin/services/')
    return render_template('admin/services.html',form=form,S_Services=S_Services)

@services_bp.route('/services/delete/<id>')
def services_delete(id):
    silinecekServices=Services.query.get(id)
    db.session.delete(silinecekServices)
    db.session.commit()
    return redirect('/admin/services/')

@services_bp.route('/services/update/<id>',methods=['GET','POST'])
def services_update(id):
    form=ServicesForm()
    deyisdirilecekServices=Services.query.get(id)
    if request.method=='POST':
        s_icon=form.s_icon.data
        s_name=form.s_name.data
        s_subject=form.s_subject.data
        deyisdirilecekServices.s_icon=s_icon
        deyisdirilecekServices.s_name=s_name
        deyisdirilecekServices.s_subject=s_subject
        db.session.commit()
        return redirect('/admin/services/')
    return render_template('admin/s_update.html',form=form,services=deyisdirilecekServices)