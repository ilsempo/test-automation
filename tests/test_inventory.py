import pytest
from steps.action_steps import user_sorts_by, user_clicks
from steps.navigation_steps import login, go_to_cart
from steps.validation_steps import page_loads, element_present_in_page

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
    
    @pytest.mark.add_to_cart
    def test_user_add_product_to_cart(self, driver):
        """
        Scenario: User adds a random product to cart
        """
        login(driver)
        user_clicks(driver, "Inventory", "add_to_cart_buttons")
        go_to_cart(driver)
        element_present_in_page(driver, "Cart", "cart_item")