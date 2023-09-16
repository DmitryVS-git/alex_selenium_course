import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



base_url = "https://demoqa.com/date-picker"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)

driver.get(base_url)

driver.maximize_window()

date = driver.find_element(By.ID, "datePickerMonthYearInput")
date.click()

time.sleep(2)

# date.send_keys(Keys.CONTROL + "a")
# date.send_keys(Keys.BACKSPACE)
# date.send_keys("12/14/1993")
# date.send_keys(Keys.ENTER)
# time.sleep(2)

day = datetime.now().strftime("%d")
date = int(day) + 1
locator = f"//div[@aria-label='Choose Friday, September {date}th, 2023']"
date_15_sep = driver.find_element(By.XPATH, locator)
date_15_sep.click()
time.sleep(2)


# new_date = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
# date_11_sep.click()

