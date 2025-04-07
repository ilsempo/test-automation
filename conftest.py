import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

def pytest_addoption(parser):
    parser.addoption(
        "--h","--headless", action="store_true", default=False, help="Run tests in headless mode"
    )

@pytest.fixture
def driver(request):
    chrome_options = Options()
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def print_test_name(request):
    logging.info(f"\033[90m>> Executing test: {request.node.name}\033[0m")