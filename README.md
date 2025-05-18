# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000. Perusahaan ini memiliki lebih dari 1.000 karyawan yang tersebar di seluruh negara. Meskipun merupakan perusahaan yang cukup besar, Jaya Jaya Maju masih menghadapi tantangan dalam mengelola tenaga kerjanya. Hal ini menyebabkan tingkat perputaran karyawan yang tinggi (rasio karyawan yang keluar dibandingkan dengan jumlah total karyawan), yang mencapai lebih dari 10%.

Untuk mencegah masalah ini semakin memburuk, manajer departemen HR meminta bantuan Anda untuk mengidentifikasi faktor-faktor kunci yang berkontribusi terhadap tingginya tingkat perputaran karyawan. Selain itu, mereka juga meminta Anda untuk membuat sebuah dasbor bisnis guna membantu memantau faktor-faktor ini secara efektif. Perusahaan juga telah menyediakan dataset yang dapat Anda unduh melalui tautan berikut: Jaya Jaya Maju.

### Permasalahan Bisnis

Jaya Jaya Maju menghadapi tingkat perputaran karyawan lebih dari 10%, yang memengaruhi stabilitas operasional dan efisiensi perusahaan. Departemen HR memerlukan analisis komprehensif untuk memahami faktor-faktor yang berkontribusi terhadap perputaran karyawan, serta sebuah dasbor untuk memantau metrik utama yang terkait dengan tenaga kerja.

### Cakupan Proyek

- Membersihkan dataset yang digunakan untuk analisis.
- Mengidentifikasi variabel yang paling berpengaruh terhadap perputaran karyawan.
- Membangun model prediktif untuk perputaran karyawan menggunakan teknik pembelajaran mesin.
- Memberikan rekomendasi strategis berdasarkan hasil analisis.
- Membangun dasbor visualisasi untuk memantau faktor risiko perputaran karyawan.

### Persiapan

Sumber data: Dataset internal HR dari Jaya Jaya Maju, yang mencakup informasi demografis, peran pekerjaan, kepuasan kerja, dan status perputaran karyawan (apakah karyawan tersebut telah keluar atau tidak).

Setup environment:

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:

1. Clone Repository

```
git clone
cd nama-repo
```

2. Install Dependencies

```
pipenv install
```

3. Activate/Enable Virtual Environment

```
pipenv shell
```

4. Run the App

```
streamlit run app.py
```

Akses Dashboard Metabase
Untuk mengakses dasbor HR, login ke Metabase dengan akun berikut:

```
Email: adityayogoal33@gmail.com
Password: @KaiHavertz29
```

Atau alternatif default:

```
Email: root@mail.com
Password: root123
```

## Business Dashboard

Business Dashboard
Business dashboard dirancang untuk membantu manajer HR dan eksekutif memantau faktor-faktor kunci yang berkontribusi terhadap perputaran karyawan. Dashboard ini dibangun menggunakan Metabase, dan mencakup berbagai visualisasi seperti:

- Rata-rata Gaji Bulanan berdasarkan Status Attrition dan Work-Life Balance
- Distribusi Karyawan berdasarkan Status Attrition
- Perbandingan Tingkat Attrition berdasarkan Bidang Pendidikan
- Dampak Jarak Tempuh terhadap Tingkat Keluar Karyawan
- Tingkat Attrition berdasarkan Kelompok Usia
- Attrition berdasarkan Status Pernikahan

🔗 Link Dashboard:

## Menjalankan Sistem Machine Learning

Sistem machine learning dikembangkan untuk memprediksi kemungkinan seorang karyawan akan keluar dari perusahaan (attrition) berdasarkan berbagai fitur seperti usia, jarak ke tempat kerja, tingkat pendidikan, keterlibatan kerja, dan kompensasi.

Model yang digunakan adalah XGBoost Classifier, dipilih karena performa akurasi yang tinggi setelah dibandingkan dengan model lain seperti Logistic Regression dan Random Forest. Model ini sudah disimpan dalam format .joblib agar dapat di-load kembali saat digunakan di aplikasi.

Untuk menjalankan prototipe sistem:

1. Buka halaman Prediksi Streamlit.
2. Masukkan informasi karyawan pada form input di bagian "Prediksi Attrition".
3. Klik Prediksi untuk melihat hasilnya:
   - Apakah karyawan berpotensi resign
   - Probabilitasnya dalam bentuk persentase

🔗 Link Prototipe: https://hr-analytics-attrition-dicoding.streamlit.app/

## Conclusion

Dengan pendekatan berbasis data, proyek ini memberikan:

- Model akurat untuk memprediksi potensi keluar karyawan
- Dasbor visualisasi untuk monitoring faktor risiko
- Rekomendasi actionable untuk meningkatkan retensi
- Perusahaan kini dapat mengambil keputusan strategis secara lebih cepat dan tepat berdasarkan data.

### Rekomendasi Action Items

Kompensasi dan Keseimbangan Hidup
Meskipun rata-rata gaji bulanan lebih tinggi pada karyawan yang keluar, hal ini menunjukkan bahwa faktor non-finansial seperti lingkungan kerja, peluang pengembangan karier, dan keseimbangan kerja-hidup perlu menjadi fokus utama untuk meningkatkan retensi. Perusahaan direkomendasikan untuk:

- Perbaiki Lingkungan Kerja untuk menciptakan budaya kerja yang positif, suportif, dan kolaboratif agar karyawan merasa nyaman dan termotivasi

Data menunjukkan bahwa karyawan yang masih single dan berusia lebih muda memiliki kecenderungan lebih tinggi untuk resign. Hal ini bisa disebabkan oleh faktor seperti pencarian pengalaman baru, mobilitas yang lebih tinggi, atau belum memiliki ikatan keluarga yang kuat sehingga lebih fleksibel mengambil keputusan untuk pindah kerja. Perusahaan direkomendasikan untuk:

- Kembangkan Program Pengembangan Karier dan Pelatihan
- Berikan Insentif yang Relevan
