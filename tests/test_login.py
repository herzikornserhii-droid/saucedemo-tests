def test_login(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.url == "https://www.saucedemo.com/inventory.html"