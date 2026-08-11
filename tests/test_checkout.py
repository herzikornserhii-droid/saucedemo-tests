from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_checkout(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_backpack_to_cart()
    
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.open_cart()
    checkout_page.start_checkout()
    checkout_page.fill_info("John", "Doe", "12345")
    checkout_page.finish()
    
    assert checkout_page.get_confirmation_message() == "Thank you for your order!"