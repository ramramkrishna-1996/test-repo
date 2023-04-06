import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
#time.sleep(3)
myalert=driver.switch_to.alert
myalert.accept()
time.sleep(3)



