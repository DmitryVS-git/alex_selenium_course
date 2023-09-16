import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



base_url = "https://testpages.herokuapp.com/styled/basic-html-form-test.html"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(base_url)

driver.maximize_window()

checkbox_1 = driver.find_element(By.XPATH, "//input[@value='cb1']")
checkbox_1.click()

assert checkbox_1.get_attribute("checked")

checkbox_3 = driver.find_element(By.XPATH, "//input[@value='cb3']")
checkbox_3.click()

assert checkbox_3.get_attribute("checked") is None

radio_btn_1 = driver.find_element(By.XPATH, "//input[@value='rd1']")
radio_btn_1.click()

radio_btn_2 = driver.find_element(By.XPATH, "//input[@value='rd2']")

assert radio_btn_1.get_attribute("checked")
assert radio_btn_2.get_attribute("checked") is None

time.sleep(2)