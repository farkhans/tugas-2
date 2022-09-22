Farkhan Syawal Harahap

2106709125

PBP F

***

## Link Heroku
[nama-proyek.herokuapp.com](https://nama-proyek.herokuapp.com/)

[nama-proyek.herokuapp.com/katalog](https://nama-proyek.herokuapp.com/katalog)

[nama-proyek.herokuapp.com/mywatchlist/html](https://nama-proyek.herokuapp.com/mywatchlist/html)

[nama-proyek.herokuapp.com/mywatchlist/xml](https://nama-proyek.herokuapp.com/mywatchlist/xml)

[nama-proyek.herokuapp.com/mywatchlist/json](https://nama-proyek.herokuapp.com/mywatchlist/json)

## Perbedaan JSON, HTML, dan XML

### JSON

JSON (JavaScript Object Notation) adalah sebuah format untuk menyimpan dan melakukan pertukaran data. Sesuai dengan namanya, data dalam format JSON akan disimpan dalam bentuk objek JavaScript. Data-data ini disimpan dalam bentuk pasangan _key and value_ sehingga kita bisa memanggil nilai atribut suatu objek menggunakan _key_ yang sesuai. _Key_ pada JSON sendiri bentuknya adalah sebuah string, dan _value_-nya bisa bermacam-macam, seperti integer, string, bahkan object. Setiap _key_ dan _value_ dipisahkan oleh tanda titik dua (:) dan antara _key_ dan _value_ sebelum dan sesudahnya dipisah oleh tanda koma (,).

### XML
XML (Extensible Markup Language) juga merupakan sebuah format yang dapat digunakan untuk menyimpan dan menukarkan data. 

## Mengapa Diperlukan _Data Delivery_ dalam Pengimplementasian Platform
Dalam membuat platform, terkadang kita perlu memerlukan data. Misalkan kita ingin menampilkan halaman utama akun media sosial. Di sana bisa ditemukan foto profil, nama, dan hal lainnya yang berkaitan dengan pengguna. Untuk menampilkannya, diperlukan data-data pengguna. Di sinilah kita memerlukan _data delivery_. 

## Cara Implementasi
1.  Membuat aplikasi `mywatchlist` dengan _command_ `python manage.py startapp wishlist`
2.  Menambahkan `mywatchlist` ke variabel `INSTALLED_APPS` di file `settings.py` pada folder `project-django`
3.  Menambahkan `path` untuk `mywatchlist` di `urls.py` milik `project-django`
4.  Membuka `models.py` di folder `mywatchlist` dan membuat model sesuai permintaan
5.  Membuat `fixtures/initial_mywatchlist_data.json` untuk `mywatchlist`
6.  Membuat beberapa fungsi untuk mengolah _request_ di `views.py` milik `mywatchlist`
7.  Pada `mywatchlist/urls.py`, buat beberapa _routing_ sesuai permintaan
8.  Membuat templat `html` untuk `mywatchlist`
9.  Migrasi data dengan _command_ `python manage.py makemigrations` lalu `python manage.py migrate`
10.  Muat data JSON `mywatchlist` dengan _command_ `python manage.py loaddata initial_mywatchlist_data.json`
11.  Coba jalankan di `localhost` dengan _command_ `python manage.py runserver`
12.  Setelah semuanya lancar, buat _test_ pada `mywatchlist/tests.py`
13.  Membuat `css/style.css` di folder `staticfiles` lalu jalankan `python manage.py collectstatic` agar `ValueError` teratasi
14.  Ketika _test_ aman, ubah isi `Procfile`. Baris pertama diubah menjadi `release: sh -c 'python manage.py migrate && python manage.py loaddata */fixtures/*.json'`. Hal ini bertujuan agar saat _deployment_ semua data inisiasi langsung dimuat
15.  Setelah semuanya siap, semua perubahan dan tambahan di-_push_ ke Github dan langsung di-_deploy_ secara otomatis
