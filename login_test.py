import os
import time
from tkinter import Image

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")

driver.find_element(By.ID, "submit").click()


message = driver.find_element(By.CLASS_NAME, "post-title").text
assert "Success1" in message


# Validate login and take screenshot on failure
try:
    message = driver.find_element(By.CLASS_NAME, "post-title").text
    assert "Success1" in message
    print("Login Sucessful")

except AssertionError:
    print("❌ Assertion failed. Capturing screenshot...")

    # Save screenshot in PyCharm project folder
    screenshot_path = os.path.join(os.getcwd(), "login_failure.png")
    driver.save_screenshot(screenshot_path)
    print(f"📸 Screenshot saved at: {screenshot_path}")
    time.sleep(5)
finally:
    driver.quit()

