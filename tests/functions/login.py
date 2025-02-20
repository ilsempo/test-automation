from selenium.webdriver.common.by import By
from functions.utils import get_xpath, get_user_info
from functions.page_validations import page_loads, verify_message

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