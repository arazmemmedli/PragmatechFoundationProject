from flask import Blueprint,render_template,redirect,request
from admin.forms import PortfolioCategoryForm,PortfolioImagesForm,PortfolioForm
from app.models import Portfolio,PortfolioCategory,PortfolioImages
from app import app,db
from werkzeug.utils import secure_filename
import os
portfolio_bp=Blueprint('portfolio',__name__,static_folder='static',template_folder='templates')

@portfolio_bp.route('/admin/portfolio/',methods=['GET','POST'])
def portfolio():
    portfolioForm=PortfolioForm()
    portfolios=Portfolio.query.all()
    if request.method == 'POST':
        admin_portfolio=Portfolio(
            p_title=portfolioForm.p_title.data,
            p_icon=portfolioForm.p_icon.data,
            data_modal=portfolioForm.data_modal.data,
            portfoliocategory_name=portfolioForm.portfoliocategory_name.data,
            portfolioimages_name=portfolioForm.portfolioimages_name.data
        )
        db.session.add(admin_portfolio)
        db.session.commit()
        return redirect('/admin/portfolio/')
    return render_template('admin/portfolio.html',form=portfolioForm,portfolios=portfolios)

@portfolio_bp.route('/admin/portfolio/category/',methods=['GET','POST'])
def portfolio_category():
    portfolioCategoryForm=PortfolioCategoryForm()
    portfoliocategories=PortfolioCategory.query.all()
    if request.method == 'POST':
        portfolio_category=PortfolioCategory(
            cat_name=portfolioCategoryForm.cat_name.data
        )
        db.session.add(portfolio_category)
        db.session.commit()
        return redirect('/admin/portfolio/category/')
    return render_template('admin/portfolio_category.html',form=portfolioCategoryForm,portfoliocategories=portfoliocategories)

@portfolio_bp.route('/admin/portfolio/images/',methods=['GET','POST'])
def portfolio_images():
    portfolioImagesForm=PortfolioImagesForm()
    t_images=PortfolioImages.query.all()
    if request.method == 'POST':
        p_img=portfolioImagesForm.p_img.data
        filename=secure_filename(p_img.filename)
        p_img.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        portfolio_images=PortfolioImages(
            p_img=filename
        )
        db.session.add(portfolio_images)
        db.session.commit()
        return redirect('/admin/portfolio/images/')
    return render_template('admin/portfolio_images.html',form=portfolioImagesForm,t_images=t_images)

@portfolio_bp.route('/portfolio/update/<id>',methods=['GET','POST'])
def admin_portfolio_update(id):
    portfolioForm=PortfolioForm()
    deyisdirilecekOlanPortfolio=Portfolio.query.get(id)
    if request.method == 'POST':
        p_title=portfolioForm.p_title.data
        p_icon=portfolioForm.p_icon.data
        data_modal=portfolioForm.data_modal.data
        portfoliocategory_name=portfolioForm.portfoliocategory_name.data,
        portfolioimages_name=portfolioForm.portfolioimages_name.data
        deyisdirilecekOlanPortfolio.p_title=p_title
        deyisdirilecekOlanPortfolio.p_icon=p_icon
        deyisdirilecekOlanPortfolio.data_modal=data_modal
        deyisdirilecekOlanPortfolio.portfoliocategory_name=portfoliocategory_name
        deyisdirilecekOlanPortfolio.portfolioimages_name=portfolioimages_name
        db.session.commit()
        return redirect('/admin/portfolio/')
    return render_template('admin/portfolio_update.html',form=portfolioForm,portfolio=deyisdirilecekOlanPortfolio)

@portfolio_bp.route('/portfolio/delete/<id>')
def admin_portfolio_delete(id):
    silinecekOlanPortfolio=Portfolio.query.get(id)
    db.session.delete(silinecekOlanPortfolio)
    db.session.commit()
    return redirect('/admin/portfolio/')

@portfolio_bp.route('/portfolio/category/delete/<id>')
def portfolio_category_delete(id):
    silinecekOlanPortfolioCategory=PortfolioCategory.query.get(id)
    db.session.delete(silinecekOlanPortfolioCategory)
    db.session.commit()
    return redirect('/admin/portfolio/category/')

@portfolio_bp.route('/portfolio/images/delete/<id>')
def portfolio_images_delete(id):
    silinecekOlanPortfolioImages=PortfolioImages.query.get(id)
    db.session.delete(silinecekOlanPortfolioImages)
    db.session.commit()
    return redirect('/admin/portfolio/images/')
    