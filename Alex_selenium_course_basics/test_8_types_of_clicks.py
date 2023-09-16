import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



base_url = "https://demoqa.com/buttons"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(base_url)

driver.maximize_window()

action = ActionChains(driver)

double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
action.double_click(double_click_btn).perform()

right_click_btn = driver.find_element(By.ID, "rightClickBtn")
action.context_click(right_click_btn).perform()

click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
click_btn.click()

time.sleep(2)
