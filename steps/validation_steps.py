from selenium.webdriver.common.by import By
from utils.utils import get_xpath, get_message, log_step
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

@log_step
def page_loads(driver, page, is_internal=False):
    page_validators = get_xpath(page, validation=True)
    for validator in page_validators[0]:
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, validator)))
        except (TimeoutException, NoSuchElementException, WebDriverException) as e:
            print(f"there was an error with locator {validator}, error: {e}")
            raise
@log_step
def verify_message(driver, message, is_internal=False):
    message = get_message(message)
    assert driver.find_element(By.XPATH, f"//*[text()='{message}']").is_displayed()

@log_step
def user_is_in_page(driver, page):
    url = get_xpath(page, validation=True)
    current_url = driver.current_url
    assert url[1] in current_url