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


## Pemrograman Sinkronus dan Asinkronus
Pada pemrograman sinkronus, program kita dieksekusi secara sekuensial (antrian eksekusi program). Jadi, jika ada suatu pekerjaan yang belum diselesaikan dan ada pekerjaan baru, pekerjaan baru tersebut harus menunggu hingga pekerjaan lama selesai. Sementara itu, pada pemrograman asinkronus program bisa dieksekusi secara paralel. jadi, apabila ada tugas yang belum diselesaikan dan ada tugas baru, tugas baru itu bisa dikerjakan tanpa harus menunggu tugas lama selesai.

## _Event-Driven Programming_
_Event-driven programming_ adalah sebuah paradigma pemrograman yang alur programnya ditentukan oleh _event_ yang dilakukan pengguna seperti mengklik suatu tombol dan menekan tombol di papan tik. Paradigma pemrograman seperti ini biasanya diterapkan di aplikasi berbasis GUI atau di sebuah halaman web. Pada tugas kali ini, paradigma ini diterapkan pada saat membuat _task_. Saat pengguna membuat _task_, program merespons dengan memberikan form untuk mengisi _task_ dan setelah menekan tombol kirim, objek task baru dibuat dan ditampilkan.

## Pemrograman Asinkronus pada AJAX
Pemrograman asinkronus pada AJAX membuat kita bisa tetap mengakses halaman tanpa harus memuat ulang halaman. Dengan ini, kita bisa mengurangi waktu untuk menunggu saat kita melakukan suatu _event_ di halaman. Contohnya apda saat pembuatan _task_, halaman tidak dimuat ulang, tetapi saat kita membuat _task_, _task_ yag kita buat tadi langsung muncul begitu kita selesai membuatnya.

## Cara Implementasi
### GET
Cara yang saya gunakan kurang lebih seperti yang dijelaskan di [halaman Tugas 6](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tugas/tugas-6/). Untuk pengambilan GET, saya mengambil dari JSON yang didapat dari tahap dua, lalu menambahkannya dengan metode `append` dari jQuery.
### POST
1.  Sedikit perubahan agar bisa memunculkan modal dari Bootstrap.
2.  Menambahkan _link_ modal Bootstrap.
3.  Membuat modal dan formnya.
4.  Membuat _view_ yang mengembalikan JSON dan _path_-nya.
5.  Membuat method untuk POST di _script_ dan menghubungkannya dengan _view_ tadi.
6.  Menambahkan _task_ baru ke halaman.
