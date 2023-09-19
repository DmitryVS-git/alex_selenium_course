import time

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_user_info_page import CheckUserInfoPage

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
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    print(f'=== Start test "{test_buy_product.__name__.capitalize()}" ===')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product()
    print("Enter the cart")

    cp = CartPage(driver)
    cp.click_button_checkout()
    print("Go to the checkout information page")

    cuip = CheckUserInfoPage(driver)
    cuip.input_information()
    print("Go to the overview page")

    time.sleep(2)

    print("=== The test was successful! ===")

    '''// Add Product to the cart'''
