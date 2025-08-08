from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.implicitly_wait(4)


driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()


total_cards = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

# 💡 Each card will be treated individually in a for loop
for card in total_cards:
    # Chaining of web elements
    productName = card.find_element(By.XPATH, "div/h4/a")
    if productName == "Blackberry":
        productName.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

# Checkout name - a[class*='btn-primary'] - used regular expression to avoid huge xpath
