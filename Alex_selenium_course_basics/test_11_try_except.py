import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# base_url = "https://demoqa.com/dynamic-properties"
base_url = "https://google.com"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)

driver.get(base_url)

driver.maximize_window()

# try:
#     visible_btn = driver.find_element(By.ID, "visibleAfter")
#     visible_btn.click()
# except NoSuchElementException as exception:
#     print(NoSuchElementException)
#     time.sleep(5)
#     print("Sleeping for 5 secs")
#     visible_btn = driver.find_element(By.ID, "visibleAfter")
#     visible_btn.click()


