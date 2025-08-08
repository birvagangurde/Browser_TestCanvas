from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.implicitly_wait(4)


# for customized css = a[href]*='shop'
# xpath - using regular expressions in xpath or css  -  not recommended - //a[contains(@href, 'shop')]
# thats why the customized css works fine

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

# Common xpath which is taking all the four cards
# //div[@class='card h-100']   gives the 4 cards

total_cards = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

# 💡 Each card will be treated individually in a for loop
for card in total_cards:
    card.find_element(By.CLASS_NAME, "btn-info").click()

