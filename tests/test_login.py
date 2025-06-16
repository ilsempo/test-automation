import pytest
from steps.action_steps import logout, user_clicks
from steps.navigation_steps import login

@pytest.mark.regression
@pytest.mark.login
class TestLogin:

    @pytest.mark.login_valid
    def test_login_valid(self):
        """
        Scenario: User logs in successfully
        """
        login()

    @pytest.mark.login_invalid
    def test_login_invalid(self):
        """
        Scenario: Locked user fails logging in
        """
        login("locked")
    
    @pytest.mark.login_logout
    def test_user_logs_in_and_out(self, driver):
        """
        Scenario: User logs in and out
        """
        login()
        user_clicks("item_name")
        logout()
