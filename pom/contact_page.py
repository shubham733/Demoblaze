class ContactPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.demoblaze.com/")

    def submit_form(self, email, name, message):
        self.page.get_by_role("link", name="Contact").click()
        self.page.locator("#recipient-email").fill(email)
        self.page.get_by_label("Contact Email:").fill(name)
        self.page.get_by_label("Message:").fill(message)
        self.page.get_by_role("button", name="Send message").click()
