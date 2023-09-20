from base.base_class import Base

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PaymentPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_finish = "finish"

    # Getters
    def get_button_finish(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_finish)))

    # Actions
    def click_button_finish(self):
        self.get_button_finish().click()
        print("Click finish button")

    # Methods
    def payment(self):
        self.print_current_url()
        self.click_button_finish()

