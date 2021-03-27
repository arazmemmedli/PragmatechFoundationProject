# admin / routes.py
from flask import Blueprint,render_template,redirect,request

admin_bp=Blueprint('admin',__name__,static_folder='static',template_folder='templates',url_prefix='/admin')

@admin_bp.route('/')
def admin_index():
    return render_template('admin/index.html')


