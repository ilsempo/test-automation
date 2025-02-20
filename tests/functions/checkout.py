from selenium.webdriver.common.by import By
from functions.utils import get_user_info, get_xpath, get_message
from functions.page_validations import page_loads

user_info = get_user_info("valid")
cart_page_locators = get_xpath("Cart")
checkout_page_locators = get_xpath("Checkout")

def checkout(driver):
    driver.find_element(By.XPATH, cart_page_locators["checkout_button"]).click()
    page_loads(driver, "Checkout")
    checkout_data = {
        "first_name_input": "first_name",
        "last_name_input" : "last_name",
        "postal_code_input" : "postal_code"
    }
    for locator, data in checkout_data.items():
        driver.find_element(By.XPATH, checkout_page_locators[locator]).send_keys(user_info[data])
    driver.find_element(By.XPATH, checkout_page_locators["continue_checkout"]).click()
    driver.find_element(By.ID, "finish").click()
