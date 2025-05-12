import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import logging

def pytest_addoption(parser):
    parser.addoption(
        "-H", "--headless", action="store_true", default=False, help="Run tests in headless mode"
    )
    parser.addoption(
        "-B", "--browser", action="store", default="chrome", help="Specify browser: chrome or firefox"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == 'chrome':
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("-private-window")
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def print_test_name(request):
    logging.info(f"\033[90m>> Executing test: {request.node.name}\033[0m")