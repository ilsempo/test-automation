from selenium.webdriver.common.by import By
from utils.utils import get_xpath, get_message
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

def page_loads(driver, page):
    page_validators = get_xpath(page, validation=True)

    for validator in page_validators[0]:
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, validator)))
        except (TimeoutException, NoSuchElementException, WebDriverException) as e:
            print(f"there was an error with locator {validator}, error: {e}")
            raise


def verify_message(driver, message):
    message = get_message(message)
    assert driver.find_element(By.XPATH, f"//*[text()='{message}']").is_displayed()

def is_in_page(driver, page):
    url = get_xpath(page, validation=True)
    current_url = driver.current_url
    print(url[0], current_url)