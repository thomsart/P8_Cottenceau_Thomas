#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("http://localhost:8000/")
print(driver.title)

search = driver.find_element_by_id("search_product")
search.send_keys("frosties")
search.send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()