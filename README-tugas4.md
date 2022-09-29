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

[https://nama-proyek.herokuapp.com/todolist](https://nama-proyek.herokuapp.com/todolist)

[https://nama-proyek.herokuapp.com/todolist/register](https://nama-proyek.herokuapp.com/todolist/register)

[https://nama-proyek.herokuapp.com/todolist/login](https://nama-proyek.herokuapp.com/todolist/login)

[https://nama-proyek.herokuapp.com/todolist/logout](https://nama-proyek.herokuapp.com/todolist/logout)

[https://nama-proyek.herokuapp.com/todolist/create-task](https://nama-proyek.herokuapp.com/todolist/create-task)


## Kegunaan `{% csrf_token %}` pada Elemen `<form>`
Token ini berfungsi sebagai proteksi dari serangan CSRF (Cross Site Request Forgery). Jika kita tidak menggunakan token ini, data-data kita yang tersimpan di sesi kuki bisa saja diambil orang lain.

## Membuat Form Secara Manual
Hal tersebut bisa kita lakukan.
1.  Buat form dengan _tag_ `<form>`.
2.  Buat tabel di dalam form.
3.  Setiap elemen di form kita simpan per baris tabel.

## Proses Alur Data
1.  Pengguna membuat permintaan HTTP 
2.  Peladen menerima permintaan, menentukan fungsi yang perlu dilakukan, dan membuat halaman form HTML
3.  Pengguna menerima halaman form HTML. Pengguna mengirim permintaan HTTP lagi disertai input yang diberikan di form
4.  Input tersebut kita olah. Untuk menyimpannya, kita bisa membuat objek berdasarkan `models` yang sudah kita buat dengan data dari pengguna.
5.  Data yang sudah kita simpan bisa kita tampilkan di halaman HTML.
6.  Peladen mengembalikan halaman HTML yang sudah ditambahkan data baru.

## Cara Implementasi
1.  Membuat aplikasi `todolist`, menambahkannya ke `INSTALLED_APPS` dan menambahkan `path`-nya
2.  Membuat model `Task` di `todolist\models.py`
3.  Membuat `view`, templat HTML, dan `path` untuk `todolist`. Pada pembuatan `view` ditentukan juga `view` yang memerlukan login
4.  Migrate dan coba di `localhost`
5.  Setelah aman, _push_ ke Github
6.  Saat _deployment_, sempat terjadi eror. Saya mengatasinya dengan membuat variabel `COLLECTSTATIC_DISABLE` dan membuat nilainya 1 di Heroku.
7.  _Deployment_ berhasil. Saya mencoba membuat beberapa akun dan _task_.
