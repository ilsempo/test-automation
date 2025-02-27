import pytest
from steps.action_steps import login, add_products_to_cart, start_checkout, fill_form_with_data, finish_checkout
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
        start_checkout(driver)
        fill_form_with_data(driver, {
        "first_name_input": "first_name",
        "last_name_input" : "last_name",
        "postal_code_input" : "postal_code"
        })
        finish_checkout(driver)
        verify_message(driver, "success_buy_message")