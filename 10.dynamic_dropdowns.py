# 41. Dynamic dropdowns
import time

from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break