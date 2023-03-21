class HomePage:
    def __init__(self, page):
        self.product_header = page.get_by_role("link", name="PRODUCT STORE")
        self.product_email = page.locator("text=Email: demo@blazemeter.com")