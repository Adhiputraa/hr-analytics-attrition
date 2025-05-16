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

## Business Dashboard

Business Dashboard
Business dashboard dirancang untuk membantu manajer HR dan eksekutif memantau faktor-faktor kunci yang berkontribusi terhadap perputaran karyawan. Dashboard ini dibangun menggunakan Metabase, dan mencakup berbagai visualisasi seperti:

- Tingkat attrition secara keseluruhan dan berdasarkan departemen
- Rata-rata kompensasi per jam dan hubungannya dengan jarak rumah
- Distribusi kepuasan kerja dan keterlibatan karyawan
- Faktor-faktor teratas yang memengaruhi prediksi keluar atau bertahannya karyawan

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

Proyek ini berhasil mengidentifikasi dan memodelkan faktor-faktor kunci yang memengaruhi attrition di perusahaan Jaya Jaya Maju. Dengan menggunakan pendekatan data-driven, perusahaan kini dapat:

- Memprediksi risiko keluarnya karyawan dengan cukup akurat
- faktor penyebab seperti ketidakseimbangan kompensasi, kurangnya karir yang jelas, dan kepuasan kerja rendah
- Menggunakan dashboard interaktif untuk memantau metrik-metrik HR secara real-time
- Dengan alat dan insight ini, diharapkan perusahaan bisa meningkatkan retensi karyawan dan mengurangi biaya akibat tingginya turnover.

### Rekomendasi Action Items

Tingkatkan Kompensasi dan Fasilitas
Berdasarkan dashboard, salah satu penyebab utama attrition adalah ketidaksesuaian antara gaji per jam dan jarak rumah ke kantor. Direkomendasikan untuk:

- gaji dengan rata-rata jarak karyawan
- mess, flat, atau subsidi transportasi

Bangun Jalur Karier yang Jelas
Data menunjukkan bahwa karyawan dengan hubungan kerja baik tetap bisa keluar jika tidak melihat prospek jangka panjang. Perusahaan perlu:

- jalur karier yang terstruktur
- Melibatkan karyawan dalam penentuan target jangka panjang

Evaluasi Kinerja dan Feedback Berkala
Keinginan mencari tantangan baru dan miskomunikasi dengan manajemen juga berkontribusi terhadap attrition. Perusahaan perlu:

- Mengadakan evaluasi dan review performa secara rutin
- ruang bagi karyawan untuk menyampaikan aspirasi dan tantangan yang dihadapi
