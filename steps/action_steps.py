from selenium.webdriver.common.by import By
from utils.utils import get_xpath, get_user_info
from steps.validation_steps import page_loads, verify_message
import random

def add_products_to_cart(driver):
    inventory_locators = get_xpath("Inventory")
    all_add_to_cart_buttons = driver.find_elements(By.XPATH, inventory_locators["add_to_cart_buttons"])
    random_add_quantity = random.randint(1,len(all_add_to_cart_buttons))
    for i in range(random_add_quantity):
        all_add_to_cart_buttons[i].click()

def checkout(driver):
    user_info = get_user_info("valid")
    cart_page_locators = get_xpath("Cart")
    checkout_page_locators = get_xpath("CheckoutOne")
    driver.find_element(By.XPATH, cart_page_locators["checkout_button"]).click()
    page_loads(driver, "CheckoutOne")
    checkout_data = {
        "first_name_input": "first_name",
        "last_name_input" : "last_name",
        "postal_code_input" : "postal_code"
    }
    for locator, data in checkout_data.items():
        driver.find_element(By.XPATH, checkout_page_locators[locator]).send_keys(user_info[data])
    driver.find_element(By.XPATH, checkout_page_locators["continue_checkout"]).click()
    driver.find_element(By.ID, "finish").click()

def login(driver, credentials="valid"):
    locators = get_xpath("Login")
    user_info = get_user_info(credentials)
    page_loads(driver, "Login")
    driver.find_element(By.XPATH, locators["username_input"]).send_keys(user_info["username"])
    driver.find_element(By.XPATH, locators["password_input"]).send_keys(user_info["password"])
    driver.find_element(By.XPATH, locators["login_button"]).click()
    if credentials == "locked":
        verify_message(driver, "locked_user_message")
    else:
        page_loads(driver, "Inventory")

def clicks(driver, page, element):
    locators = get_xpath(page)
    driver.find_element(By.XPATH, locators[element]).click()