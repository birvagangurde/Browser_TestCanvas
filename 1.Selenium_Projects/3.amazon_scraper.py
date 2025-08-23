import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()

# Open Amazon India homepage
driver.get("https://www.amazon.in/")

# Search headphones
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("headphones")
driver.find_element(By.ID, 'nav-search-submit-button').click()

# 🔍 Search for 'headphones'

# Locate all actual product result blocks using their unique data-component-type attribute
# This avoids picking up ads, banners, or other non-product elements
products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")


time.sleep(5)
data = []

for product in products[:5]:
    product_titles = product.find_element(By.XPATH, './/a/h2/span').text
    # print(product_titles.text)
    try:
        product_price = product.find_element(By.XPATH, './/span[@class="a-price"]').text
        # print(product_price.text)
    except:
        product_price = "N/A"

    data.append([product_titles, product_price])


# 🧾 Write the data to a CSV file
with open("amazon_headphones.csv", 'w', newline='', encoding='utf-8-sig') as file:
    # utf-8-sig adds a Byte Order Mark (BOM) at the top of the file —
    # Excel recognizes it and correctly displays ₹ instead of junk like â‚¹.
    writer = csv.writer(file)
    writer.writerow(['Product Title', 'Product Price'])
    writer.writerows(data)

# Notes
# Amazon pagesnew are dynamic — always add delays or use WebDriverWait to avoid grabbing incomplete DOM.
# If prices are missing (sponsored listings or unavailable products), handle exceptions gracefully.
