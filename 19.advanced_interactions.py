import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
# action.double_click()
# action.context_click()
# action.drag_and_drop()

# 1. Hover
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(2)
# 2. Click after hover
# ➡️ Moves to "Reload" and clicks it.
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()


'''
🔸 Always call .perform() at the end to execute the action.

source = driver.find_element(By.ID, "source")
target = driver.find_element(By.ID, "target")
action.drag_and_drop(source, target).perform()

Always finish action chains with .perform() to trigger the behavior.
move_to_element() is key for hover actions; it does not click, just moves the pointer.

Use By.ID, By.LINK_TEXT, etc., for locating elements.
Implicit waits (like driver.implicitly_wait(5)) handle small delays in element loading.

Right-click is done with context_click(), and you can hover over menus before right-clicking.
You can click on dropdown options after hover using the same pattern.
Use driver.maximize_window() for better view and debugging.
ActionChains is ideal for testing dynamic menus, hoverable elements, and rich UI components.
'''