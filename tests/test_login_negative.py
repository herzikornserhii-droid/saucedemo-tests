def test_login_wrong_password(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    error = page.locator("[data-test='error']")
    assert error.is_visible()