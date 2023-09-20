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
    sidebar_menu = "react-burger-menu-btn"
    link_sidebar_menu_about = "about_sidebar_link"
    cart = "shopping_cart_container"

    # Getters
    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_add_to_cart)))

    def get_sidebar_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.sidebar_menu)))

    def get_link_sidebar_menu_about(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.link_sidebar_menu_about)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.cart)))

    # Actions
    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print("Click add to cart button")

    def click_sidebar_menu(self):
        self.get_sidebar_menu().click()
        print("Click sidebar menu")

    def click_link_sidebar_menu_about(self):
        self.get_link_sidebar_menu_about().click()
        print("Click link 'about' sidebar's menu")

    def click_cart(self):
        self.get_cart().click()
        print("Click and enter the cart")

    # Methods
    def select_product(self):
        self.print_current_url()
        self.click_button_add_to_cart()
        self.click_cart()

    def select_sidebar_menu_about(self):
        self.print_current_url()
        self.click_sidebar_menu()
        self.click_link_sidebar_menu_about()
        self.assert_url("https://saucelabs.com/")
