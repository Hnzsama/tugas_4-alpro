# Kumpulan Latihan Dasar Python

Repository ini berisi kumpulan 10 file skrip Python sederhana yang mencakup konsep-konsep dasar pemrograman seperti input/output, percabangan (`if-elif-else`), dan perulangan (`for`, `while`).
Setiap file dirancang untuk menyelesaikan satu tugas spesifik.

## Daftar Skrip

### 1. `tugas_1_cek_bilangan.py`

Program ini meminta pengguna memasukkan sebuah angka bulat, lalu menentukan apakah angka tersebut adalah **positif**, **negatif**, atau **nol**.

### 2. `tugas_2_nilai_huruf.py`

Program ini menentukan **predikat nilai** (A, B, C, D, atau E) berdasarkan rentang skor (0–100) yang diinput oleh pengguna.

### 3. `tugas_3_hari_nomor.py`

Program sederhana untuk mengubah input angka (1–7) menjadi nama hari yang sesuai dalam seminggu (1 untuk Senin, 7 untuk Minggu). Jika input tidak valid, program menampilkan pesan error.

### 4. `tugas_4_deret_angka.py`

Skrip ini menampilkan deret angka dari 1 hingga **N** dengan dua cara: menggunakan **`for` loop** dan **`while` loop**.

### 5. `tugas_5_jumlah_ganjil.py`

Program ini menghitung jumlah semua bilangan **ganjil** dari 1 hingga **N**.
Contoh: jika N = 10 → hasil = 1 + 3 + 5 + 7 + 9 = 25.

### 6. `tugas_6_tabel_perkalian.py`

Program ini akan menampilkan **tabel perkalian** dari 1 hingga 10 untuk sebuah angka yang dimasukkan oleh pengguna.

### 7. `tugas_7_bilangan_prima.py`

Program untuk memeriksa apakah sebuah bilangan yang diinput oleh pengguna termasuk **bilangan prima** atau bukan.

### 8. `tugas_8_segitiga_bintang.py`

Skrip ini mencetak pola **segitiga siku-siku** menggunakan karakter bintang (`*`).
Jumlah baris ditentukan oleh input dari pengguna.
Contoh (N = 5):

```
*
**
***
****
*****
```

### 9. `tugas_9_tebak_angka.py`

Sebuah permainan **tebak angka** sederhana. Angka rahasia ditentukan di awal program.
Pengguna menebak angka tersebut dengan petunjuk: **“Terlalu besar”** atau **“Terlalu kecil”** hingga berhasil menebak dengan benar.

### 10. `tugas_10_login.py`

Skrip ini adalah simulasi sistem login sederhana.

* Username: `admin`
* Password: `1234`
  Pengguna memiliki maksimal 3 kali kesempatan untuk login. Jika benar → tampilkan **“Login berhasil”**, jika salah hingga 3 kali → tampilkan **“Akses ditolak”**.

---

## Cara Menjalankan

Setiap skrip dapat dijalankan secara individual melalui terminal. Pastikan Python sudah terinstal.

```bash
# Contoh untuk menjalankan file cek bilangan
python tugas_1_cek_bilangan.py

# Contoh untuk menjalankan file login
python tugas_10_login.py
```