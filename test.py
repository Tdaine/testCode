#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://demo.zentao.net/user-login-lw==.html")
time.sleep(3)
driver.find_element_by_id("account").clear()
time.sleep(3)
driver.find_element_by_id("account").send_keys("demo")
time.sleep(3)
driver.find_element_by_name("password").send_keys(Keys.TAB)
time.sleep(3)
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()


