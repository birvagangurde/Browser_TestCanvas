
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

file_path = "C:/Users/BIRVA/Downloads/download.xlsx"

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")

driver.find_element(By.ID, "downloadButton").click()

# edit the excel with updated value

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
'''
The input tag has attribute: type="file" ✅
If not present, Selenium cannot handle the native OS file window.
'''
file_input.send_keys(file_path)

wait = WebDriverWait(driver, 5)

toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")

wait.until(expected_conditions.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)   #unpacks the tuple


'''
Selenium can't automate OS pop-ups (like Windows file dialog).
Always use implicit waits for stability.
Use explicit waits for dynamic elements like toast.
'''
