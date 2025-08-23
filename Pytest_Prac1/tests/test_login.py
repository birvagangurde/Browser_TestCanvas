
from selenium.webdriver.common.by import By

from Pytest_Prac1.pytestsDemo.login_page import LoginPage


def test_valid_login(browser):
    login_page = LoginPage(browser)

    # browser.get("https://www.saucedemo.com/v1/")
    login_page.load_website()

    # browser.find_element(By.ID, "user-name").send_keys("standard_user")

    # browser.find_element(By.ID, "password").send_keys("secret_sauce")
    # browser.find_element(By.ID, "password").send_keys("wrong_password")

    # browser.find_element(By.XPATH, "//input[@type='submit']").click()

    login_page.login("standard_user", "secret_sauce")

    error_message = browser.find_element(By.XPATH, "//h3[@data-test='error']").text
    print(error_message)

    assert "inventory" in browser.current_url


def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.load_website()
    login_page.login("standard_user", "wrong_pasword")
    assert "Epic sadface" in login_page.get_error_message()

