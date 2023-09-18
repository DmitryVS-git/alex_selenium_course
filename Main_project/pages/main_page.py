from base.base_class import Base

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_add_to_cart = "add-to-cart-sauce-labs-backpack"
    cart = "shopping_cart_container"

    # Getters
    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_add_to_cart)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.cart)))

    # Actions
    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print("Click add to cart button")

    def click_cart(self):
        self.get_cart().click()
        print("Click and anter the cart")

    # Methods
    def select_product(self):
        self.print_current_url()
        self.click_button_add_to_cart()
        self.click_cart()

