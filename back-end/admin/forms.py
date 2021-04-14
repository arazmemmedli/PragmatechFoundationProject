from flask_wtf import FlaskForm
from wtforms import StringField,FileField,IntegerField,SubmitField,TextAreaField,SelectField,DateTimeField
from app import db
from app.models import Portfolio,PortfolioCategory,PortfolioImages
from app.models import BlogPost,BlogCategory

PortfolioCategoryList=[]
PortfolioImagesList=[]
for c_obj in PortfolioCategory.query.all():
    PortfolioCategoryList.append(
        (c_obj.cat_name)
    )

for i_obj in PortfolioImages.query.all():
    PortfolioImagesList.append(
        (i_obj.p_img)
    )

BlogCategoryList=[]
for obj in BlogCategory.query.all():
    BlogCategoryList.append(
        (obj.name)
    )
class AboutForm(FlaskForm):
    a_subject=TextAreaField('a_subject')
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
    s_subject=TextAreaField('s_subject')
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
    e_subject=TextAreaField('e_subject')
    e_submit=SubmitField()

class EducationForm(FlaskForm):
    ed_date=StringField('ed_date')
    ed_name=StringField('ed_name')
    ed_subject=TextAreaField('ed_subject')
    ed_submit=SubmitField()

class DesignSkillsForm(FlaskForm):
    ds_name=StringField('ds_name')
    ds_subject=TextAreaField('ds_subject')
    ds_percent=StringField('ds_percent')
    ds_number=StringField('ds_number')
    ds_submit=SubmitField()

class LanguageSkillsForm(FlaskForm):
    ls_name=StringField('ls_name')
    ls_subject=TextAreaField('ls_subject')
    ls_percent=StringField('ls_percent')
    ls_submit=SubmitField()

class CodingSkillsForm(FlaskForm):
    cs_percent=StringField('cs_percent')
    cs_number=StringField('cs_number')
    cs_name=StringField('cs_name')
    cs_subject=TextAreaField('cs_subject')
    cs_submit=SubmitField()

class ReviewsForm(FlaskForm):
    r_img=FileField('r_img')
    r_name=StringField('r_name')
    r_company=StringField('r_company')
    r_icon=StringField('r_icon')
    r_subject=TextAreaField('r_subject')
    r_submit=SubmitField()

class ClientsForm(FlaskForm):
    c_img=FileField('c_img')
    c_submit=SubmitField()

class ContactForm(FlaskForm):
    fullname=StringField('fullname')
    email=StringField('email')
    message=TextAreaField('message')

class PortfolioCategoryForm(FlaskForm):
    cat_name=StringField('cat_name')
    cat_submit=SubmitField()

class PortfolioImagesForm(FlaskForm):
    p_img=FileField('p_img')
    p_submit=SubmitField()

class PortfolioForm(FlaskForm):
    p_title=StringField('p_title')
    p_icon=StringField('p_icon')
    data_modal=StringField('data_modal')
    portfoliocategory_name=SelectField('portfoliocategory_name',choices=PortfolioCategoryList)
    portfolioimages_name=SelectField('portfolioimages_name',choices=PortfolioImagesList)
    port_submit=SubmitField()

class BlogForm(FlaskForm):
    blog_img=FileField('blog_img')
    blog_date=StringField('blog_date')
    blog_title=StringField('blog_title')
    short_info=TextAreaField('short_info')
    content=TextAreaField('content')
    blog_url=StringField('blog_url')
    blogcategory_id=SelectField('blogcategory_id',choices=BlogCategoryList)
    blog_submit=SubmitField()

class BlogCategoryForm(FlaskForm):
    name=StringField('name')
    submit=SubmitField()

class PortfolioModalForm(FlaskForm):
    m_data_modal=StringField('m_data_modal')
    portfolimodalimages_name=SelectField('portfolimodalimages_name',choices=PortfolioImagesList)
    m_submit=SubmitField()