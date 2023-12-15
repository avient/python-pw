import pytest
from pages.auth_page import Auth


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
        m = Auth(browser)
        m.user_login()
