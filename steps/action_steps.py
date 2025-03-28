from selenium.webdriver.common.by import By
from utils.utils import get_xpath, get_user_info, log_step
from steps.validation_steps import page_loads, message_is_displayed, user_is_in_page
import random
import logging

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
def finish_checkout(driver, credentials="valid"):
    checkout_page_locators = get_xpath("CheckoutOne")
    checkout_page_two_locators= get_xpath("CheckoutTwo")
    driver.find_element(By.XPATH, checkout_page_locators["continue_checkout"]).click()
    if credentials == "problem":
        user_is_in_page(driver, "CheckoutOne", is_internal=True)
    else:
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
        message_is_displayed(driver, "locked_user_message", is_internal=True)
    else:
        page_loads(driver, "Inventory", is_internal=True)

@log_step
def user_clicks(driver, page, element, is_internal=False):
    locators = get_xpath(page)
    driver.find_element(By.XPATH, locators[element]).click()

@log_step
def user_sorts_by(driver, page, criteria):
    locators = get_xpath(page)
    user_clicks(driver, page, "sort_select", is_internal=True)
    user_clicks(driver, page, criteria, is_internal=True)
    item_names = driver.find_elements(By.XPATH, locators["item_name"])
    items = [item.text for item in item_names]
    if criteria == "sort_az":
        sorted_item_names = sorted(items)
    elif criteria == "sort_za":
        sorted_item_names = sorted(items, reverse=True)
    assert items == sorted_item_names