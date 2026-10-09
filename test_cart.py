from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_cart(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Add product
    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    # Verify cart
    cart_page = CartPage(driver)

    assert cart_page.get_cart_title() == "Your Cart"
