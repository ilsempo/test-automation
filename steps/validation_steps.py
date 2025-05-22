from selenium.webdriver.common.by import By
from utils.utils import get_xpath, get_message, log_step, safe_find_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@log_step
def page_loads(driver, page, is_internal=False):
    page_validators = get_xpath(page, validation=True)
    for validator in page_validators[0]:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, validator)))

@log_step
def message_is_displayed(driver, message, is_internal=False):
    message = get_message(message)
    assert safe_find_element(driver, By.XPATH, f"//*[text()='{message}']").is_displayed()

@log_step
def user_is_in_page(driver, page, is_internal=False):
    url = get_xpath(page, validation=True)
    current_url = driver.current_url
    assert url[1] in current_url