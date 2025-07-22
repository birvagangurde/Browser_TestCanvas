from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

# Key Notes
# Always prefer ID when available - fastest locator
# CSS selectors are generally faster than XPATH
# XPATH allows advanced DOM Traversal - great when no attributes are unique

