# Assignment 1: -
# Infosys Stock Page
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup Chrome with Notifications disabled
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)

driver.get("https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT")

# Optional: wait for html pop up and dismiss it

try:
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'No Thanks')]"))
    ).click()

except:
    print("Popup not found or already gone")

# Current stock price


# get the stock price - all child divs of the price container
# price_element = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'inprice1') and contains(@class, 'nsecp')][1]"))
# )
# stock_price = price_element.text.replace('\n', '')
#
# print(stock_price)

wait = WebDriverWait(driver, 10)

price_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@rel]")))

stock_price = price_element.get_attribute("rel")
print(stock_price)  # this is the current stock price


# 52 Week High/Low

week_low_price = driver.find_element(By.ID, "sp_yearlylow")
print(week_low_price.text)

week_high_price = driver.find_element(By.ID, "sp_yearlyhigh")
print(week_high_price.text)


# Company Name

company_name = driver.find_element(By.ID, "stockName").text
print(company_name)


# Sector Name
sector_full_text = driver.find_element(By.XPATH, "//a[@title='Software & IT Services sector details']").text
print(sector_full_text)

# Example text: "Sector : Software & IT Services | Industry : IT Services & Consulting\nSoftware & IT Services"

