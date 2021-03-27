from flask import Blueprint,render_template,redirect,request
from app.models import Contact
from app import app,db

contact_bp=Blueprint('contact',__name__,static_folder='static',template_folder='templates')
@contact_bp.route('/admin/contact/')
def contact():
    t_contacts=Contact.query.all()
    return render_template('admin/contact.html',t_contacts=t_contacts)