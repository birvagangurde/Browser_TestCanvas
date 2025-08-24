from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

# Use contains (*=) in CSS selector to match partial attribute values.
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

# You hit checkout and you get an autosuggestive drop down which we will be dealing with
driver.find_element(By.ID, "country").send_keys("ind")

# Autosuggest may load in < 4s or > 4s — explicit wait is safer.
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))


driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
'''
If clicking anywhere in a label selects the checkbox, click the parent element.
Optional tag names:
XPath: //*[@class='value'] or //tag[@class='value']
CSS: [type='submit'] or tag[type='submit']
'''
driver.find_element(By.CSS_SELECTOR, "[type=""submit]").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
print(successText)

assert "Success! Thank you!" in successText

driver.close()




