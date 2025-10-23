from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.card = (By.CLASS_NAME, "shopping_cart_badge")

    def add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def get_cart_count(self):
        try:
            card_count = self.driver.find_element(*self.card).text
            return card_count
        except:
            return None

    def logout(self):
        self.driver.find_element(By.CLASS_NAME, "bm-burger-button").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
