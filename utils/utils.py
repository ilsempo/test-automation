import yaml

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
