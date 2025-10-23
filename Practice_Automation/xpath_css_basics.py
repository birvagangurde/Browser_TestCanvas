from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

# Questions: -
# Locate the username and password fields using
# ID
# XPATH
# CSS Selector

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")


driver.find_element(By.XPATH, "//input[@type='text']").send_keys("tomsmith")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("tomsmith")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("SuperSecretPassword!")


