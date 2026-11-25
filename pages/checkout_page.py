class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.checkout_btn = page.locator("[data-test=checkout]")
        self.first = page.locator("[data-test=firstName]")
        self.last = page.locator("[data-test=lastName]")
        self.zip = page.locator("[data-test=postalCode]")
        self.continue_btn = page.locator("[data-test=continue]")
        self.finish_btn = page.locator("[data-test=finish]")
        self.confirmation = page.locator(".complete-header")

    def fill_details(self, first, last, zip_code):
        self.first.fill(first)
        self.last.fill(last)
        self.zip.fill(zip_code)
        self.continue_btn.click()
