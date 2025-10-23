import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(results)

assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# time.sleep(5)


'''
Problem with only implicit wait: Unnecessarily delays
It waits globally for a defined time (e.g., 5s).

Explicit wait: 
Target specific element (e.g., promo message) and tell Selenium:
"Wait up to 10 seconds for this one element only"

Benefits:
Overrides implicit wait.
Used only for that specific element.
Rest of the app still runs with faster default implicit wait.


'''
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo" )))

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

'''
visibility_of_element_located()	Element appears and is visible
presence_of_element_located()	Element is present in DOM (not necessarily visible)
text_to_be_present_in_element()	Specific text appears in an element
title_is() / title_contains()	Waits for the page title
'''