import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class SystemTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()
        
    def test_login(self):
        self.driver.get("https://trifekta.id/login")

        # get username input
        username = self.driver.find_element(By.ID, "username")
        # input username value
        username.send_keys("tester06@mailinator.com")

        # get password input
        password = self.driver.find_element(By.ID, "password")
        # input password value
        password.send_keys("12345678")

        # get login button
        login_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        login_button.click()
        
        # find class post-write to check if login success
        post_write = self.driver.find_element(By.CLASS_NAME, "post-write")
        self.assertTrue(post_write.is_displayed())
        

if __name__ == "__main__":
    unittest.main()

