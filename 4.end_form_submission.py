
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demoqa.com/automation-practice-form")
time.sleep(3)

# 🔧 Tasks:
# Fill personal info.

# First Name
driver.find_element(By.ID, "firstName").send_keys("Aakansha")

# Last Name
driver.find_element(By.ID, "lastName").send_keys("Niyati")

# Email ID
driver.find_element(By.ID, "userEmail").send_keys("gujar@gmail.com")

# Gender selection: -

# ❌ This targets the hidden radio input (which is not clickable)
# driver.find_element(By.CSS_SELECTOR, "#gender-radio-2").click()

# ✅ Correct approach: Wait for the label (visible and clickable) that triggers the radio input
gender_label = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[@for='gender-radio-2']"))
)

# 🔽 Scroll the gender label into view — ensures it's visible before clicking
driver.execute_script("arguments[0].scrollIntoView(true);", gender_label)

time.sleep(1)
gender_label.click()

# Phone number
driver.find_element(By.ID, "userNumber").send_keys("9821345234")

# Date of Birth
date_picker = driver.find_element(By.ID, "dateOfBirthInput")

driver.execute_script("arguments[0].scrollIntoView(true);", date_picker)

time.sleep(1)
date_picker.click()
