import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//input[@name='field-keywords']").send_keys("iphone13")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input[id='nav-search-submit-button']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='sg-col-inner']//span[text()='74,900']").click()
time.sleep(10)



