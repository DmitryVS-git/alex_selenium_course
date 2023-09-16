import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import Keys
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
user_name.send_keys(Keys.BACKSPACE * 2)
user_name.send_keys("er")
print("Input Login")

password = driver.find_element(By.ID, "password")
password.send_keys(password_all)
print("Input password")
password.send_keys(Keys.RETURN)

filter_dropdown = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")
filter_dropdown.click()
print("Click filter")
filter_dropdown.send_keys(Keys.DOWN * 2)
time.sleep(3)
filter_dropdown.send_keys(Keys.UP)
filter_dropdown.send_keys(Keys.RETURN)
print("Enter filter")

now_date = datetime.now().strftime("%Y.%m.%d %H.%M.%S")
name_screenshot = f"screen_{now_date}.png"

driver.save_screenshot(f".\screen\{name_screenshot}")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Click login_button")
