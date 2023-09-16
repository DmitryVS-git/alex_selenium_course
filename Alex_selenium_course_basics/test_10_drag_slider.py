import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

base_url = "https://www.schoolsw3.com/howto/howto_js_rangeslider.php"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)

driver.get(base_url)

driver.maximize_window()

default_slider = driver.find_element(By.XPATH, "//div[@id='slidecontainer']/input")
# кликаем и держим ползунок, передвигаем по оси x на 50 пунктов, отпускаем и исполняем
action.click_and_hold(default_slider).move_by_offset(50, 0).release().perform()

square_slider = driver.find_element(By.ID, "id2")
action.click_and_hold(square_slider).move_by_offset(-150, 0).release().perform()

time.sleep(2)
