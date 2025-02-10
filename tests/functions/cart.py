from selenium.webdriver.common.by import By
from functions.utils import get_products

def add_products_to_cart(driver):
    products = get_products()
    for product_name in products:
        driver.find_element(By.XPATH, f"//div[normalize-space()='{product_name}']/ancestor::div[@class='inventory_item']//button").click()

def go_to_cart(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()