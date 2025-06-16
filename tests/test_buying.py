import pytest
from steps.action_steps import add_products_to_cart, fill_form_with_data, user_clicks
from steps.navigation_steps import go_to_cart, finish_checkout, login
from steps.validation_steps import message_is_displayed, user_is_in_page

@pytest.mark.regression
@pytest.mark.buy
class TestBuying:

    @pytest.mark.buying_success
    def test_buying_success(self):
        """
        Scenario: User completes buying proccess successfully
        """
        login()
        add_products_to_cart()
        go_to_cart()
        user_clicks("checkout_button")
        fill_form_with_data({
        "first_name_input": "first_name",
        "last_name_input" : "last_name",
        "postal_code_input" : "postal_code"
        })
        finish_checkout()
        message_is_displayed("success_buy_message")

    @pytest.mark.buying_fail
    def test_buying_fail(self):
        """
        Scenario: User fails buying
        """
        login("problem")
        add_products_to_cart()
        go_to_cart()
        user_clicks("checkout_button")
        fill_form_with_data({
        "first_name_input": "first_name",
        "last_name_input" : "last_name",
        "postal_code_input" : "postal_code"
        }, "problem")
        finish_checkout("problem")
        message_is_displayed("last_name_missing")

    @pytest.mark.cancel_buying
    def test_cancel_buying(self):
        """
        Scenario: User cancels buying process
        """
        login()
        add_products_to_cart()
        go_to_cart()
        user_clicks("checkout_button")
        fill_form_with_data({
        "first_name_input": "first_name",
        "last_name_input" : "last_name",
        "postal_code_input" : "postal_code"
        })
        user_clicks("continue_checkout")
        user_clicks("cancel_button")
        user_is_in_page("Inventory")