import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

'''
CSS Selectors via Selector Hub
. is for class names
If using ID → use #idname

Using sleep is temporary; later replaced by implicit or explicit waits.
'''
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
# 📌 This XPath captures all products dynamically,
# so the test won’t break if more products are added later.

count = len(results)

assert count > 0
