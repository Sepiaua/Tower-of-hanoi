# Tower-of-hanoi
Proyek ini merupakan visualisasi dari algoritma Tower of Hanoi menggunakan pendekatan Depth-First Search (DFS). Dibuat dengan Python dan antarmuka grafis Tkinter, program ini menunjukkan langkah-langkah pemindahan cakram dari tiang A ke tiang C secara visual dan interaktif.

Fitur:
Visualisasi animasi langkah demi langkah dari solusi Tower of Hanoi.
Menggunakan algoritma rekursif DFS.
Tiga cakram berwarna (merah, putih, hijau) sebagai representasi dari ukuran cakram.
Output terminal yang menunjukkan urutan perpindahan cakram.

Teknologi:
Python 3
Tkinter untuk GUI
Rekursi (Depth-First Search)

Cara Menjalankan:
Pastikan Python sudah terinstall, kemudian jalankan:
python hanota.py

Tampilan:
Layar akan menampilkan tiga tiang dengan cakram yang berpindah satu per satu mengikuti aturan Tower of Hanoi.
Setiap langkah akan ditampilkan juga di terminal.

Algoritma:
Tower of Hanoi diselesaikan menggunakan pendekatan DFS:
Pindahkan n-1 cakram ke tiang bantu.
Pindahkan cakram terbesar ke tiang tujuan.
Pindahkan kembali n-1 cakram dari tiang bantu ke tiang tujuan.

Struktur File:
hanota.py: Skrip utama yang berisi logika DFS dan visualisasi Tkinter.

Catatan:
Saat ini menggunakan 3 cakram secara default. Untuk cakram lebih banyak, perlu penyesuaian ukuran dan posisi pada GUI.
Waktu delay antar langkah adalah 0.5 detik.

