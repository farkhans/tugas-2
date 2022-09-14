Farkhan Syawal Harahap

2106709125

PBP F

***

## Link Heroku
[nama-proyek.herokuapp.com](https://nama-proyek.herokuapp.com/)

[nama-proyek.herokuapp.com/katalog](https://nama-proyek.herokuapp.com/katalog)

## Bagan _Request_ Aplikasi Berbasis Django
![alt text](https://github.com/farkhans/tugas-2/blob/main/django-architecture.png "Bagan Request Aplikasi Berbasis Django")

[Sumber gambar](https://data-flair.training/blogs/wp-content/uploads/sites/2/2019/03/Django-Architecture-Diagram.jpg)

Saat kita mengakses sebuah aplikasi berbasis Django, sebuah `http request` akan dikirim ke `URLconf` (`urls.py` di folder proyek Django). _Request_ tersebut akan dicari di `urlpatterns` dan mengembalikan _response_ yang sesuai. _Response_ tersebut bisa saja mengembalikan sebuah _template_ atau mengarah ke URL _configurations_ aplikasi lainnya. Sebelum mengembalikan sebuah _template_, aplikasi Django akan melihat `views` yang sesuai terlebih dahulu, `views` ini sesuai dengan pengembalian dari URL _configurations_ dari `urls.py`. Melalui `views`, Django akan menerima _request_ dan mengembalikan _response_, biasanya berupa halaman `html`. Apabila kita memerlukan data untuk ditampilkan di halaman `html`, Django akan meminta bantuan `models` untuk menyediakan data yang diperlukan. Saat datanya sudah didapat, `views` akan me-_render_ _template_ disertai data-data yang diperlukan. Setelah itu, hasil _render_ tadi dikembalikan sehingga kita bisa melihat halaman yang kita inginkan.

## _Virtual Environtment_
Dalam mengerjakan proyek Django, kita disarankan untuk menggunakan _virtual environtment_. Namun, mengapa harus menggunakan _virtual environtment_? Apakah tidak bisa sekadar instal saja?

Pada dasarnya, kita bisa saja langsung menginstal Django tanpa harus menggunakan _virtual environtment_. Namun, hal ini tidak disarankan untuk dilakukan. Tanpa _virtual environtment_, apa pun yang kita instal di satu proyek akan berlaku juga untuk proyek lainnya. Sekarang, misalkan kita punya beberapa proyek dengan _requirements_ yang berbeda. Katakanlah setiap proyek itu menggunakan _library_ yang sama, tetapi memerlukan versi yang berbeda. Tanpa _virtual environtment_, kita tidak bisa melakukan hal itu. Namun, dengan _virtual environtment_, kita bisa melakukan hal yang demikian. _Virtual environtment_ membatasi hal-hal yang kita lakukan untuk suatu proyek agar terbatas pada proyek itu saja. Misalkan kita punya proyek A yang memerlukan _library_ C versi 1 dan proyek B yang memerlukan _library_ C versi 2. Dengan _virtual environtment_ kita bisa menginstal _library_ yang sesuai untuk masing-masing proyek, tanpa harus mengganggu proyek lainnya.

## Cara Implementasi
Pada dasarnya, hal yang saya lakukan sama seperti hal yang telah dijelaskan pada Tutorial 0 dan 1.
1. Saya memastikan bahwa `katalog` sudah masuk ke `INSTALLED_APPS` yang ada di `settings.py`.
2. Saya mengonfigurasikan `views.py` pada direktori `katalog`. Saya membuat fungsi `katalog` yang akan me-_render_ `request`, `katalog.html`, dan data-data yang diperlukan. Data itu sendiri didapat dari `models.py` serta beberapa data tambahan seperti `nama` dan `id`. Data-data tersebut disimpan dalam suatu `dictionary` bernama `context` sehingga masing-masing data memiliki pasangan `key`-nya. Saya juga sempat memeriksa `models.py` untuk melihat model yang dibuat.
3. Saya mengonfigurasikan _routing_ di `urls.py` pada direktori `katalog`. _Routing_ `urls.py` di direktori `project_django` juga saya konfigurasikan, di sini saya hanya menambahkan `katalog` ke dalam `urlpatterns`.
4. Saya membuka `katalog.html`. Di sini saya memformat beberapa bagian sesuai dengan data di `context`. Untuk tabel, saya menggunakan _loop_ terhadap daftar item. Saya juga sempat melihat `initial_catalog_data.json` untuk melihat item-item yang dibuat. Saya juga memasukkan data-data tersebut ke _database_ lokal dengan menggunakan _command_ `python manage.py loaddata initial_catalog_data.json`.
5. Setelah semuanya selesai, saya menjalankan perintah `python manage.py makemigrations`, `python manage.py migrate`, dan `python manage.py runserver` untuk membuat migrasi model dan mencoba menjalankannya di server lokal.
6. Setelah semua berjalan lancar, saya `push` ke github saya.
7. Saatnya men-_deploy_. Saya membuka _Heroku_ dan menyalin API _key_ saya. Setelah itu, saya membuat _repository secret_ yang berisi API _key_ saya dan nama proyek saya di _Heroku_ agar proyek ini bisa dijalankan di _Heroku_. Saya menjalankan _job_ di github. _Voila_, proyek berhasil di-_deploy_.
