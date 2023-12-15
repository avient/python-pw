from pages.base import Base
from data.constants import Constants
from data.assertions import Assertions
from playwright.sync_api import Page


class Auth(Base):
    USERNAME_INPUT = "[data-test = 'username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BTN = "[data-test='login-button']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self):
        self.open("")
        self.input(self.USERNAME_INPUT, Constants.login)
        self.input(self.PASSWORD_INPUT, Constants.password)
        self.click(self.LOGIN_BTN)
        self.assertion.check_URL("inventory.html", "Wrong URL")
