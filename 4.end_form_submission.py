
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

# 🔽 Scroll the gender label into view — ensures it's visible before clicking hence scrolling down helps
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

# .scrollIntoView(true) is used when elements are off-screen.

# Wait to ensure dropdowns are loaded
time.sleep(3)

# Select Year
year_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
year_select.select_by_value("2001")

time.sleep(2)
# Select Month
month_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
month_select.select_by_visible_text("November")

time.sleep(2)
# Select Day
driver.find_element(By.CLASS_NAME, "react-datepicker__day--007").click()

# Subject
subject_select = driver.find_element(By.XPATH, '(//input[@type="text"])[6]')
# subject_select = driver.find_element(By.ID, '#subjectsContainer')
subject_select.send_keys("Maths")
subject_select.send_keys(Keys.ENTER)

# Hobbies
hobbies_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//label[@for='hobbies-checkbox-3'])"))
)
hobbies_select.click()

# Upload a file

upload_input = driver.find_element(By.ID, 'uploadPicture')

# you just send the file path directly to the file input element using .send_keys().
upload_input.send_keys("C:\\Users\\BIRVA\\Downloads\\new.png")

time.sleep(5)

# Current Address

address = driver.find_element(By.ID, 'currentAddress')
driver.execute_script("arguments[0].scrollIntoView(true);", address)
address.send_keys("New colony Mumbai 400672")

# State

state_select = driver.find_element(By.ID, "react-select-3-input")
state_select.send_keys("Rajasthan")
time.sleep(2)
state_select.send_keys(Keys.ENTER)

# City

city_select = driver.find_element(By.ID, "react-select-4-input")
city_select.send_keys("Jai")
time.sleep(2)
city_select.send_keys(Keys.ENTER)

# Click on submit

driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Verifying the Submit message
time.sleep(3)

modal_title = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'example-modal-sizes-title-lg'))
)

assert 'Thank You' == modal_title



