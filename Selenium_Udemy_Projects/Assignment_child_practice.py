import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()

windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])

red_text = driver.find_element(By.XPATH, "//p[@class='im-para red']").text

email_id =  red_text.split(" ")[4]
print(email_id)
driver.close()

driver.switch_to.window(windows_opened[0])

driver.find_element(By.NAME, "username").send_keys(email_id)
driver.find_element(By.NAME, "password").send_keys(email_id)

driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
incorrect_text = driver.find_element(By.CSS_SELECTOR, ".alert").text

print(incorrect_text)