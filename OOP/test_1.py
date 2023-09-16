from login_page import LoginPage


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Test1:
    base_url = "https://www.saucedemo.com"
    login_standard_user = "standard_user"
    password_main = "secret_sauce"

    def test_select_product(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(self.base_url)

        driver.maximize_window()
        print(f'=== Start test "{self.test_select_product.__name__.capitalize()}" ===')

        login = LoginPage(driver)

        login.authorization(login_name=self.login_standard_user, login_password=self.password_main)

        '''Add Product to the cart'''
        btn_add_to_cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        btn_add_to_cart.click()
        print("Click 'add to cart' button")

        cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "shopping_cart_container")))
        cart.click()
        print("Enter the cart")

        success_test = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".title")))
        value_success_test = success_test.text

        assert "Your Cart" == value_success_test

        print("=== The test was successful! ===")

        '''// Add Product to the cart'''


test = Test1()
test.test_select_product()
