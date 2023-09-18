from base.base_class import Base

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_checkout = "checkout"

    # Getters
    def get_button_checkout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_checkout)))

    # Actions
    def click_button_checkout(self):
        self.get_button_checkout().click()
        print("Click checkout button")

    # Methods
    def confirm_product(self):
        self.print_current_url()
        self.click_button_checkout()

