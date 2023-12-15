import pytest
from pages.basket_page import BasketPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestBuyProduct:
    def test_buy_product(self, browser):
        inventory_page = InventoryPage(browser)
        basket_page = BasketPage(browser)
        checkout_page = CheckoutPage(browser)

        inventory_page.click_add_to_card()
        inventory_page.click_go_to_basket()
        basket_page.click_checkout()
        checkout_page.checkout()
