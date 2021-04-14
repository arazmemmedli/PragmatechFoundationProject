# app / __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
upload_folder='admin/static/uploads'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/data.db'
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['UPLOAD_PATH']=upload_folder
db=SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import AboutMe
from app.models import Services
from app.models import Pricing
from app.models import Experience
from app.models import Education
from app.models import DesignSkills
from app.models import LanguageSkills
from app.models import CodingSkills
from app.models import Reviews
from app.models import Clients
from app.models import Contact
from app.models import Portfolio,PortfolioCategory,PortfolioImages,PortfolioModal
from app.models import BlogCategory,BlogPost,Comment



from admin.routes import admin_bp
from web.routes import web_bp
from admin.a_routes import about_bp
from admin.s_routes import services_bp
from admin.p_routes import pricing_bp
from admin.experience_routes import experience_bp
from admin.education_routes import education_bp
from admin.ds_routes import designskills_bp
from admin.ls_routes import languageskills_bp
from admin.cs_routes import codingskills_bp
from admin.reviews_routes import reviews_bp
from admin.clients_routes import clients_bp
from admin.portfolio_routes import portfolio_bp
from web.blogroutes import web_blog_bp
from admin.blog_routes import admin_blog_bp

app.register_blueprint(admin_bp)
app.register_blueprint(web_bp)
app.register_blueprint(about_bp)
app.register_blueprint(services_bp)
app.register_blueprint(pricing_bp)
app.register_blueprint(experience_bp)
app.register_blueprint(education_bp)
app.register_blueprint(designskills_bp)
app.register_blueprint(languageskills_bp)
app.register_blueprint(codingskills_bp)
app.register_blueprint(reviews_bp)
app.register_blueprint(clients_bp)
app.register_blueprint(portfolio_bp)
app.register_blueprint(web_blog_bp)
app.register_blueprint(admin_blog_bp)
