from pages.products_page import ProductsPage


def test_products(driver):
    driver.get("https://www.saucedemo.com/")

    from pages.login_page import LoginPage

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    products_page = ProductsPage(driver)

    assert products_page.get_products_title() == "Products"
