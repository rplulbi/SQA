import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Membuka halaman web Enroll
driver.get("https://enroll.ulbi.ac.id/")

# Mencari elemen input pencarian menggunakan ID
search_input = driver.find_element(By.NAME, "email_mhs")

# Memasukkan kata kunci pencarian
search_input.send_keys("idaymulyadi10@gmail.com")


# Tambahkan penundaan waktu untuk melihat hasil pencarian
time.sleep(10)

# Misalnya, dapatkan judul halaman saat ini
page_title = driver.title
print("Judul halaman:", page_title)

# Menutup WebDriver
driver.quit()
