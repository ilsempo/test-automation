import pytest
from functions.login import login
from functions.cart import add_products_to_cart, go_to_cart
from functions.checkout import checkout, verify_success

@pytest.mark.buy
def test_buying_process(driver):
    login(driver)
    add_products_to_cart(driver)
    go_to_cart(driver)
    checkout(driver)
    assert verify_success(driver)