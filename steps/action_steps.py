from selenium.webdriver.common.by import By
from utils.utils import get_xpath, get_user_info, log_step, safe_find_element, safe_is_displayed, get_page
from steps.validation_steps import page_loads
from utils.context import context
import random
import logging

@log_step
def add_products_to_cart():
    inventory_locators = get_xpath(page="Inventory")
    all_add_to_cart_buttons = safe_find_element(By.XPATH, inventory_locators["add_to_cart_buttons"])
    random_add_quantity = random.randint(1, len(all_add_to_cart_buttons))
    for i in range(random_add_quantity):
        all_add_to_cart_buttons[i].click()

@log_step
def fill_form_with_data(data: dict[str, str | int], user_type="valid"):
    user_info = get_user_info(user_type)
    checkout_page_locators = get_xpath()
    data_to_fill = data
    for locator, enter_data in data_to_fill.items():
        safe_find_element(By.XPATH, checkout_page_locators[locator]).send_keys(user_info[enter_data])

@log_step
def logout():
    user_clicks("burguer_button", is_internal=True)
    user_clicks("logout_link", is_internal=True)
    page_loads("Login", is_internal=True)

@log_step
def user_clicks(element, is_internal=False):
    locators = get_xpath()
    element_to_click = safe_find_element(By.XPATH, locators[element])
    if isinstance(element_to_click, list):
        element_to_click = random.choice(element_to_click)
    if safe_is_displayed(element_to_click):
        element_to_click.click()

@log_step
def user_sorts_by(criteria):
    locators = get_xpath()
    user_clicks("sort_select", is_internal=True)
    user_clicks(criteria, is_internal=True)
    if criteria in ("sort_az", "sort_za"):
        item_names_or_prices = safe_find_element(By.XPATH, locators["item_name"])
        items = [item.text for item in item_names_or_prices]
    elif criteria in ("sort_lohi", "sort_hilo"):
        item_names_or_prices = safe_find_element(By.XPATH, locators["item_price"])
        items = [float(item.text.replace("$", "")) for item in item_names_or_prices]
    if criteria in ("sort_az", "sort_lohi"):
        sorted_items = sorted(items)
    elif criteria in ("sort_za", "sort_hilo"):
        sorted_items = sorted(items, reverse=True)
    assert items == sorted_items, f"Items not sorted as expected for {criteria}.\nActual: {items}\nExpected: {sorted_items}"

@log_step
def user_switches_to_tab(tab_to_switch):
    driver = context.driver
    tabs = driver.window_handles
    tabs_dict = {}
    for i, tab in enumerate(tabs):
        driver.switch_to.window(tab)
        url = driver.current_url.replace("https://", "")
        url = url.replace("www.", "")
        social_network = url.split(".")[0]
        tabs_dict[social_network] = i
    driver.switch_to.window(tabs[tabs_dict[tab_to_switch]])
    assert tab_to_switch in driver.current_url