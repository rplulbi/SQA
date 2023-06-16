from selenium.webdriver import Chrome

driver = Chrome()
driver.get("https://www.google.com/?hl=ID")

driver.find_element_by_name("q").send_keys("SQA")
