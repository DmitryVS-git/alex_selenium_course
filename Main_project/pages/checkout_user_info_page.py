from base.base_class import Base

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckUserInfoPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name = "first-name"
    last_name = "last-name"
    zip_code = "postal-code"
    button_continue = "continue"

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.zip_code)))

    def get_button_continue(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_continue)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("Input zip code")

    def click_button_continue(self):
        self.get_button_continue().click()
        print("Click continue button")

    # Methods
    def input_information(self):
        self.print_current_url()

        self.input_first_name("Ivan")
        self.input_last_name("Ivanov")
        self.input_zip_code("63262")

        self.click_button_continue()

