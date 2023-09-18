from pages.login_page import LoginPage
from pages.main_page import MainPage

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

    mp = MainPage(driver)
    mp.select_product()
    print("Enter the cart")

    print("=== The test was successful! ===")

    '''// Add Product to the cart'''
