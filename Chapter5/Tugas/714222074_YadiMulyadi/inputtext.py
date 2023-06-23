import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Membuka halaman web
driver.get("https://practicetestautomation.com/practice-test-login/")

# Mencari elemen input pencarian menggunakan ID
search_input = driver.find_element(By.NAME, "username")

# Memasukkan kata kunci pencarian
search_input.send_keys("student")

# Tambahkan penundaan waktu untuk melihat hasil pencarian
time.sleep(10)

