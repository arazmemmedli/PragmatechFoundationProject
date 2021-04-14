from flask import Blueprint,render_template,redirect,request,flash,url_for
from app.models import BlogCategory,BlogPost,Comment
from app import app,db
web_blog_bp=Blueprint('web_blog',__name__,static_folder='static',template_folder='templates',static_url_path='web/static',url_prefix='/blog')

@web_blog_bp.route('/')
def index_blog():
    blogs=BlogPost.query.all()
    return render_template('web/blog.html',blogs=blogs)

@web_blog_bp.route('/detail/<id>')
def blog_single(id):
    blog=BlogPost.query.get(id)
    b_categories=BlogCategory.query.all()
    c_blog=BlogPost.query.filter_by(id=id).first()
    comments=Comment.query.filter_by(blogpost_id=c_blog.id)
    relatedposts=BlogPost.query.filter(BlogPost.id != id, BlogPost.blogcategory_id == blog.blogcategory_id).all()  
    return render_template('web/single.html',blog=blog,b_categories=b_categories,comments=comments,relatedposts=relatedposts)

@web_blog_bp.route('/tag/design/')
def tag_design():
    d_blogs=BlogPost.query.all()
    return render_template('web/tag_design.html',d_blogs=d_blogs)

@web_blog_bp.route('/tag/html/')
def tag_html():
    h_blogs=BlogPost.query.all()
    return render_template('web/tag_html.html',h_blogs=h_blogs)

@web_blog_bp.route('/detail/<id>',methods=['GET','POST'])
def blog_comment(id):
    if request.method == 'POST':
        blogcomment=Comment(
            com_name=request.form['com_name'],
            com_email=request.form['com_email'],
            comment=request.form['comment'],
            blogpost_id=id
        )
        db.session.add(blogcomment)
        db.session.commit()
        return redirect(url_for('web_blog.blog_single',id=id))
    return render_template('web/single.html')

@web_blog_bp.route('/detail/delete/<id>')
def comment_delete(id):
    silinecekOlanComment=Comment.query.get(id)
    db.session.delete(silinecekOlanComment)
    db.session.commit()
    return redirect(url_for('web_blog.blog_single'),id=id)

@web_blog_bp.route('/category/design/')
def category_design():
    category=BlogPost.query.filter_by(blogcategory_id='Design').all()
    return render_template('web/category_design.html',category=category)

@web_blog_bp.route('/category/music/')
def category_music():
    m_categories=BlogPost.query.filter_by(blogcategory_id='Music').all()
    return render_template('web/category_music.html',m_categories=m_categories)

@web_blog_bp.route('/category/uncategorized/')
def category_uncategorized():
    u_categories=BlogPost.query.filter_by(blogcategory_id='Uncategorized').all()
    return render_template('web/category_uncategorized.html',u_categories=u_categories)


@web_blog_bp.route('/category/wordpress/')
def category_wordpress():
    w_categories=BlogPost.query.filter_by(blogcategory_id='WordPress').all()
    return render_template('web/category_wordpress.html',w_categories=w_categories)
        
        