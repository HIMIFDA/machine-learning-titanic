# Simple Implementation of Machine Learning Using Logistic Regression.


### Pendahuluan
Pada 14 april 1912 di Southampton, kapal titanic menarik jangkarnya dan melakukan ekspedisi pertamanya menuju New York City. Titanic merupakan kapal terbesar yang beroperasi pada masa itu, mengangkut sekitar 2.224 orang. Kapal yang digadang-gadang tidak bisa tenggelam ini sayangnya malah menabrak gunung es pada pukul 23:40. Kapal ini tenggelam dua jam empat puluh menit kemudian pada pukul 02:20 hari Minggu, 15 April (05:18 GMT) dan mengakibatkan kematian lebih dari 1.500 penumpangnya. Tenggelamnya Titanic adalah salah satu bencana maritim masa damai mematikan sepanjang sejarah.

Dari data yang didapat (kita hanya memiliki 1308 data) kita bisa menghitung rata-rata bahwa persentase selamat dari seluruh penumpang hanya sebesar 38% hal ini disebabkan pada saat itu kapal titanic tidak membawa sekoci yang bisa menampung seluruh penumpangnya. Dari 38% persentase selamat itu ternyata semakin tinggi kelasnya maka akan semakin besar persentase selamatnya, kita pun bisa kita bagi lagi menjadi persentase perkelas menjadi:

 - Kelas 1 sebesar 61%
 - Kelas 2 sebesar 42%
 - Kelas 3 sebesar 25%

Sepertinya pada saat kapal mewah ini tenggelam, penumpang dengan jenis kelamin perempuan lebih diprioritaskan untuk dapat dievakuasi. Hal tersebut dibenarkan setelah kita melihat data dan mengkalkulasikan persentasenya, dari persentase selamat perkelas diatas, kita bisa mengkalkulasikan persetase selamat perjeniskelamin  dan mendapatkan hasil:

 - Kelas 1
       Perempuan:  96%
       Laki-laki: 34%
 - Kelas 2
       Perempuan:  88%
       Laki-laki: 14%
 - Kelas 1
      Perempuan:  49%
      Laki-laki: 15%

Beruntunglah mereka yang berusia lebih muda, karna setelah kita melihat dan mengkalkulasikan data lebih dalam lagi, kita mendapatkan kesimpulan bahwa semakin muda umurnya, maka persentase selamatnya akan lebih besar, berikut perhitungan persentase berdasarkan umur kurang dari atau lebih dari 25 tahun:

- Kelas 1
       Perempuan:
	       - Di bawah 25 tahun: 96%
	       - Di atas 25 tahun: 96%
       Laki-laki:
	       - Di bawah 25 tahun: 36%
	       - Di atas 25 tahun: 33%
- Kelas 2
       Perempuan:
	       - Di bawah 25 tahun: 93%
	       - Di atas 25 tahun: 86%
       Laki-laki:
	       - Di bawah 25 tahun: 36%
	       - Di atas 25 tahun: 7%
- Kelas 1
      Perempuan:
	       - Di bawah 25 tahun: 52%
	       - Di atas 25 tahun: 44%
       Laki-laki:
	       - Di bawah 25 tahun: 14%
	       - Di atas 25 tahun: 15%
   

### Machine Learning
*Machine learning* merupakan subset dari *artificial intelligence*, *machine learning* merupakan teknik mengintruksikan komputer untuk bertindak tanpa perlu di program secara eksplisit.  Atau, penjelasan lebih detailnya seperti ini:

    Sebuah program komputer dikatakan belajar dari pengalaman E yang berhubungan dengan tugas T dan mengukur kinerja P jika kinerjanya pada T, yang diukur dengan P, ditingkatkan dengan pengalaman E. Misalkan kita makan algoritma pembelajaran banyak data historis. 
    Dalam contoh kasus titanic, apa P, T dan E?
    
    Answer
    P = kemungkinan selamat penumpang titanic.
    T = menghitung probabilitas keselamatan penumpang titanic.
    E = algoritme untuk menghitung probabilitas berdasarkan datasets.

Dengan *machine learning* kita bisa membuat komputer membuat keputusan berdasarkan data-data yang kita berikan, data-data tersebut akan diproses berdasarkan algoritme tertentu yang pada akhirnya akan mengeluarkan sebuah *output*/hipotesa. Masalah-masalah yang sebelumnya terlihat mustahil untuk dipecahkan, sekarang sudah mulai bisa dipecahkan dengan *machine learning*. dalam dekade terakhir, *machine learning* telah memberi kita *self-driving car*([Tesla Autopilot Self-Driving Car](https://www.youtube.com/watch?v=PUw_DMaQ264&t=12s)), *search engine* ([RankBrain](https://en.wikipedia.org/wiki/RankBrain)), image recognition([Facebbook's Image Recognition](http://www.theverge.com/2016/8/25/12630850/facebook-fair-deepmask-sharpmask-ai-image-recognition)) dan masih banyak lagi.

### Project
Pada project ini, kita akan menghitung probabilitas keselamatan penumpan titanic berdasarkan kelas, umur, dan jenis kelamin. Teknik yang digunakan adalah teknik [*supervised learning*](https://en.wikipedia.org/wiki/Supervised_learning), kita akan melakukan klasifikasi terhadap data-data yang kita punya sehingga bisa mengeluarkan *output* label apakah penumpang tersebut akan selamat atau tidak.

Kita menggunakan 3 fitur(x1, x2, x3) untuk membuat hipotesa:

 1. Kelas
 2. Umur
 3. Jenis kelamin

Algoritme yang digunakan adalah [*softmax regression*](http://www.kdnuggets.com/2016/07/softmax-regression-related-logistic-regression.html).

Kita menggunakan Python sebagai bahasa pemrogrammannya dan menggunakan beberapa *tools* diantaranya:

 - [TensorFlow](https://tensorflow.org)
 - [Sci-kit](http://scikit-learn.org/)
 - [Numpy](http://www.numpy.org/)
 - [Pandas](http://pandas.pydata.org/)

### Instalasi
Pastikan kalian menggunakan Python3 di komputer kalian dan pastikan kalian juga sudah menginstall pip3 di komputer kalian.

Pertama, jalankan setup.sh
    
    > ./setup.sh

- Kita menjanlankan setup.sh untuk menginstall segala depedencies yang dibutuhkan.
- Setelah semua depedencies dibutuhkan kita akan melatih model kita
- Setelah model kita selesai dilatih kita akan menyimpan model kita pada folder /model

Setelah melewati tahap pertama, kita sudah bisa menjalankan aplikasi kita

    > python3 main.py

   
Buka browser kalian dan akses http://0.0.0.0:5000

### Kontributor
- [Andrea Damayanti](https://www.facebook.com/Chedhit.4ever?fref=ts)
- [Pramesti Hatta K.](https://facebook.com/opam22)
- [Trianto Fajar](https://www.facebook.com/insinyur.sth?fref=ts)
- [Windi Triyani](https://www.facebook.com/windy.triyani?fref=ts)

### License
© 2017 Himpunan Mahasiswa Informatika Unsada

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
