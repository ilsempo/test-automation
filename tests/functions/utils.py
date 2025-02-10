import csv
import yaml

def get_products():
    with open("products2.csv", "r", newline='', encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return [row["name"] for row in reader]

def get_data():
    with open("data.yaml", "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data

def get_website():
    with open("website.yaml", "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data
    
def get_xpath(page_name, validation=False):
    website = get_website()
    if not validation:
        page_locators = website["pages"][page_name]["locators"]
        xpath = {key : value["XPATH"] for key, value in page_locators.items()}
    else:
        page_validation = website["pages"][page_name]["validation"]
        xpath = set(path["XPATH"] for path in page_validation.values() if "XPATH" in path)
    return xpath

def get_user_info(user_type):
    data = get_data()
    return data["user"][user_type]

def get_message(key):
    data = get_data()
    xpath_message_constructor = f"//*[text()='{data["message"][key]}']"
    return xpath_message_constructor