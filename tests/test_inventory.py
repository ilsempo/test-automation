import pytest
from steps.action_steps import user_sorts_by, user_clicks
from steps.navigation_steps import login
from steps.validation_steps import page_loads

@pytest.mark.inventory
class TestInventory:

    @pytest.mark.product_sorting
    def test_product_sorting(self, driver):
        """
        Scenario: User sorts items in inventory with different criteria
        """
        login(driver)
        user_sorts_by(driver, "Inventory", "sort_za")
        user_sorts_by(driver, "Inventory", "sort_az")
        user_sorts_by(driver, "Inventory", "sort_hilo")
        user_sorts_by(driver, "Inventory", "sort_lohi")

    @pytest.mark.access_detail
    def test_user_access_to_item_detail(self, driver):
        """
        Scenario: User enters a random item detail page
        """
        login(driver)
        user_clicks(driver, "Inventory", "item_name")
        page_loads(driver, "InventoryDetail")