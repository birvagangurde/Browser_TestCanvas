from selenium.webdriver.common.by import By


def test_valid_login(browser):
    browser.get("https://www.saucedemo.com/v1/")

    browser.find_element(By.ID, "user-name").clear()
    browser.find_element(By.ID, "user-name").send_keys("standard_user")

    browser.find_element(By.ID, "password").send_keys("secret_sauce")

    browser.find_element(By.XPATH, "//input[@type='submit']").click()

    assert "inventory" in browser.current_url



