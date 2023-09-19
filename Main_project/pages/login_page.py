from base.base_class import Base

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(Base):
    url = "https://www.saucedemo.com"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    user_name = "user-name"
    password = "password"
    button_login = "login-button"
    check_word = ".title"

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_login)))

    def get_check_word(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.check_word)))

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.print_current_url()

        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()

        self.assert_word(self.get_check_word(), "Products")
