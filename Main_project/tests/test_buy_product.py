import time

import pytest

from pages.checkout_user_info_page import CheckUserInfoPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pages.payment_page import PaymentPage


@pytest.mark.run(order=2)
def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    print(f'=== Start test "{test_buy_product_1.__name__.capitalize()}" ===')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product_1()
    print("Enter the cart")

    cp = CartPage(driver)
    cp.click_button_checkout()
    print("Go to the checkout information page")

    cuip = CheckUserInfoPage(driver)
    cuip.input_information()
    print("Go to the overview page")

    pp = PaymentPage(driver)
    pp.payment()

    fp = FinishPage(driver)
    fp.finish()

    print(f"=== The '{test_buy_product_1.__name__.capitalize()}' was successful! ===")


@pytest.mark.run(order=1)
def test_buy_product_2(set_up, set_group):
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    print(f'=== Start test "{test_buy_product_2.__name__.capitalize()}" ===')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product_2()
    print("Enter the cart")

    cp = CartPage(driver)
    cp.click_button_checkout()
    print("Go to the checkout information page")

    print(f"=== The '{test_buy_product_2.__name__.capitalize()}' was successful! ===")


@pytest.mark.run(order=3)
def test_buy_product_3(set_up, set_group):
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    print(f'=== Start test "{test_buy_product_3.__name__.capitalize()}" ===')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product_3()
    print("Enter the cart")

    cp = CartPage(driver)
    cp.click_button_checkout()
    print("Go to the checkout information page")

    print(f"=== The '{test_buy_product_3.__name__.capitalize()}' was successful! ===")
