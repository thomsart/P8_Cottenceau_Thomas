#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex_co
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

options = Options()
options.add_argument("--disable-extensions")
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe", options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://localhost:8000/")

search = driver.find_element(By.ID, "id_product_name")
search.send_keys("frosties")
search.send_keys(Keys.ENTER)
search.clear()
time.sleep(5)

try:
    result = WebDriverWait(driver, 10).until(ex_co.presence_of_element_located((By)))
except Exception:
    print("erreur: La page ne s'est pas ouverte!!!")


driver.quit()


# with driver:
#     wait = WebDriverWait(driver, 20)
#     driver.get("http://localhost:8000/")
#     driver.find_element(By.ID, "search_product_home").send_keys("frosties" + Keys.RETURN)
#     first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
#     print(first_result.get_attribute("textContent"))
