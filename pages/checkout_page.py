from pages.base import Base
from data.assertions import Assertions
from playwright.sync_api import Page


class CheckoutPage(Base):
    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    ZIP = "[data-test='postalCode']"
    CNT_BTN = "[data-test='continue']"
    FINISH_BTN = "[data-test='finish']"
    FINAL_TEXT = "//span[text()='Checkout: Complete!']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def checkout(self):
        self.input(self.FIRST_NAME, "Ivan")
        self.input(self.LAST_NAME, "Ivanov")
        self.input(self.ZIP, "123456")
        self.click(self.CNT_BTN)
        self.click(self.FINISH_BTN)
        self.assertions.have_text(self.FINAL_TEXT, "Checkout: Complete!", "no")
