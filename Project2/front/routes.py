from flask import Blueprint,render_template,redirect,request,url_for

front_bp=Blueprint('front',__name__,template_folder='templates',static_folder='static',static_url_path='/front/static')

@front_bp.route('/')
def index():
    from run import db,AboutMe
    Abouts=AboutMe.query.all()
    return render_template('front/index.html',Abouts=Abouts)
