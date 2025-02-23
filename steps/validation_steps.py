from selenium.webdriver.common.by import By
from utils.utils import get_xpath, get_message

def page_loads(driver, page):
    page_validators = get_xpath(page, validation=True)
    assert all(driver.find_element(By.XPATH, validator).is_displayed() for validator in page_validators)

def verify_message(driver, message):
    message = get_message(message)
    assert driver.find_element(By.XPATH, f"//*[text()='{message}']").is_displayed()