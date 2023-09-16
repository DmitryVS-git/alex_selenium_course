import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com")
driver.maximize_window()

user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

products_title = driver.find_element(By.CSS_SELECTOR, ".title").text

assert products_title == "Products"

time.sleep(2)

print("Finita la tua comedia, amico mio")