from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'
db = SQLAlchemy(app)

class AboutMe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a_subject = db.Column(db.String(250))
    a_age = db.Column(db.Integer)
    a_freelance = db.Column(db.String(50))
    a_phone = db.Column(db.String(40))
    a_residence = db.Column(db.String(70))
    a_address = db.Column(db.String(80))
    a_e_mail= db.Column(db.String(80))
    
    def save(self):
        db.session.add(self)
        db.session.commit()

# main index 
@app.route('/')
def index():
    Abouts=AboutMe.query.all()
    return render_template('app/index.html',Abouts=Abouts)

# admin index
@app.route('/admin')
def admin():
    return render_template('admin/index.html')

# about index
@app.route('/admin/about')
def about():
    abouts=AboutMe.query.all()
    return render_template('admin/about.html',abouts=abouts)

# add about index
@app.route('/admin/about/add',methods=['GET','POST'])
def add_about():
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
        about.save()
        # db.session.add(about)
        # db.session.commit()
        return redirect('/admin/about')
    return render_template('admin/add_about.html')

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
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
    return render_template('admin/update.html',about=deyisdirilecekOlanAbout)

@app.route('/delete/<id>')
def delete(id):
    silinecekOlanAbout=AboutMe.query.get(id)
    db.session.delete(silinecekOlanAbout)
    db.session.commit()
    return redirect('/admin/about')
if __name__=='__main__':
    app.run(debug=True)