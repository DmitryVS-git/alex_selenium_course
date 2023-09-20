from base.base_class import Base

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_add_to_cart_product_1 = "add-to-cart-sauce-labs-backpack"
    button_add_to_cart_product_2 = "add-to-cart-sauce-labs-bike-light"
    button_add_to_cart_product_3 = "add-to-cart-sauce-labs-bolt-t-shirt"
    sidebar_menu = "react-burger-menu-btn"
    link_sidebar_menu_about = "about_sidebar_link"
    cart = "shopping_cart_container"

    # Getters
    def get_button_add_to_cart_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_add_to_cart_product_1)))

    def get_button_add_to_cart_product_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_add_to_cart_product_2)))

    def get_button_add_to_cart_product_3(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_add_to_cart_product_3)))

    def get_sidebar_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.sidebar_menu)))

    def get_link_sidebar_menu_about(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.link_sidebar_menu_about)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.cart)))

    # Actions
    def click_button_add_to_cart_product_1(self):
        self.get_button_add_to_cart_product_1().click()
        print("Click add to cart button")

    def click_button_add_to_cart_product_2(self):
        self.get_button_add_to_cart_product_2().click()
        print("Click add to cart button")

    def click_button_add_to_cart_product_3(self):
        self.get_button_add_to_cart_product_3().click()
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
    def select_product_1(self):
        self.print_current_url()
        self.click_button_add_to_cart_product_1()
        self.click_cart()

    def select_product_2(self):
        self.print_current_url()
        self.click_button_add_to_cart_product_2()
        self.click_cart()

    def select_product_3(self):
        self.print_current_url()
        self.click_button_add_to_cart_product_3()
        self.click_cart()


    def select_sidebar_menu_about(self):
        self.print_current_url()
        self.click_sidebar_menu()
        self.click_link_sidebar_menu_about()
        self.assert_url("https://saucelabs.com/")
