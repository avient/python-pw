from pages.base import Base
from data.assertions import Assertions
from playwright.sync_api import Page


class InventoryPage(Base):
    ADD_TO_CARD = "button.btn"
    FOLLOW_TO_BASKET = "[id='shopping_cart_container']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def click_add_to_card(self):
        self.click_element_by_index(self.ADD_TO_CARD, 0)

    def click_go_to_basket(self):
        self.click(self.FOLLOW_TO_BASKET)
