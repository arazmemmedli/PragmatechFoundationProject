from flask import Blueprint,render_template,redirect,request
from admin.forms import ClientsForm
from app.models import Clients
from app import app,db
from werkzeug.utils import secure_filename
import os
clients_bp=Blueprint('clients',__name__,static_folder='static',template_folder='templates')

@clients_bp.route('/admin/clients/',methods=['GET','POST'])
def clients():
    form=ClientsForm()
    t_clients=Clients.query.all()
    if request.method=='POST':
        c_img=form.c_img.data
        filename=secure_filename(c_img.filename)
        c_img.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        clients=Clients(
            c_img=filename
        )
        db.session.add(clients)
        db.session.commit()
        return redirect('/admin/clients/')
    return render_template('admin/clients.html',form=form,t_clients=t_clients)

@clients_bp.route('/clients/delete/<id>')
def clients_delete(id):
    silinecekOlanClients=Clients.query.get(id)
    db.session.delete(silinecekOlanClients)
    db.session.commit()
    return redirect('/admin/clients/')

@clients_bp.route('/clients/update/<id>',methods=['GET','POST'])
def clients_update(id):
    form=ClientsForm()
    deyisdirilecekOlanClients=Clients.query.get(id)
    if request.method=='POST':
        c_img=form.c_img.data
        filename=secure_filename(c_img.filename)
        c_img.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        c_img=filename
        deyisdirilecekOlanClients.c_img=c_img
        db.session.commit()
        return redirect('/admin/clients/')
    return render_template('admin/clients_update.html',form=form,clients=deyisdirilecekOlanClients)