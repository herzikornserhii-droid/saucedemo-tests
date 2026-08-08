def test_add_to_cart(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    badge = page.locator("[data-test='shopping-cart-badge']")
    assert badge.inner_text() == "1"