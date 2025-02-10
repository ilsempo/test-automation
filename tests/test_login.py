import pytest
from functions.login import login


@pytest.mark.login
class TestLogin:

    @pytest.mark.login_valid
    def test_login_valid(self, driver):
        login(driver, return_result=True)

    @pytest.mark.login_invalid
    def test_login_invalid(self, driver):
        login(driver, "locked", return_result=True)
