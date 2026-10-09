from selenium.webdriver.common.by import By


class CartPage:

    cart_title = (By.CLASS_NAME, "title")
    checkout_button = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_title(self):
        return self.driver.find_element(*self.cart_title).text

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()