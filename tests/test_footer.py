import pytest
from steps.navigation_steps import login
from steps.action_steps import logout, user_clicks

#FIXME
@pytest.mark.footer
class TestFooterLinks:

    @pytest.mark.footer_links
    def test_footer_links(self, driver):
        login(driver)
