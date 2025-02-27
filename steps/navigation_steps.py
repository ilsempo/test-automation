from selenium.webdriver.common.by import By
from utils.utils import get_xpath, log_step
from steps.validation_steps import page_loads

@log_step
def go_to_cart(driver):
    inventory_locators = get_xpath("Inventory")
    cart_element = driver.find_element(By.XPATH, inventory_locators["go_to_cart_icon"])
    cart_element.click()
    page_loads(driver, "Cart", is_internal=True)