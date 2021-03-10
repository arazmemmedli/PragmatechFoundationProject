Jinja template nədir? Necə istifadə olunur?
- Jinja2: Python və Html səhifələri arasında əlaqə yaradmağımıza verən bir template-dir(Şablondur).
  HTML səhifəmizdə {{}} aras;nda yazılmış variable-ları python ilə əlaqələndirə bilərik.
  Nümunə:

  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
      Salam {{ad}} {{soyad}}
  </body>
  </html>

  Burda {{}} arasındakı ad, soyad python kodundan göndərəcəyimiz dəyişən olaraq təyin edirik

  Aşağıda python kodlarına baxaq:
  
  from flask import Flask,render_template

  app=Flask(__name__)

  @app.route('/')
  def index():
    return render_template('index.html',ad='Araz',soyad='Memmedli')

  if __name__=='__main__':
    app.run(debug=True)

  Bu yazdığımız kodları run edəndə '/' url-ə gedəndə html səhifəsinə təyin etdiyimiz ad,soyad Araz,Memmedli olacaqdır

Database migration nədir necə istifadə olunur?

- Database migrations bir çox formada olur. Sadəcə məlumatların bir verilənlər bazasından eyni tipli digər        verilənlər bazasına köçürülməsini əhatə edə bilər: məsələn, bir serverdə yerləşən bir SQLite verilənlər bazasındakı  məlumatları başqa bir serverdəki başqa bir SQLite verilənlər bazasına köçürə bilərsiniz. Bu şəkildə verilənlər bazasında sıfırlanmadan istənilən dəyişikliklər edilir.

Məsələn:

  Web saytin database-nin 1hissəsinin table-in qurub 2ci table-in yaradanda 1ci table-ni silib ikisin bir yerdə işə salmaq lazimdi bunun qarşısın almaq üçün migration köməyimizə çatır.Migration hecbirin silmədən ikisin bir yerdə işə salmağımıza köməy olur