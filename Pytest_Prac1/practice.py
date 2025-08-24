from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/v1/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.XPATH, "//input[@type='submit']").click()

card_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text



# error_message = browser.find_element(By.XPATH, "//h3[@data-test='error']").text




