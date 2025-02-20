from selenium.webdriver.common.by import By
from functions.utils import get_xpath
from functions.page_validations import page_loads
import random

inventory_locators = get_xpath("Inventory")

def add_products_to_cart(driver):
    all_add_to_cart_buttons = driver.find_elements(By.XPATH, inventory_locators["add_to_cart_buttons"])
    random_add_quantity = random.randint(1,len(all_add_to_cart_buttons))
    for i in range(random_add_quantity):
        all_add_to_cart_buttons[i].click()

def go_to_cart(driver):
    cart_element = driver.find_element(By.XPATH, inventory_locators["go_to_cart_icon"])
    cart_element.click()
    page_loads(driver, "Cart")