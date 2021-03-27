from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from front.routes import front_bp
from admin.routes import admin_bp
from admin.a_routes import about_bp

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
class AboutMe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a_subject = db.Column(db.Text)
    a_age = db.Column(db.Integer)
    a_freelance = db.Column(db.String(50))
    a_phone = db.Column(db.String(40))
    a_residence = db.Column(db.String(70))
    a_address = db.Column(db.String(80))
    a_e_mail= db.Column(db.String(80))
 
app.register_blueprint(front_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(about_bp)

if __name__=='__main__':
    app.run(debug=True)