from flask_wtf import FlaskForm
from wtforms import StringField,FileField,IntegerField,SubmitField,TextAreaField

class AboutForm(FlaskForm):
    a_subject=StringField('a_subject')
    a_age=IntegerField('a_age')
    a_freelance=StringField('a_freelance')
    a_phone=StringField('a_phone')
    a_residence=StringField('a_residence')
    a_address=StringField('a_address')
    a_e_mail=StringField('a_e_mail')
    submit=SubmitField()

class ServicesForm(FlaskForm):
    s_icon=StringField('s_icon')
    s_name=StringField('s_name')
    s_subject=StringField('s_subject')
    submit=SubmitField()

class PricingForm(FlaskForm):
    p_icon=StringField('p_icon')
    p_name=StringField('p_name')
    p_number=IntegerField('p_number')
    submit=SubmitField()

class PricingCategoryForm(FlaskForm):
    p_title=StringField('p_title')
    c_submit=SubmitField()

class ExperienceForm(FlaskForm):
    e_date=StringField('e_date')
    e_name=StringField('e_name')
    e_subject=StringField('e_subject')
    e_submit=SubmitField()

class EducationForm(FlaskForm):
    ed_date=StringField('ed_date')
    ed_name=StringField('ed_name')
    ed_subject=StringField('ed_subject')
    ed_submit=SubmitField()

class DesignSkillsForm(FlaskForm):
    ds_name=StringField('ds_name')
    ds_subject=StringField('ds_subject')
    ds_percent=StringField('ds_percent')
    ds_number=StringField('ds_number')
    ds_submit=SubmitField()

class LanguageSkillsForm(FlaskForm):
    ls_name=StringField('ls_name')
    ls_subject=StringField('ls_subject')
    ls_percent=StringField('ls_percent')
    ls_submit=SubmitField()

class CodingSkillsForm(FlaskForm):
    cs_percent=StringField('cs_percent')
    cs_number=StringField('cs_number')
    cs_name=StringField('cs_name')
    cs_subject=StringField('cs_subject')
    cs_submit=SubmitField()

class ReviewsForm(FlaskForm):
    r_img=FileField('r_img')
    r_name=StringField('r_name')
    r_company=StringField('r_company')
    r_icon=StringField('r_icon')
    r_subject=StringField('r_subject')
    r_submit=SubmitField()

class ClientsForm(FlaskForm):
    c_img=FileField('c_img')
    c_submit=SubmitField()

class ContactForm(FlaskForm):
    fullname=StringField('fullname')
    email=StringField('email')
    message=TextAreaField('message')
    

