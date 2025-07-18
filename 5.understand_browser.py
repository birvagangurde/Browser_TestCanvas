# Chapter 32 - Selenium Course

# ------------------------------------------
# Selenium Automation: Basic Browser Actions
# Description: Demonstrates opening browser, maximizing, fetching title and URL using Selenium.
# Supports: Chrome, Firefox, Microsoft Edge
# ------------------------------------------
import time

from selenium import webdriver
# Chrome driver service

# ✅ Step 1: Launch the browser (default: Chrome)
# To run on Firefox/Edge, replace webdriver.Chrome() with webdriver.Firefox()/webdriver.Edge()

driver = webdriver.Chrome()

# ✅ Step 2: Open the target URL
driver.get("https://rahulshettyacademy.com")

# ✅ Step 3: Maximize the browser window
# Ensures browser opens in fullscreen mode for better visibility during automation
driver.maximize_window()

time.sleep(2)

# ✅ Step 4: Fetch and print the page title
# Equivalent to the browser tab title (used to verify if correct page is loaded)

print(driver.title)

print(driver.current_url)