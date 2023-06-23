import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Membuka halaman web
driver.get("https://practicetestautomation.com/practice-test-login/")