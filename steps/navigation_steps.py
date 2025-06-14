from selenium.webdriver.common.by import By
from utils.utils import get_xpath, log_step, safe_find_element, get_user_info
from steps.validation_steps import page_loads, user_is_in_page, message_is_displayed
from steps.action_steps import user_clicks

@log_step
def go_to_cart(driver):
    inventory_locators = get_xpath("Inventory")
    cart_element = safe_find_element(driver, By.XPATH, inventory_locators["go_to_cart_icon"])
    cart_element.click()
    page_loads(driver, "Cart", is_internal=True)

@log_step
def finish_checkout(driver, credentials="valid"):
    checkout_page_locators = get_xpath("CheckoutOne")
    checkout_page_two_locators= get_xpath("CheckoutTwo")
    safe_find_element(driver, By.XPATH, checkout_page_locators["continue_checkout"]).click()
    if credentials == "problem":
        user_is_in_page(driver, "CheckoutOne", is_internal=True)
    else:
        page_loads(driver, "CheckoutTwo", is_internal=True)
        safe_find_element(driver, By.XPATH, checkout_page_two_locators["finish_checkout"]).click()

@log_step
def login(driver, credentials="valid"):
    locators = get_xpath("Login")
    user_info = get_user_info(credentials)
    page_loads(driver, "Login", is_internal=True)
    safe_find_element(driver, By.XPATH, locators["username_input"]).send_keys(user_info["username"])
    safe_find_element(driver, By.XPATH, locators["password_input"]).send_keys(user_info["password"])
    safe_find_element(driver, By.XPATH, locators["login_button"]).click()
    if credentials == "locked":
        message_is_displayed(driver, "locked_user_message", is_internal=True)
    else:
        page_loads(driver, "Inventory", is_internal=True)

@log_step
def user_access_page(driver, page_name, element):
    element_to_click = element
    user_clicks(driver, element_to_click, is_internal=True)
    page_loads(driver, page_name, is_internal=True)