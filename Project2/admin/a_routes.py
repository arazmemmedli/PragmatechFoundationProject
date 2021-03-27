from flask import Blueprint,render_template,redirect,request,url_for

about_bp=Blueprint('about',__name__,template_folder='templates',static_folder='static',static_url_path='/admin/static',url_prefix='/admin/about')
@about_bp.route('/')
def about_index():
    from run import db,AboutMe
    abouts=AboutMe.query.all()
    return render_template('admin/about.html',abouts=abouts)

@about_bp.route('/add',methods=['GET','POST'])
def add_about():
    from run import db,AboutMe
    if request.method=='POST':
        about=AboutMe(
            a_subject=request.form['a_subject'],
            a_age=request.form['a_age'],
            a_freelance=request.form['a_freelance'],
            a_phone=request.form['a_phone'],
            a_residence=request.form['a_residence'],
            a_address=request.form['a_address'],
            a_e_mail=request.form['a_e_mail']
        )
        db.session.add(about)
        db.session.commit()
        return redirect('/admin/about')
    return render_template('admin/add_about.html')

@about_bp.route('/update/<id>')
def about_update(id):
    from run import db,AboutMe
    deyisdirilecekOlanAbout=AboutMe.query.get(id)
    if request.method=='POST':
        a_subject=request.form['a_subject']
        a_age=request.form['a_age']
        a_freelance=request.form['a_freelance']
        a_phone=request.form['a_phone']
        a_residence=request.form['a_residence']
        a_address=request.form['a_address']
        a_e_mail=request.form['a_e_mail']
        deyisdirilecekOlanAbout.a_subject=a_subject
        deyisdirilecekOlanAbout.a_age=a_age
        deyisdirilecekOlanAbout.a_freelance=a_freelance
        deyisdirilecekOlanAbout.a_phone=a_phone
        deyisdirilecekOlanAbout.a_residence=a_residence
        deyisdirilecekOlanAbout.a_address=a_address
        deyisdirilecekOlanAbout.a_e_mail=a_e_mail
        db.session.commit()
        return redirect('/admin/about')
    return render_template('admin/a_update.html',about=deyisdirilecekOlanAbout)

@about_bp.route('/delete/<id>')
def delete(id):
    from run import db,AboutMe
    silinecekOlanAbout=AboutMe.query.get(id)
    db.session.delete(silinecekOlanAbout)
    db.session.commit()
    return redirect('/admin/about')