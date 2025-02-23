import pytest
from steps.action_steps import login, add_products_to_cart, checkout
from steps.navigation_steps import go_to_cart
from steps.validation_steps import verify_message

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