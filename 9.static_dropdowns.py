from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
# CSS -  tagname[attribute='value'] -> //input[@type='submit'],
# #id, .classname use these in selectors hub
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()



# Static dropdowns------------------------------------------------------------------------------------
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value()

# Tips---------------------
# use select class only when dealing with select html elements
# know these 3 methods(visible text, index, value) to confirm if the dropdown is static



driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()


