import pytest
from steps.action_steps import login

@pytest.mark.inventory
class TestInventory:

    @pytest.mark.product_sorting
    def product_sorting(self, driver):
        login(driver)
        