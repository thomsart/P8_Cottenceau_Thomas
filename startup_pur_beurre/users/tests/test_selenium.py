#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(PATH, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("http://localhost:8000/")
print(driver.title)

 
search = driver.find_element_by_xpath("//form[@id='search_product_nav_bar']")
search.send_keys("frosties")
search.send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()