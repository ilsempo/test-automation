from selenium.webdriver.common.by import By
from utils.utils import get_xpath, get_message, log_step, safe_find_element, get_url
from utils.context import context
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@log_step
def page_loads(page_name, is_internal=False):
    driver = context.driver
    page_validators = get_xpath(page_name, validation=True)
    for validator in page_validators[0]:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, validator)))

@log_step
def message_is_displayed(message, is_internal=False):
    message = get_message(message)
    assert safe_find_element(By.XPATH, f"//*[text()='{message}']").is_displayed()

@log_step
def user_is_in_page(page_name, is_internal=False):
    driver = context.driver
    url = get_xpath(page_name, validation=True)
    current_url = driver.current_url
    assert url[1] in current_url

@log_step
def element_present_in_page(locator, is_internal=False):
    locators = get_xpath()
    assert safe_find_element(By.XPATH, locators[locator]).is_displayed()

@log_step
def new_tab_appears():
    original_tabs = context.original_tabs
    driver = context.driver
    new_tabs = driver.window_handles
    assert len(new_tabs) > len(original_tabs)
    for tab in new_tabs:
        if tab not in original_tabs:
            driver.switch_to.window(tab)
            WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete" 
            and d.title.strip() != "")
            driver.switch_to.window(original_tabs[0])

@log_step
def validate_external_url(url_to_validate):
    driver = context.driver
    url = get_url(url_to_validate)
    assert driver.current_url == url