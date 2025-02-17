from selenium.webdriver.common.by import By
from functions.utils import get_user_info, get_xpath, get_message

user_info = get_user_info("valid")
cart_page_locators = get_xpath("Cart")
checkout_page_locators = get_xpath("Checkout")
checkout_page_validators = get_xpath("Checkout", validation=True)

def checkout(driver):
    driver.find_element(By.XPATH, cart_page_locators["checkout_button"]).click()
    assert all(driver.find_element(By.XPATH, element).is_displayed() for element in checkout_page_validators)
    print(checkout_page_locators["first_name_input"])
    driver.find_element(By.XPATH, checkout_page_locators["first_name_input"]).send_keys(user_info["first_name"])
    driver.find_element(By.XPATH, checkout_page_locators["last_name_input"]).send_keys(user_info["last_name"])
    driver.find_element(By.XPATH, checkout_page_locators["postal_code_input"]).send_keys(user_info["postal_code"])
    driver.find_element(By.XPATH, checkout_page_locators["continue_checkout"]).click()
    driver.find_element(By.ID, "finish").click()

def verify_success(driver):
    success_message = get_message("success_buy_message")
    print(success_message)
    assert driver.find_element(By.XPATH, f"//h2[contains(text(), '{success_message}')]").is_displayed()