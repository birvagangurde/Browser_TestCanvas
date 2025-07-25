# 44.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")

'''
Why no loop here?
When the index/position is fixed and known (like 3rd button always being Option 2), 
using index is simpler and more efficient than a for loop.
'''

radiobuttons[2].click()

'''
Indexing is used when you know the structure won’t change.
radiobuttons[2] clicks the third radio button.
No need to use loops here if you're sure of the index.

is_selected() helps verify if a checkbox or radio button is selected.   

'''
assert radiobuttons[2].is_selected()


assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

'''
Key Tips
assert not is used to check invisibility.
If the element does show up instead of hiding, the test fails.

Use .is_selected() for checkboxes and radio buttons validation.
Use .is_displayed() to check element visibility for hide/show scenarios.
'''

