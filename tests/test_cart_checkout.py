import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_inventory_has_six_products(logged_in):
    expect(logged_in.items).to_have_count(6)


@pytest.mark.regression
def test_add_item_updates_cart_badge(logged_in):
    logged_in.add_to_cart("sauce-labs-backpack")
    expect(logged_in.cart_badge).to_have_text("1")


@pytest.mark.regression
def test_end_to_end_purchase(page, logged_in, checkout):
    logged_in.add_to_cart("sauce-labs-backpack")
    logged_in.cart_link.click()
    checkout.checkout_btn.click()
    checkout.fill_details("Test", "User", "462001")
    checkout.finish_btn.click()
    expect(checkout.confirmation).to_have_text("Thank you for your order!")
