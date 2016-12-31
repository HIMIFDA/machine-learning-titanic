# Simple implementation of machine learning using softmax regression.


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
   
