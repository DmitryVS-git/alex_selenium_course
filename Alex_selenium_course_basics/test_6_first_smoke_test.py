import time

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

'''INFO Product №1'''
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text

print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/parent::div/following-sibling::div//div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

add_to_cart_btn = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart_btn.click()
print("Select product 1")

cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
cart.click()
print("Enter cart")

'''INFO Shopping cart'''
cart_product_1 = driver.find_element(By.ID, "item_4_title_link")
value_cart_product_1 = cart_product_1.text

print(value_cart_product_1)
assert value_cart_product_1 == value_product_1
print("INFO cart product 1 is GOOD")

price_cart_product_1 = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_cart_price_product_1 == value_price_product_1
print("INFO cart price product 1 is GOOD")

btn_checkout = driver.find_element(By.ID, "checkout")
btn_checkout.click()
print("Click checkout button")

'''Checkout User Info'''
first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Dmitry")
print("Input first name")

last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Dmitrievich")
print("Input last name")

zip_code = driver.find_element(By.ID, "postal-code")
zip_code.send_keys("256t25626")
print("Input zip code")

btn_continue = driver.find_element(By.ID, "continue")
btn_continue.click()
print("Click continue button")

'''Checkout Overview Info'''
overview_product_1 = driver.find_element(By.ID, "item_4_title_link")
value_overview_product_1 = overview_product_1.text

print(value_overview_product_1)
assert value_overview_product_1 == value_cart_product_1
print("INFO overview product 1 is GOOD")

overview_price_product_1 = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price")
value_overview_price_product_1 = overview_price_product_1.text
print(value_overview_price_product_1)
assert value_overview_price_product_1 == value_cart_price_product_1
print("INFO overview price product 1 is GOOD")

item_total = driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label")
# value_item_total = item_total.text.split(": ")[1]
value_item_total = item_total.text

assert value_price_product_1 in value_item_total

print("INFO final item total is GOOD")
