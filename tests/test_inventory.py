import pytest
from steps.action_steps import user_sorts_by, user_clicks
from steps.navigation_steps import login, go_to_cart
from steps.validation_steps import page_loads, element_present_in_page, user_is_in_page

@pytest.mark.regression
@pytest.mark.inventory
class TestInventory:

    @pytest.fixture(autouse=True)
    def background(self):
        login()
        user_is_in_page("Inventory")

    @pytest.mark.product_sorting
    def test_product_sorting(self):
        """
        Scenario: User sorts items in inventory with different criteria
        """
        user_sorts_by("sort_za")
        user_sorts_by("sort_az")
        user_sorts_by("sort_hilo")
        user_sorts_by("sort_lohi")

    @pytest.mark.access_detail
    def test_user_access_to_item_detail(self):
        """
        Scenario: User enters a random item detail page
        """
        user_clicks("item_name")
        page_loads("Inventory-item")
    
    @pytest.mark.add_to_cart
    def test_user_add_product_to_cart(self):
        """
        Scenario: User adds a random product to cart
        """
        user_clicks("add_to_cart_buttons")
        go_to_cart()
        element_present_in_page("cart_item")