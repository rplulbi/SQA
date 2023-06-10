# Quality Assurance Roadmap

## Contents
- [Introduction](#introduction)
- [Test Plan Sample](#test-plan-sample)
- [The Road Map](#the-road-map)
- [Advices](#advices)

## Introduction

Pengujian merupakan fase penting dalam setiap siklus hidup produk; apakah itu lini produksi makanan, mobil, atau perangkat lunak, hasilnya harus sesuai dengan yang diharapkan dan memenuhi, memenuhi kebutuhan produk yang kita buat.

Memiliki dasar yang kuat untuk memahami bagaimana komponen perangkat lunak bekerja dan berintegrasi satu sama lain serta memperoleh keterampilan memecahkan berbagai hal adalah keahlian yang penting bagi setiap QA. Pengujian perangkat lunak adalah seni menyelidiki perangkat lunak dan menemukan perilaku yang tidak diinginkan yang mungkin menghasilkan skenario yang tidak diinginkan.

Di bawah ini Anda dapat menemukan jalur untuk QA dan kurva pembelajaran pengujian perangkat lunak yang mungkin Anda perlukan untuk memulai perjalanan.

## Test Plan Sample

Salah satu dokumen terpenting yang harus dibuat oleh tim QA adalah rencana pengujian, karena tim akan bertindak membabi buta tanpa; tidak mengetahui kriteria, titik awal, atau bahkan kapan melakukan jenis pengujian yang berbeda dapat mempertaruhkan keseluruhan pengiriman dan menyebabkan pengiriman kode yang buruk.

Bagian dan konten rencana pengujian dapat bervariasi berdasarkan proyek dan sifat pengiriman, oleh karena itu, PDF rencana pengujian terlampir dianggap sebagai yang umum yang melayani semua tujuan pengiriman pengujian perangkat lunak.

PDF terlampir dapat ditemukan di sini [dokumen test plan](https://github.com/rplulbi/SQA/blob/main/Chapter2/Test_Plan_Sample.pdf) untuk diunduh.

## The Road Map

![QA Engineer Road Map 2022](https://i.imgur.com/cM9cM8T.png)
![QA Engineer Road Map 2022](https://i.imgur.com/meodAKp.png)

## Advices

- Jangan memercayai kode pengujian yang menurut Anda tidak gagal.
- Pahami pengujian perangkat lunak dan jangan langsung masuk ke otomatisasi; secara pribadi, saya mengklasifikasikan otomatisasi sebagai cara yang efisien untuk mengerjakan tugas yang berlebihan. pastikan untuk merancang kriteria pengujian Anda dengan benar dan nanti, Anda dapat mengotomatisasi untuk mencapai yang sebelumnya.
- Otomasi tidak lebih dari mendokumentasikan tes tertulis secara manual dan merekayasanya sedemikian rupa sehingga kode dapat dibaca, dimengerti, dan digunakan kembali.
- Pastikan kode pengujian Anda benar-benar menguji sesuatu.
- Kode pengujian Anda tidak memerlukan pengujian.
- 200~OK tidak selalu oke; Jangan hanya mengandalkan status server saat pengujian, mendapatkan status 200 untuk panggilan API yang tidak sah akan membahayakan keamanan perangkat lunak Anda.

