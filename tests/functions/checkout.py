from selenium.webdriver.common.by import By
from functions.utils import get_user_info

def checkout(driver):
    user_info = get_user_info("valid")
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys(user_info["first_name"])
    driver.find_element(By.ID, "last-name").send_keys(user_info["last_name"])
    driver.find_element(By.ID, "postal-code").send_keys(user_info["postal_code"])
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

def verify_success(driver):
    text = "Thank you for your order!"
    success_message = driver.find_element(By.XPATH, f"//h2[contains(text(), '{text}')]")
    return success_message.is_displayed()