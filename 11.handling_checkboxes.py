# 43 handling checkboxes using selenium python programming

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

'''
The checkbox you're trying to select (e.g., Option 2) may appear in a 
different order on different test runs.
So, index-based access is not reliable.  But it's unreliable since position may change (dynamic UI).
Instead, use the value attribute to identify and act on the correct checkbox.


'''
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# This returns a list of all checkboxes using XPath
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()  #Use it to write assertions and validate UI interaction in tests.
        break


'''
Element Locators Hierarchy:
Prefer using ID, Name, or Value.
But if not available → use XPath or CSS Selector.
'''

# Practice on radiobuttons

radio_buttons = driver.find_elements(By.XPATH, '//input[@name="radioButton"]')

for button in radio_buttons:
    if button.get_attribute("value") == "radio2":
        button.click()
        break

