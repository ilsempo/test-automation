import pytest
from functions.login import login

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
