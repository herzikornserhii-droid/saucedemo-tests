import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("username, password", [
    ("locked_out_user", "secret_sauce"),
    ("standard_user","wrong_password"),
    ("", "secret_sauce"),
])
def test_login_fails(page, username, password):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    error = page.locator("[data-test='error']")
    assert error.is_visible()