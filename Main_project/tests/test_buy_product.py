from pages.login_page import LoginPage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def test_buy_product():
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = options)
    print(f'=== Start test "{test_buy_product.__name__.capitalize()}" ===')

    login = LoginPage(driver)
    login.authorization()

    cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "shopping_cart_container")))
    cart.click()
    print("Enter the cart")

    print("=== The test was successful! ===")

    '''// Add Product to the cart'''
