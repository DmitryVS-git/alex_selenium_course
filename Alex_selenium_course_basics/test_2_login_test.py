import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

base_url = "https://www.saucedemo.com"
login_standard_user = "standard_use"
password_all = "secret_sauce"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(base_url)

driver.maximize_window()

user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys(login_standard_user)
print("Input Login")

password = driver.find_element(By.ID, "password")
password.send_keys(password_all)
print("Input password")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Click login_button")

warning = driver.find_element(By.XPATH, "//h3[@data-test='error']")
warning_text = warning.text

time.sleep(2)

assert warning_text == "Epic sadface: Username and password do not match any user in this service"

driver.refresh()
time.sleep(2)