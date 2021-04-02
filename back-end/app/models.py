from app import db
from app import migrate
class AboutMe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a_subject = db.Column(db.Text)
    a_age = db.Column(db.Integer)
    a_freelance = db.Column(db.String(50))
    a_phone = db.Column(db.String(40))
    a_residence = db.Column(db.String(70))
    a_address = db.Column(db.String(80))
    a_e_mail= db.Column(db.String(80))

class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    s_icon = db.Column(db.String(70))
    s_name = db.Column(db.String(60))
    s_subject = db.Column(db.String(200))

class Pricing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p_icon=db.Column(db.String(70))
    p_name=db.Column(db.String(60))
    p_number=db.Column(db.Integer)

class PricingCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p_title=db.Column(db.String(200))

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    e_date = db.Column(db.String(100))
    e_name = db.Column(db.String(160))
    e_subject = db.Column(db.String(250))

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ed_date = db.Column(db.String(100))
    ed_name = db.Column(db.String(160))
    ed_subject = db.Column(db.String(250))

class DesignSkills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ds_name = db.Column(db.String(120))
    ds_subject = db.Column(db.String(250))
    ds_percent = db.Column(db.String(70))
    ds_number = db.Column(db.String(70))

class LanguageSkills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ls_name = db.Column(db.String(120))
    ls_subject = db.Column(db.String(250))
    ls_percent = db.Column(db.String(70))

class CodingSkills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cs_percent = db.Column(db.String(70))
    cs_number = db.Column(db.String(70))
    cs_name = db.Column(db.String(120))
    cs_subject = db.Column(db.String(250))

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    r_img = db.Column(db.String(200))
    r_name = db.Column(db.String(140))
    r_company = db.Column(db.String(150))
    r_icon = db.Column(db.String(100))
    r_subject = db.Column(db.String(255))

class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c_img = db.Column(db.String(200))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(140))
    email = db.Column(db.String(140))
    message = db.Column(db.Text)

class PortfolioCategory(db.Model):
    __tablename__='portfolio_category'
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(100))
    posts = db.relationship('Portfolio', backref='portfolio_category')

class PortfolioImages(db.Model):
    __tablename__='portfolio_images'
    id = db.Column(db.Integer, primary_key=True)
    p_img = db.Column(db.String(200))
    p_posts = db.relationship('Portfolio', backref='portfolio_images')

class Portfolio(db.Model):
    __tablename__='portfolio'
    id = db.Column(db.Integer, primary_key=True)
    p_title = db.Column(db.String(140))
    p_icon = db.Column(db.String(70))
    data_modal = db.Column(db.String(100))
    portfoliocategory_name=db.Column(db.String(100), db.ForeignKey('portfolio_category.cat_name'), nullable=False)
    portfolioimages_name=db.Column(db.String(200), db.ForeignKey('portfolio_images.p_img'), nullable=False)














