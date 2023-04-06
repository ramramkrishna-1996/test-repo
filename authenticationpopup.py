import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(20)