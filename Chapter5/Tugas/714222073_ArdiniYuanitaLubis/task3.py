import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)
        # Menutup WebDriver
        self.driver.quit()

    def test_search_google(self):
        # Membuka halaman web Google
        self.driver.get("https://dinilubis.github.io/")  

        # Mencari elemen input pencarian menggunakan ID
        search_input1 = self.driver.find_element(By.ID, "username")
        search_input2 = self.driver.find_element(By.ID, "password")
        search_input3 = self.driver.find_element(By.ID, "tombol")

        # Memasukkan kata kunci pencarian
        search_input1.send_keys("Dini")
        search_input2.send_keys("123123")
        # Menekan tombol Enter untuk melakukan pencarian
        search_input1.send_keys(Keys.ENTER)
        search_input2.send_keys(Keys.ENTER)
        search_input3.send_keys(Keys.ENTER)

        # Memastikan halaman hasil pencarian muncul
        search_results = self.driver.find_elements(By.XPATH, "//div[@class='g']")
        self.assertTrue(len(search_results) > 0, "Hasil pencarian ditemukan")


if __name__ == "__main__":
    unittest.main()
