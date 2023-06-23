## driver.get(url)
Fungsi driver.get(url) merujuk pada metode yang digunakan dalam Selenium WebDriver untuk membuka URL yang ditentukan dalam browser yang dikendalikan.

## search_input = driver.find_element(By.NAME, "email_mhs")
metode dalam Selenium WebDriver yang digunakan untuk mencari elemen pada halaman web berdasarkan atribut "name" elemen tersebut. Metode ini mengembalikan elemen pertama yang ditemukan dengan atribut "name" yang cocok.

# search_input.send_keys("idaymulyadi10@gmail.com")
untuk memasukan input teks pada Element "email_mhs"

## Proses Load URL
- modul urllib.request : untuk mengakses URL dan mengunduh datanya.
- Fungsi load_url mengambil URL sebagai argumen, kemudian mencoba membuka URL tersebut menggunakan urlopen dari modul urllib.request
- Jika berhasil, data dari URL tersebut dibaca menggunakan read() dan kemudian dapat Anda proses sesuai kebutuhan.

## Buat File Proses Input Text
- process_text yang menerima input teks sebagai argumen (contoh: metode upper() untuk mengubah teks menjadi huruf kapital.)
- fungsi input(): Untum memasukan text
- fungsi process_text dengan input teks sebagai argumen. Hasil yang diproses kemudian dicetak ke layar.