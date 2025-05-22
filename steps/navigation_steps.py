from selenium.webdriver.common.by import By
from utils.utils import get_xpath, log_step, safe_find_element
from steps.validation_steps import page_loads, user_is_in_page

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