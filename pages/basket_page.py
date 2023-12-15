from pages.base import Base
from data.assertions import Assertions
from playwright.sync_api import Page


class BasketPage(Base):
    CHECKOUT_BTN = "#checkout"

    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)
