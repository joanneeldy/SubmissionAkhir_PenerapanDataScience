# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

By: Joanne Landy Tantreece - Cohort Laskar AI

## Business Understanding

**Jaya Jaya Institut** merupakan sebuah institusi pendidikan tinggi fiktif yang telah berdiri sejak tahun 2000. Dengan reputasi yang sangat baik, institut ini telah berhasil mencetak banyak lulusan berkualitas. Namun, di balik kesuksesannya, Jaya Jaya Institut menghadapi sebuah tantangan besar yang dapat memengaruhi reputasi dan keberlanjutan operasionalnya di masa depan.

### Permasalahan Bisnis

Permasalahan utama yang dihadapi oleh Jaya Jaya Institut adalah **tingkat _dropout_ mahasiswa yang cukup tinggi**. Banyaknya mahasiswa yang tidak menyelesaikan pendidikannya menjadi perhatian serius bagi manajemen. Tingkat _dropout_ yang tinggi tidak hanya berdampak pada citra dan akreditasi institut, tetapi juga pada efisiensi sumber daya dan pendapatan.

Oleh karena itu, pihak manajemen ingin dapat **mengidentifikasi mahasiswa yang berpotensi _dropout_ sedini mungkin**. Dengan deteksi dini, institut dapat memberikan bimbingan khusus, program pendampingan, atau bantuan lain yang diperlukan untuk membantu mahasiswa tersebut tetap berada di jalur kelulusan dan pada akhirnya menekan angka _dropout_.

### Cakupan Proyek

Proyek ini bertujuan untuk membangun sebuah sistem komprehensif untuk membantu Jaya Jaya Institut dalam mengatasi permasalahan _dropout_. Cakupan dari proyek ini meliputi:

1.  **Analisis Data Eksploratif (EDA):** Melakukan analisis mendalam pada data historis performa mahasiswa untuk menemukan faktor-faktor kunci yang paling signifikan dalam memengaruhi status kelulusan atau _dropout_.
2.  **Pengembangan Model Machine Learning:** Membuat model klasifikasi yang mampu memprediksi probabilitas seorang mahasiswa akan _dropout_ berdasarkan data akademis dan demografis mereka.
3.  **Pembuatan Dashboard Bisnis:** Merancang dan membangun dashboard interaktif yang memungkinkan pihak manajemen untuk memantau metrik-metrik penting terkait performa mahasiswa secara visual dan mudah dipahami.
4.  **Pengembangan Prototipe Aplikasi Web:** Mengimplementasikan model machine learning ke dalam sebuah aplikasi web prototipe yang ramah pengguna, sehingga dapat digunakan oleh staf akademik untuk melakukan prediksi pada kasus per kasus.

### Persiapan

Dataset yang digunakan dalam proyek ini adalah **"Predict students' dropout and academic success"** yang bersumber dari UCI Machine Learning Repository dan disediakan oleh Dicoding melalui tautan [ini](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance).

Setup environment:
Untuk menjalankan proyek ini secara lokal, Anda memerlukan beberapa library Python. Instal semua dependensi yang dibutuhkan dengan menjalankan perintah berikut di terminal:

```bash
pip install -r requirements.txt
```

## Business Dashboard

Sebuah dashboard bisnis interaktif telah dibuat menggunakan **Looker Studio** untuk memberikan gambaran umum (high-level overview) mengenai performa mahasiswa di Jaya Jaya Institut. Dashboard ini dirancang untuk digunakan oleh level manajerial guna memantau tren dan mengidentifikasi area yang memerlukan perhatian khusus.

Fitur utama dari dashboard ini meliputi:

- KPI Utama: Kartu skor yang menampilkan metrik penting seperti Total Mahasiswa, Tingkat Dropout (%), Jumlah Lulus, dan Jumlah Dropout.
- Analisis Faktor Kunci: Visualisasi yang menunjukkan bagaimana faktor-faktor seperti status kelunasan SPP dan status beasiswa memengaruhi hasil akhir mahasiswa.
- Performa per Jurusan: Tabel detail yang mengurutkan program studi berdasarkan tingkat dropout tertinggi, memungkinkan identifikasi jurusan yang paling berisiko.
- Filter Interaktif: Kemampuan untuk memfilter seluruh data di dashboard berdasarkan program stu di tertentu.

Dashboard ini dapat diakses secara publik melalui link berikut:

**Link Dashboard** : https://lookerstudio.google.com/reporting/f7cfb32a-20d1-4c02-9af5-fe00bcbf90e5

## Menjalankan Sistem Machine Learning

Sebagai solusi prediktif, sebuah prototipe sistem machine learning telah dikembangkan dalam bentuk aplikasi web menggunakan Streamlit. Aplikasi ini memungkinkan staf akademik (seperti dosen wali atau bagian kemahasiswaan) untuk memasukkan data seorang mahasiswa dan secara instan mendapatkan prediksi apakah mahasiswa tersebut berisiko dropout atau tidak, lengkap dengan tingkat probabilitasnya.

Aplikasi ini sudah di-deploy ke cloud dan dapat diakses oleh siapa saja. Untuk menjalankan aplikasi ini secara lokal di komputer Anda, gunakan perintah berikut di terminal:

```
streamlit run app.py
```

Aplikasi web prototipe ini dapat diakses secara publik melalui link berikut:

**Link Aplikasi**: https://joanneeldy-submissionpds2.streamlit.app/

## Conclusion

Proyek ini berhasil menjawab permasalahan bisnis yang dihadapi oleh Jaya Jaya Institut. Berdasarkan analisis data, ditemukan bahwa faktor-faktor seperti **status kelunasan SPP** (`Tuition_fees_up_to_date`) dan **jumlah SKS yang diluluskan pada semester awal** merupakan prediktor terkuat terhadap potensi dropout seorang mahasiswa.

Model **Logistic Regression** terpilih sebagai model klasifikasi terbaik karena menunjukkan performa yang unggul dalam metrik yang paling krusial, yaitu **Recall untuk kelas 'Dropout' sebesar 93%**. Ini berarti model sangat andal dalam menangkap sebagian besar kasus mahasiswa yang sebenarnya berisiko dropout, sehingga meminimalkan jumlah kasus yang terlewatkan.

Kombinasi antara **dashboard analitik** untuk pemantauan strategis dan **aplikasi prediktif** untuk aksi taktis memberikan solusi yang komprehensif dan berbasis data bagi Jaya Jaya Institut untuk menekan angka dropout secara efektif.

### Rekomendasi Action Items

Berdasarkan hasil analisis dan model yang telah dikembangkan, berikut adalah beberapa rekomendasi tindakan yang dapat segera diimplementasikan oleh Jaya Jaya Institut:

- **Action Item 1: Implementasi Sistem Peringatan Dini Keuangan.**
  Mengingat status kelunasan SPP adalah faktor paling signifikan, direkomendasikan untuk membuat sistem proaktif yang secara otomatis mengidentifikasi dan menghubungi mahasiswa yang SPP-nya belum lunas di pertengahan semester. Pendekatan ini bisa berupa penawaran konseling keuangan, informasi beasiswa, atau opsi pembayaran yang lebih fleksibel.

- **Action Item 2: Program Pendampingan Akademik Berbasis Performa.**
  Jumlah SKS yang lulus di semester 1 dan 2 terbukti sangat krusial. Institut sebaiknya mewajibkan sesi pendampingan intensif dengan Dosen Pembimbing Akademik bagi setiap mahasiswa yang jumlah SKS lulusnya berada di bawah ambang batas tertentu (misalnya, kurang dari 80% dari total SKS yang diambil).

- **Action Item 3: Pemanfaatan Aplikasi Prediktif oleh Staf Akademik.**
  Mendorong penggunaan aplikasi web prediktif yang telah dibuat oleh Dosen Pembimbing Akademik di awal setiap semester. Dengan memasukkan data mahasiswa bimbingannya, dosen dapat mengidentifikasi siapa saja yang memiliki probabilitas dropout tinggi dan perlu mendapatkan perhatian serta intervensi lebih awal, bahkan sebelum nilai akhir semester keluar.

```

```
