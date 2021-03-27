from flask import Blueprint,render_template,redirect,request,url_for

admin_bp=Blueprint('admin',__name__,template_folder='templates',static_folder='static',static_url_path='/admin/static',url_prefix='/admin')

@admin_bp.route('/')
def a_index():
    return render_template('admin/index.html')
