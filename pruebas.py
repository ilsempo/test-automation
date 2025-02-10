# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.saucedemo.com/")

# user_names = driver.find_element(By.XPATH, "//div[@id='login_credentials']")
# print(user_names.text.split("\n"))
# driver.quit()

dictionary = {'username_input': "//input[@id='user-name']", 'password_input': "//input[@id='password']", 'login_button': "//input[@id='login-button']"}

print(dictionary['username_input'])