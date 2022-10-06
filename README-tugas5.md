## Inline, Internal, dan External CSS

### Inline CSS
Inline CSS adalah kode CSS yang disisipkan di tag suatu elemen HTML. Caranya adalah dengan menambahkan attribute `style` pada tag yang ingin diberikan kode CSS dan memberikan value berupa kode CSS. Kelebihan inline CSS adalah meng-_override_ semua kode CSS yang telah dibuat, kecuali yang `!important`. Kekurangan inline CSS adalah menurunkan _readibility_ kode jika kode CSS yang disisipkan terlalu panjang dan kita perlu mengulang kode yang sama jika ingin membuat elemen dengan kode CSS yang sama.

### Internal CSS
Internal CSS adalah kode CSS yang disisipkan di dalam `meta` suatu file HTML. Internal CSS ditandai dengan tag `<style>` yang ada di blok `meta`. Kelebihan internal CSS adalah kita tidak perlu mengulang kode CSS yang telah kita buat untuk suatu elemen, tidak seperti inline CSS. Meskipun demikian, hal tersebut hanya berlaku untuk elemen yang berada di file yang sama saja.

### External CSS
External CSS adalah kode CSS yang berada dalam file tersendiri. Untuk menambahkannya ke HTML, kita bisa menambahkan `link` di `meta` yang merujuk ke file CSS yang telah dibuat. Kelebihannya adalah CSS tersebut bisa digunakan untuk banyak file HTML sehingga kita bisa mendefinisikan satu untuk banyak file. Kekurangannya adalah terkadang kita bisa lupa untuk memasukkan `link` file CSS ke HTML sehingga membuat bingung mengapa CSS yang telah dibuat tidak bekerja.

## Beberapa Tag HTML
1.  `div`, tag yang membuat suatu blok yang bisa diisi elemen html lainnya.
2.  `a`, tag untuk membuat _hyperlink_
3.  `meta`, tag yang berisi metadata dari halaman HTML
4.  `span`, tag untuk mengubah style dari sebagian teks
5.  `form`, untuk membuat suatu form
6.  `table`, membuat tabel

## Beberapa CSS Selector
1.  `element`, memilih elemen tertentu,
2.  `.class-name`, memilih elemen yang memiliki class `class-name`,
3.  `#id`, memilih elemen yang memiliki id `id`,
4.  `*`, memilih semua elemen,
5.  `.class1, .class2, ...`, memilih elemen dengan class `class1`, `class2`, atau class lainnya yang ditambahkan di selector tersebut
6.  `element .class-name`, memilih elemen tertentu dengan class `class-name`

