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


Flask Forms nədir? Necə istifadə olunur?
- Hyper Text Transfer Protocol olan HTTP, serverlerin ve istifadecilerin bir-biri ile nece unsiyyet qurdugunu      
  tesvir eden protocoldur.
  Meselen: Istenilen  brauzere girib her hansi  bir melumati axtardigimizda servere sorgu gonderirik ve server bize bu serverde cavab gonderir.Bu zaman yerine yetirmeli qaydalar HTTP adlanir.

  HTTP methodlari:
  GET,POST,PUT,HEAD,PUT

  GET:
  - GET methodu serverden melumat almaq ucun istifade olunur.
    Meselen:Saytdaki her hansi bir sehifeye daxil olanda bir unvan isteyirik ve bu teleb brauzerde GET metodu ile edilir
  POST:
  - POST methodu servere melumatlar gondermek ucun istifade olunur.POST methodu ile servere limitsiz melumatlar 
    gondere bileriy.POST metodu ilə göndərilən məlumatlar HTTP sorğusunun istək hissəsində saxlanıldığı üçün məlumatlar daha guvenli şəkildə ötürülür.
  
  DELETE:
  - Bir istifadecini id ile silmek ucun istifade olunur.
  
  PUT:
  - PUT bir qaynaq yaratmaq və ya dəyişdirmək üçün istifadə olunur, yəni mövcud deyilsə - yarat, əgər varsa, 
    dəyişdirin.
  - Bir istifadecini update yeni  yeniləmək üçün bu metodu yaradın.
   
Flask layihəsinin folder ve fayl strukturunu necə optimallaşdıra bilərik?

Flask Blueprint nədir? Necə istifadə olunur?
-