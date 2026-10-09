from selenium.webdriver.common.by import By


class CheckoutPage:

    checkout_title = (By.CLASS_NAME, "title")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    confirmation_message = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def get_checkout_title(self):
        return self.driver.find_element(*self.checkout_title).text

    def enter_customer_details(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()

    def get_confirmation_message(self):
        return self.driver.find_element(*self.confirmation_message).text