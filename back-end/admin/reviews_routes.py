from flask import Blueprint,render_template,redirect,request
from admin.forms import ReviewsForm
from app.models import Reviews
from app import app,db
from werkzeug.utils import secure_filename
import os
reviews_bp=Blueprint('reviews',__name__,static_folder='static',template_folder='templates')

@reviews_bp.route('/admin/reviews/',methods=['GET','POST'])
def reviews():
    form=ReviewsForm()
    t_reviews=Reviews.query.all()
    if request.method=='POST':
        file=form.r_img.data
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        reviews=Reviews(
            r_img=filename,
            r_name=form.r_name.data,
            r_company=form.r_company.data,
            r_icon=form.r_icon.data,
            r_subject=form.r_subject.data
        )
        db.session.add(reviews)
        db.session.commit()
        return redirect('/admin/reviews/')
    return render_template('admin/reviews.html',form=form,t_reviews=t_reviews)

@reviews_bp.route('/reviews/delete/<id>')
def reviews_delete(id):
    silinecekOlanReviews=Reviews.query.get(id)
    db.session.delete(silinecekOlanReviews)
    db.session.commit()
    return redirect('/admin/reviews/')

@reviews_bp.route('/reviews/update/<id>',methods=['GET','POST'])
def reviews_update(id):
    form=ReviewsForm()
    deyisdirilecekOlanReviews=Reviews.query.get(id)
    if request.method=='POST':
        file=form.r_img.data
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        r_img=filename
        r_name=form.r_name.data
        r_company=form.r_company.data
        r_icon=form.r_icon.data
        r_subject=form.r_subject.data
        deyisdirilecekOlanReviews.r_img=r_img
        deyisdirilecekOlanReviews.r_name=r_name
        deyisdirilecekOlanReviews.r_company=r_company
        deyisdirilecekOlanReviews.r_icon=r_icon
        deyisdirilecekOlanReviews.r_subject=r_subject
        db.session.commit()
        return redirect('/admin/reviews/')
    return render_template('admin/reviews_update.html',form=form,reviews=deyisdirilecekOlanReviews)