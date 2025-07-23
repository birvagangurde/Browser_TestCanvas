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

# 42

# print(driver.find_element(By.ID, "autosuggest").text)

'''
⚠️ Issue with .text:
You cannot retrieve dynamically inserted values (like India) using .text.

.text works only for static content present when the page loads.

'''

# print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "BASINDIA"

'''   
Input elements update their text via the DOM attribute value.
get_attribute("value") pulls this updated info.

Replaces manual output checks.
If mismatch: test fails immediately, indicating a bug.
'''
