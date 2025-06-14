import pytest
from steps.action_steps import logout, user_clicks
from steps.navigation_steps import login

@pytest.mark.login
class TestLogin:

    @pytest.mark.login_valid
    def test_login_valid(self, driver):
        """
        Scenario: User logs in successfully
        """
        login(driver)

    @pytest.mark.login_invalid
    def test_login_invalid(self, driver):
        """
        Scenario: Locked user fails logging in
        """
        login(driver, "locked")
    
    @pytest.mark.login_logout
    def test_user_logs_in_and_out(self, driver):
        """
        Scenario: User logs in and out
        """
        login(driver)
        user_clicks(driver, "item_name")
        logout(driver)
