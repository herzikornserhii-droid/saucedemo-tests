class InventoryPage:
    def __init__(self, page):
        self.page = page
        
    def add_backpack_to_cart(self):
        self.page.click("[data-test='add-to-cart-sauce-labs-backpack']")
        
    def get_cart_count(self):
        return self.page.locator("[data-test='shopping-cart-badge']").inner_text()