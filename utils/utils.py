import yaml
import logging

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

def log_step(func):
    def wrapper(driver, *args, **kwargs):
        step_name = func.__name__
        is_internal = kwargs.get("is_internal")
        try:
            func(driver, *args, **kwargs)
            if not is_internal:
                logging.info(f"\033[92m{step_name}\033[0m")
                if step_name == "fill_form_with_data":
                    data = args[0]
                    for key, value in data.items():
                        logging.info(f"\033[36m| {key} | {value} |\033[0m")
        except Exception as e:
            if not is_internal:
                logging.error(f"\033[31m{step_name} - {str(e)}\033[0m")
            raise e
    return wrapper