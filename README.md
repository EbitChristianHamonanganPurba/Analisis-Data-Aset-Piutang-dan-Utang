# Analisis-Data-Aset-Piutang-dan-Utang

Berikut ini contoh data yang saya gunakan untuk dianalisis:

![image](https://github.com/EbitChristianHamonanganPurba/Analisis-Data-Aset-Piutang-dan-Utang/assets/167233970/882b9fbb-f275-43ee-9a28-410ae065b92b)

Langkah 2 : Membuat Visualisasi 

Setelah memperoleh data diatas, dilanjutkan membuat visualisasi data menggunakan Python. Visualisasi data yang saya tampilkan terdiri dari histogram, box & whisker, bar chart, dan pie chart, 

Langkah 3 : Analisis Statistik

Untuk analisis statistik keterkaitan antara data-data ini, kita dapat menggunakan berbagai teknik seperti analisis regresi, dan uji hipotesis.

Langkah 4 : Visualisasi Keterkaitan Data 

![image](https://github.com/EbitChristianHamonanganPurba/Analisis-Data-Aset-Piutang-dan-Utang/assets/167233970/1742bb03-265f-4015-bcd6-31a1b498fb76)
![image](https://github.com/EbitChristianHamonanganPurba/Analisis-Data-Aset-Piutang-dan-Utang/assets/167233970/eb31b2b7-a255-43f1-90eb-b5b53ecb2aed)
![image](https://github.com/EbitChristianHamonanganPurba/Analisis-Data-Aset-Piutang-dan-Utang/assets/167233970/470391e9-a39e-432a-b550-24de2242e908)
![image](https://github.com/EbitChristianHamonanganPurba/Analisis-Data-Aset-Piutang-dan-Utang/assets/167233970/b1238f1e-7e08-49de-8353-658c33a80bdb)
![image](https://github.com/EbitChristianHamonanganPurba/Analisis-Data-Aset-Piutang-dan-Utang/assets/167233970/5f8c7e47-2c63-4d82-b13f-feb731c55ac1)



Berikut ini interpretasi dari setiap analisis yang saya lakukan : 

1. Historgram Nilai Aset
   
   - Distribusi Nilai Aset :

     Dari histogram ini, kita dapat melihat apakah distribusi nilai aset normal, miring ke kiri (skewed left), atau miring ke kanan (skewed right). Jika distribusi terlihat normal, ini berarti sebagian besar nilai aset berada di sekitar rata-rata (mean) dengan sedikit yang berada jauh dari rata-rata. Jika distribusi miring, ini mungkin menunjukkan adanya aset yang sangat tinggi atau sangat rendah dibandingkan dengan mayoritas.

   - Keputusan Manajemen:
   
     Manajemen mungkin perlu meninjau kembali aset yang sangat tinggi atau rendah untuk memastikan tidak ada risiko signifikan atau untuk menemukan peluang investasi yang lebih baik.

2. Boxplot Nilai Aset Berdasarkan Jenis
   
   - Variabilitas dan Outliers:

     Rentang interkuartil (IQR) yang besar pada boxplot menunjukkan bahwa nilai aset sangat bervariasi dalam jenis tersebut. Kehadiran outliers menunjukkan adanya aset dengan nilai yang sangat tinggi atau sangat rendah dalam kategori tertentu. Misalnya, jika jenis aset 'Properti' memiliki banyak outliers, mungkin ada properti tertentu yang nilainya jauh melebihi atau di bawah rata-rata.
     
   - Strategi Pengelolaan Aset:
   
     Mengetahui jenis aset yang memiliki variabilitas tinggi dapat membantu manajemen dalam pengambilan keputusan terkait alokasi dan diversifikasi aset.


3. ANALISIS PIUTANG
   
   Grafik Countplot
   
   - Fokus Pengelolaan:
   
     Jika jenis piutang 'Kredit Konsumen' mendominasi, ini menjadi area fokus untuk pengelolaan piutang, karena jenis ini mungkin menjadi kontributor utama pada total piutang. Strategi pengumpulan dan mitigasi risiko dapat difokuskan pada jenis piutang ini.

   Pie chart
   
   - Efisiensi Pengelolaan Piutang:
   
     Jika sebagian besar piutang berada dalam status 'Belum Jatuh Tempo', ini menunjukkan manajemen piutang yang efisien. Sebaliknya, jika banyak piutang yang berada dalam status 'Terlambat', ini mengindikasikan perlunya perbaikan dalam proses pengumpulan piutang atau penilaian risiko kredit yang lebih baik.

4. ANALISIS UTANG
   
   Countplot
   
   - Kesehatan Finansial:
   
     Dominasi utang dengan status 'Aktif' mungkin menunjukkan perusahaan mampu mengelola kewajibannya dengan baik. Namun, banyaknya utang dengan status 'Tertunda' dapat menunjukkan masalah likuiditas atau kesulitan dalam memenuhi kewajiban finansial.

   Boxplot Nilai Utang Berdasarkan Jenis
   
   - Variabilitas Nilai Utang:

     Variabilitas nilai utang yang besar dalam satu jenis mungkin menunjukkan risiko yang lebih tinggi yang terkait dengan jenis utang tersebut. Misalnya, jika 'Utang Bank' memiliki variabilitas tinggi, ini mungkin menandakan ketergantungan pada pinjaman bank yang bisa berdampak pada stabilitas keuangan perusahaan.
   
   - Strategi Pengelolaan Utang:

     Mengetahui jenis utang dengan variabilitas tinggi dapat membantu dalam merencanakan strategi pengelolaan utang yang lebih efektif.

5. ANALISIS REGRESI

   - Koefisien:
   
     Menunjukkan pengaruh masing-masing variabel independen terhadap variabel dependen.
     
   - P-value:
   
     Jika p-value kurang dari 0.05, koefisien tersebut signifikan secara statistik. Artinya, variabel independen memiliki pengaruh signifikan terhadap variabel dependen.
     
   - R-squared:
     
     Mengukur seberapa baik model menjelaskan variabilitas data. R-squared yang lebih tinggi menunjukkan model yang lebih baik.
     
   - Durbin-Watson:

      Digunakan untuk mendeteksi adanya autokorelasi di residual (error) dari model regresi.
     

6. UJI HIPOTESIS

   Uji hipotesis, seperti uji t atau uji ANOVA, dapat digunakan untuk membandingkan rata-rata antar kelompok.

   - Perbedaan Signifikan:
   
     Jika p-value kurang dari tingkat signifikansi (misalnya 0.05), kita menolak hipotesis nol dan menyimpulkan bahwa ada perbedaan signifikan antara rata-rata nilai aset dari kedua jenis aset tersebut. Ini mungkin menunjukkan bahwa satu jenis aset lebih bernilai daripada yang lain, yang dapat mempengaruhi keputusan investasi atau strategi pengelolaan aset.

   - T-statistic:
   
     Menunjukkan seberapa besar perbedaan antara rata-rata dua kelompok.

 
