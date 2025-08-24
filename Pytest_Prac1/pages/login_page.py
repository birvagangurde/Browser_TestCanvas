from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//input[@type='submit']")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")
        self.card = (By.CLASS_NAME, "shopping_cart_badge")

    def load_website(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def get_cart_count(self):
        try:
            card_count = self.driver.find_element(*self.card).text
            return card_count
        except:
            return None
