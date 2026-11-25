class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_to_cart(self, product_slug):
        self.page.locator(f"[data-test=add-to-cart-{product_slug}]").click()
