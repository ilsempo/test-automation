import pytest
from steps.navigation_steps import login
from steps.validation_steps import new_tab_appears, validate_external_url
from steps.action_steps import user_clicks, user_switches_to_tab

@pytest.mark.regression
@pytest.mark.footer
class TestFooterLinks:

    @pytest.mark.parametrize(
        "locator, social_network, data", [
            ("social_facebook", "facebook", "facebook_saucelabs"),
            ("social_linkedin", "linkedin", "linkedin_saucelabs"),
            ("social_twitter", "x", "twitter_saucelabs")
        ]
    )

    @pytest.mark.footer_links
    def test_footer_links(self, locator, social_network, data):
        """
        Scenario: User tries all sauce labs social network links
        """
        login()
        user_clicks(locator)
        new_tab_appears()
        user_switches_to_tab(social_network)
        validate_external_url(data)