import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    print("\n[SETUP] Opening Chrome Browser")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("\n [TEARDOWN] closing Browser")
    driver.quit()