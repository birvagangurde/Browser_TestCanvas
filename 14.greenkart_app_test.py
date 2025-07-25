import time

from selenium import webdriver
from selenium.webdriver.common.by import By

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
time.sleep(5)
# time.sleep(5) used here temporarily.
# ❌ Not recommended – Will replace with Explicit Wait (in next lesson).

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)



'''
✅ Benefits of chaining:

🧠 Explanation (Chaining Concept):
results holds parent web elements (i.e., product blocks).
Instead of using driver.find_element, we use result.find_element.
This limits the scope of the XPath to within each individual product card.


Faster lookup (search within a block instead of whole page)
Cleaner, modular, and easy-to-read code

# BAD (searches whole page)
driver.find_element(By.XPATH, "//div[@class='product']/div/button").click()

# GOOD (searches only within that product block)
result.find_element(By.XPATH, "div/button").click()
'''