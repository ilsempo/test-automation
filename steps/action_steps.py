from selenium.webdriver.common.by import By
from utils.utils import get_xpath, get_user_info, log_step
from steps.validation_steps import page_loads, message_is_displayed
import random
import time

@log_step
def add_products_to_cart(driver):
    inventory_locators = get_xpath("Inventory")
    all_add_to_cart_buttons = driver.find_elements(By.XPATH, inventory_locators["add_to_cart_buttons"])
    random_add_quantity = random.randint(1, len(all_add_to_cart_buttons))
    for i in range(random_add_quantity):
        all_add_to_cart_buttons[i].click()

@log_step
def fill_form_with_data(driver, data: dict[str, str | int], user_type="valid"):
    user_info = get_user_info(user_type)
    checkout_page_locators = get_xpath("CheckoutOne")
    data_to_fill = data
    for locator, enter_data in data_to_fill.items():
        driver.find_element(By.XPATH, checkout_page_locators[locator]).send_keys(user_info[enter_data])

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

#FIXME
@log_step
def logout(driver):
    user_clicks(driver, "Inventory", "burguer_button", is_internal=True)
    time.sleep(10)
    user_clicks(driver, "Inventory", "logout_link", is_internal=True)
    page_loads(driver, "Login", is_internal=True)

@log_step
def user_clicks(driver, page, element, is_internal=False):
    locators = get_xpath(page)
    element_to_click = driver.find_elements(By.XPATH, locators[element])
    element_to_click = random.choice(element_to_click)
    element_to_click.click()

@log_step
def user_sorts_by(driver, page, criteria):
    locators = get_xpath(page)
    user_clicks(driver, page, "sort_select", is_internal=True)
    user_clicks(driver, page, criteria, is_internal=True)
    if criteria in ("sort_az", "sort_za"):
        item_names_or_prices = driver.find_elements(By.XPATH, locators["item_name"])
        items = [item.text for item in item_names_or_prices]
    elif criteria in ("sort_lohi", "sort_hilo"):
        item_names_or_prices = driver.find_elements(By.XPATH, locators["item_price"])
        items = [float(item.text.replace("$", "")) for item in item_names_or_prices]
    if criteria in ("sort_az", "sort_lohi"):
        sorted_items = sorted(items)
    elif criteria in ("sort_za", "sort_hilo"):
        sorted_items = sorted(items, reverse=True)
    assert items == sorted_items, f"Items not sorted as expected for {criteria}.\nActual: {items}\nExpected: {sorted_items}"