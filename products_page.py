from selenium.webdriver.common.by import By


class ProductsPage:

    products_title = (By.CLASS_NAME, "title")
    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def get_products_title(self):
        return self.driver.find_element(*self.products_title).text

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()