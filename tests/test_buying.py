import pytest
from functions.login import login
from functions.cart import add_products_to_cart, go_to_cart
from functions.checkout import checkout
from functions.page_validations import verify_message

@pytest.mark.buy
class TestBuying:

    @pytest.mark.buying_success
    def test_buying_process(self, driver):
        """
        Scenario: User completes buying proccess successfully
        """
        login(driver)
        add_products_to_cart(driver)
        go_to_cart(driver)
        checkout(driver)
        verify_message(driver, "success_buy_message")