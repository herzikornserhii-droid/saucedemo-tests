class CheckoutPage:
    def __init__(self, page):
        self.page = page
        
    def open_cart(self):
        self.page.click("[data-test='shopping-cart-link']")
        
    def start_checkout(self):
        self.page.click("[data-test='checkout']")
        
    def fill_info(self, first_name, last_name, zip_code):
        self.page.fill("[data-test='firstName']", first_name)
        self.page.fill("[data-test='lastName']", last_name)
        self.page.fill("[data-test='postalCode']", zip_code)
        self.page.click("[data-test='continue']")
        
    def finish(self):
        self.page.click("[data-test='finish']")
        
    def get_confirmation_message(self):
        return self.page.locator("[data-test='complete-header']").inner_text()