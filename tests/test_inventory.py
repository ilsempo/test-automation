import pytest
from steps.action_steps import login, user_sorts_by

@pytest.mark.inventory
class TestInventory:

    @pytest.mark.product_sorting_Az
    def test_product_sorting(self, driver):
        """
        Scenario: User sorts items in inventory with different criteria
        """
        login(driver)
        user_sorts_by(driver,"Inventory", "sort_za")