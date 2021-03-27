from flask import Blueprint,render_template,redirect,request
from admin.forms import PricingForm
from app.models import Pricing
from admin.forms import PricingCategoryForm
from app.models import PricingCategory
from app import app,db
pricing_bp=Blueprint('pricing',__name__,static_folder='static',template_folder='templates')

@pricing_bp.route('/admin/pricing/',methods=['GET','POST'])
def pricing():
    form=PricingForm()
    pricings=Pricing.query.all()
    p_categories=PricingCategory.query.all()
    if request.method=='POST':
        pricing=Pricing(
            p_icon=form.p_icon.data,
            p_name=form.p_name.data,
            p_number=form.p_number.data
        )
        db.session.add(pricing)
        db.session.commit()
        return redirect('/admin/pricing/')
    return render_template('admin/pricing.html',form=form,pricings=pricings)

@pricing_bp.route('/admin/pricing/category/',methods=['GET','POST'])
def admin_category():
    form=PricingCategoryForm()
    pricingcategories=PricingCategory.query.all()
    if request.method=='POST':
        pricingcategory=PricingCategory(
            p_title=form.p_title.data
        )
        db.session.add(pricingcategory)
        db.session.commit()
        return redirect('/admin/pricing/category/')
    return render_template('admin/pricing_category.html',form=form,pricingcategories=pricingcategories)

@pricing_bp.route('/pricing/delete/<id>')
def pricing_delete(id):
    silinecekOlanPricing=Pricing.query.get(id)
    db.session.delete(silinecekOlanPricing)
    db.session.commit()
    return redirect('/admin/pricing/')

@pricing_bp.route('/pricing/category/delete/<id>')
def pricingcategory_delete(id):
    silinecekOlanPricingCategory=PricingCategory.query.get(id)
    db.session.delete(silinecekOlanPricingCategory)
    db.session.commit()
    return redirect('/admin/pricing/category/')

@pricing_bp.route('/pricing/update/<id>',methods=['GET','POST'])
def pricing_update(id):
    form=PricingForm()
    deyisdirilecekOlanPricing=Pricing.query.get(id)
    if request.method=='POST':
        p_icon=form.p_icon.data
        p_name=form.p_name.data
        p_number=form.p_number.data
        deyisdirilecekOlanPricing.p_icon=p_icon
        deyisdirilecekOlanPricing.p_name=p_name
        deyisdirilecekOlanPricing.p_number=p_number
        db.session.commit()
        return redirect('/admin/pricing/')
    return render_template('admin/p_update.html',form=form,pricing=deyisdirilecekOlanPricing)

@pricing_bp.route('/pricing/category/update/<id>')
def pricingcategory_update(id):
    form=PricingCategoryForm()
    deyisdirilecekOlanPricingCategory=PricingCategory.query.get(id)
    if request.method=='POST':
        p_title=form.p_title.data
        deyisdirilecekOlanPricingCategory.p_title=p_title
        db.session.commit()
        return redirect('/admin/pricing/category/')
    return render_template('admin/pricingcategoryupdate.html',form=form,p_category=deyisdirilecekOlanPricingCategory)
