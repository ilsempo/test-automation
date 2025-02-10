from selenium.webdriver.common.by import By
from functions.utils import get_xpath, get_user_info, get_message

def login(driver, credentials="valid", return_result=False):
    validators = get_xpath("Login", validation=True)
    locators = get_xpath("Login")
    user_info = get_user_info(credentials)
    assert all(driver.find_element(By.XPATH, f"{validator}").is_displayed() for validator in validators)
    driver.find_element(By.XPATH, locators["username_input"]).send_keys(user_info["username"])
    driver.find_element(By.XPATH, locators["password_input"]).send_keys(user_info["password"])
    driver.find_element(By.XPATH, locators["login_button"]).click()
    if credentials == "valid":
        validators = get_xpath("Inventory", validation=True)
        assert all(driver.find_element(By.XPATH, validator).is_displayed() for validator in validators)
        if return_result:
            return True
    elif credentials == "locked":
        message = get_message("locked_user_message")
        elements = driver.find_elements(By.XPATH, message)
        assert len(elements) > 0 and elements[0].is_displayed()
        if return_result:
            return True