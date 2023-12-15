import pytest
from pages.auth_page import Auth


@pytest.fixture(scope='class')
def user_login(browser):
    m = Auth(browser)
    m.user_login()
