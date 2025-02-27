from selenium.webdriver.common.by import By
from utils.utils import get_xpath, get_user_info, log_step
from steps.validation_steps import page_loads, verify_message
import random

@log_step
def add_products_to_cart(driver):
    inventory_locators = get_xpath("Inventory")
    all_add_to_cart_buttons = driver.find_elements(By.XPATH, inventory_locators["add_to_cart_buttons"])
    random_add_quantity = random.randint(1, len(all_add_to_cart_buttons))
    for i in range(random_add_quantity):
        all_add_to_cart_buttons[i].click()

@log_step
def start_checkout(driver):
    cart_page_locators = get_xpath("Cart")
    driver.find_element(By.XPATH, cart_page_locators["checkout_button"]).click()
    page_loads(driver, "CheckoutOne", is_internal=True)

@log_step
def fill_form_with_data(driver, data: dict[str, str | int], user_type="valid"):
    user_info = get_user_info(user_type)
    checkout_page_locators = get_xpath("CheckoutOne")
    data_to_fill = data
    for locator, enter_data in data_to_fill.items():
        driver.find_element(By.XPATH, checkout_page_locators[locator]).send_keys(user_info[enter_data])

@log_step
def finish_checkout(driver):
    checkout_page_locators = get_xpath("CheckoutOne")
    checkout_page_two_locators= get_xpath("CheckoutTwo")
    driver.find_element(By.XPATH, checkout_page_locators["continue_checkout"]).click()
    page_loads(driver, "CheckoutTwo", is_internal=True)
    driver.find_element(By.XPATH, checkout_page_two_locators["finish_checkout"]).click()

@log_step
def login(driver, credentials="valid"):
    locators = get_xpath("Login")
    user_info = get_user_info(credentials)
    page_loads(driver, "Login", is_internal=True)
    driver.find_element(By.XPATH, locators["username_input"]).send_keys(user_info["username"])
    driver.find_element(By.XPATH, locators["password_input"]).send_keys(user_info["password"])
    driver.find_element(By.XPATH, locators["login_button"]).click()
    if credentials == "locked":
        verify_message(driver, "locked_user_message", is_internal=True)
    else:
        page_loads(driver, "Inventory", is_internal=True)

@log_step
def user_clicks(driver, page, element):
    locators = get_xpath(page)
    driver.find_element(By.XPATH, locators[element]).click()