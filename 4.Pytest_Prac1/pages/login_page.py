

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = "user-name"
        self.password_input = "password"
        self.login_button = "//input[@type='submit']"
        self.error_message = "//h3[@data-test='error']"

    def load_website(self):
        self.driver.get("https://www.saucedemo.com/v1/")

    def login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("wrong_password")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
