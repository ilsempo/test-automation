import yaml
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_data():
    with open("data/data.yaml", "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data

def get_website():
    with open("data/website.yaml", "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data
    
def get_xpath(page_name, validation=False):
    website = get_website()
    if not validation:
        page_locators = website["pages"][page_name]["locators"]
        xpaths = {key : value["XPATH"] for key, value in page_locators.items()}
    else:
        page_validation = website["pages"][page_name]["validation"]
        url = website["pages"][page_name]["url"]
        xpaths = (set(path["XPATH"] for path in page_validation.values() if "XPATH" in path), url)
    return xpaths

def get_user_info(user_type):
    data = get_data()
    return data["user"][user_type]

def get_message(key):
    data = get_data()
    message = data['message'][key]
    return message

def safe_find_element(driver, by, locator):
    try:
        elements = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((by, locator))
        )
        if not elements:
            raise NoSuchElementException()
        return elements if len(elements) > 1 else elements[0]
    except (TimeoutException, NoSuchElementException) as e:
        logging.error(f"\033[31m[find_element error] | Locator: {by}='{locator}'\nMessage: {e}\033[0m")
        raise

def logging_adjustments(step_name, args):
    basic_logging = f"\033[92m{step_name}\033[0m"
    if step_name == "user_sorts_by":
        basic_logging = f"\033[92m{step_name} \033[0m\033[36m-> {args[1]}\033[0m"
    logging.info(basic_logging)
    if step_name == "fill_form_with_data":
        data = args[0]
        max_key_lenght = max(len(key) for key in data)
        max_value_lenght = max(len(value) for value in data.values())
        for key, value in data.items():
            key_string = key.ljust(max_key_lenght)
            value_string = value.ljust(max_value_lenght)
            logging.info(f"\033[36m   | {key_string} -> {value_string} |\033[0m")

def log_step(func):
    def wrapper(driver, *args, **kwargs):
        step_name = func.__name__
        is_internal = kwargs.get("is_internal")
        try:
            func(driver, *args, **kwargs)
            if not is_internal:
                logging_adjustments(step_name, args)
        # except (TimeoutException, NoSuchElementException, WebDriverException) as e:
        #     logging.error(f"\033[31m{step_name} - Error with locator: {e}\033[0m")
        #     raise
        except Exception as e:
            if not is_internal:
                logging.error(f"\033[31m{step_name} - {str(e)}\033[0m")
            raise
    return wrapper