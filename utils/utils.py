import yaml
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.context import context
import time
import log_handler

def get_data():
    with open("data/data.yaml", "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data

def get_website():
    with open("data/website.yaml", "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data

def get_xpath(page=None, validation=False):
    website = get_website()
    page_name = page or get_page() or "Login"
    if not validation:
        page_locators = website["pages"][page_name]["locators"]
        xpaths = {key : value["XPATH"] for key, value in page_locators.items()}
    else:
        page_validation = website["pages"][page_name]["validation"]
        url = website["pages"][page_name]["url"]
        xpaths = (set(path["XPATH"] for path in page_validation.values() if "XPATH" in path), url)
    return xpaths

def get_page():
    driver = context.driver
    url = driver.current_url
    page = url.split("/")[-1].split("?")[0].split(".")[0].capitalize()
    return page

def get_user_info(user_type):
    data = get_data()
    return data["user"][user_type]

def get_message(key):
    data = get_data()
    message = data['message'][key]
    return message

def safe_find_element(by, locator):
    driver = context.driver
    try:
        elements = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((by, locator))
        )
        return elements if len(elements) > 1 else elements[0]
    except (TimeoutException, NoSuchElementException) as e:
        logging.error(f"\033[31m[find_element error] | Locator: {by}='{locator}'\nMessage: {e}\033[0m")
        raise

def safe_is_displayed(element, max_retries = 3, delay = 0.5):
    retries = 0
    while retries < max_retries:
        try:
            if element.is_displayed():
                return True
        except (StaleElementReferenceException, NoSuchElementException) as e:
            logging.info(f"{type(e).__name__} - retrying...")
        time.sleep(delay)
        retries += 1
    return False

def logging_adjustments(step_name, args):
    if step_name in log_handler.step_handlers:
        log_handler.step_handlers[step_name](args, step_name)
    else:
        log_handler.log_default(step_name)

def log_step(func):
    def wrapper(*args, **kwargs):
        step_name = func.__name__
        is_internal = kwargs.get("is_internal")
        try:
            func(*args, **kwargs)
            if not is_internal:
                logging_adjustments(step_name, args)
        except Exception as e:
            if not is_internal:
                logging.error(f"\033[31m{step_name} - {str(e)}\033[0m")
            raise
    return wrapper