import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("iphone14")
driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(5)
htang= driver.find_element(By.XPATH,"//span[@class='a-price-whole']").click()

