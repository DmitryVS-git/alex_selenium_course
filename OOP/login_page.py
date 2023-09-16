from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        '''Login'''
        user_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "user-name")))
        user_name.send_keys(login_name)
        print("Input Login")

        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
        password.send_keys(login_password)
        print("Input password")

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        print("Click login_button")
        '''// Login'''