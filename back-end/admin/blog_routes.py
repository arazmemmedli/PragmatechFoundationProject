from flask import Blueprint,render_template,redirect,request,flash,url_for
from admin.forms import BlogForm,BlogCategoryForm
from app.models import BlogPost,BlogCategory
from app import app,db
from werkzeug.utils import secure_filename
import os

admin_blog_bp=Blueprint('admin_blog',__name__,static_folder='static',template_folder='templates')

@admin_blog_bp.route('/admin/blog/',methods=['GET','POST'])
def admin_blog():
    blogForm=BlogForm()
    t_blogs=BlogPost.query.all()
    if request.method == 'POST':
        blog_img=blogForm.blog_img.data
        filename=secure_filename(blog_img.filename)
        blog_img.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        admin_blogs=BlogPost(
            blog_img=filename,
            blog_date=blogForm.blog_date.data,
            blog_title=blogForm.blog_title.data,
            short_info=blogForm.short_info.data,
            content=blogForm.content.data,
            blog_url=blogForm.blog_url.data,
            blogcategory_id=blogForm.blogcategory_id.data
        )
        db.session.add(admin_blogs)
        db.session.commit()
        return redirect('/admin/blog/')
    return render_template('admin/admin_blog.html',form=blogForm,t_blogs=t_blogs)

@admin_blog_bp.route('/admin/blog/category/',methods=['GET','POST'])
def admin_blog_category():
    blogCategoryForm=BlogCategoryForm()
    t_blogcategories=BlogCategory.query.all()
    if request.method == 'POST':
        blog_category=BlogCategory(
            name=blogCategoryForm.name.data
        )
        db.session.add(blog_category)
        db.session.commit()
        return redirect('/admin/blog/category/')
    return render_template('admin/blog_category.html',form=blogCategoryForm,t_blogcategories=t_blogcategories)

@admin_blog_bp.route('/blog/update/<id>',methods=['GET','POST'])
def admin_blog_update(id):
    blogForm=BlogForm()
    deyisdirilecekOlanAdminBlog=BlogPost.query.get(id)
    if request.method == 'POST':
        blog_img=blogForm.blog_img.data
        filename=secure_filename(blog_img.filename)
        blog_img.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        blog_img=filename
        blog_date=blogForm.blog_date.data
        blog_title=blogForm.blog_title.data
        short_info=blogForm.short_info.data
        content=blogForm.content.data
        blog_url=blogForm.blog_url.data
        blogcategory_id=blogForm.blogcategory_id.data
        deyisdirilecekOlanAdminBlog.blog_img=blog_img
        deyisdirilecekOlanAdminBlog.blog_date=blog_date
        deyisdirilecekOlanAdminBlog.blog_title=blog_title
        deyisdirilecekOlanAdminBlog.short_info=short_info
        deyisdirilecekOlanAdminBlog.content=content
        deyisdirilecekOlanAdminBlog.blog_url=blog_url
        deyisdirilecekOlanAdminBlog.blogcategory_id=blogcategory_id
        db.session.commit()
        return redirect('/admin/blog/')
    return render_template('admin/admin_blog_update.html',form=blogForm,t_blog=deyisdirilecekOlanAdminBlog)

@admin_blog_bp.route('/blog/delete/<id>',methods=['GET','POST'])
def admin_blog_delete(id):
    silinecekOlanAdminBlog=BlogPost.query.get(id)
    db.session.delete(silinecekOlanAdminBlog)
    db.session.commit()
    return redirect('/admin/blog/')





    

