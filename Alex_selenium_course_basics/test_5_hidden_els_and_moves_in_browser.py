import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

base_url = "https://www.saucedemo.com"
login_standard_user = "standard_user"
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

menu = driver.find_element(By.ID, "react-burger-menu-btn")
menu.click()
print("Click menu button")

time.sleep(2)

menu_link_about = driver.find_element(By.ID, "about_sidebar_link")
menu_link_about.click()
print("Click link about in the menu")

now_date = datetime.now().strftime("%Y.%m.%d %H.%M.%S")
name_screenshot = f"screen_{now_date}.png"

driver.save_screenshot(f".\screen\{name_screenshot}")

driver.back()
print("Go back")
driver.forward()
print("Go forward")
time.sleep(2)

