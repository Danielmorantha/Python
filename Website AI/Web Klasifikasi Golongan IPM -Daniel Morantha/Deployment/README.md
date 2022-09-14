# Deployment Model Regresi Linier

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment model Machine DecisionTreeClassifier. Adapun model yang digunakan merupakan model untuk mengklasifikasi IPM berdasarkan:

	Harapan_Lama_Sekolah	Pengeluaran_Perkapita	Rerata_Lama_Sekolah	Usia_Harapan_Hidup

-   `Harapan_Lama_Sekolah` dengan tipe data float (bilangan Desimal)
-   `Pengeluaran_Perkapita` dengan tipe data integer
-   `Rerata_Lama_Sekolah` dengan tipe data float
-   `Usia_Harapan_Hidup` dengan tipe data float


#

## Sekilas mengenai input model

Agar dapat mengklasifikasi IPM, data input model harus mengikuti format sebagai berikut:\
`[Harapan_Lama_Sekolah	Pengeluaran_Perkapita	Rerata_Lama_Sekolah	Usia_Harapan_Hidup]`

Sebagai contoh:\
Harapan_Lama_Sekolah: 14.36\
Pengeluaran_Perkapita: 9572\
Rerata_Lama_Sekolah: 9.37\
Usia_Harapan_Hidup: 69.96

#

## Folder, file, dan kegunaannya

-   templates/
    -   index.html --> Berisi template website
-   app.py --> Berisi konfigurasi route untuk API
-   model-DT-DanielMorantha.pkl --> Model decision tree yang sudah di-training
-   request.py --> Berisi percobaan pemanggilan API dengan payload data JSON
-   requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model decision tree

#

## Cara menjalankan API pada komputer Anda

### Menjalankan API

1. Pastikan Anda sudah menginstall Anaconda
1. Buka terminal/command prompt/power shell
1. Buat virtual environment dengan\
   `conda create -n <nama-environment> python=3.9`
1. Aktifkan virtual environment dengan\
   `conda activate <nama-environment>`
1. Install semua dependency/package Python dengan\
   `pip install -r requirements.txt`
1. Jalankan API menggunakan perintah\
   `python app.py`

### Akses melalui Website

Setelah API berjalan:

1. Anda akan diberikan URL untuk membuka website berupa `localhost:5000/` atau `127.0.0.1:5000/`
1. Buka URL dengan browser, coba masukkan data yang ingin di prediksi
1. Anda akan diberikan estimasi biaya asuransi pada sisi kanan halaman website

### Mencoba Akses API menggunakan payload JSON

Setelah API berjalan:

1. Buka terminal/comand prompt/power shell
1. Jalankan perintah `python request.py`
1. Hasil klasifikasi IPM terdapat pada value dari key `'prediction_text'` yang dapat Anda manfaatkan untuk aplikasi lain.
