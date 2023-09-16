import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://the-internet.herokuapp.com/add_remove_elements/"
base_url_2 = "https://the-internet.herokuapp.com/dynamic_loading/1"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)

driver.get(base_url_2)

driver.maximize_window()

# driver.implicitly_wait(10) - не явное ожидание

# print("Start Test")
# add_btn = driver.find_element(By.XPATH, "//button")
# add_btn.click()
#
# delete_btn = driver.find_element(By.XPATH, "//div[@id='elements']/button")
# delete_btn.click()
# print("Finish Test")

# print("Start Test")
# add_btn = driver.find_element(By.XPATH, "//button")
# add_btn.click()
#
# delete_btn = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='elements']/button")))
# delete_btn.click()
# print("Finish Test")

print("Start Test")
start_btn = driver.find_element(By.XPATH, "//button")
start_btn.click()

expected_text = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']//h4")))
print("Finish Test")