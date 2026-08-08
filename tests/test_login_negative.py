from pages.login_page import LoginPage


def test_login_wrong_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")
    error = page.locator("[data-test='error']")
    assert error.is_visible()