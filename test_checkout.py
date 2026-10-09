
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout(driver):

    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for Products page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    # Add Backpack to cart
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    # Open cart
    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    # Click Checkout
    driver.find_element(
        By.ID, "checkout"
    ).click()

    # Enter customer information
    driver.find_element(
        By.ID, "first-name"
    ).send_keys("Abhishek")

    driver.find_element(
        By.ID, "last-name"
    ).send_keys("Pandey")

    driver.find_element(
        By.ID, "postal-code"
    ).send_keys("485001")

    # Continue
    driver.find_element(
        By.ID, "continue"
    ).click()

    # Verify Checkout Overview
    checkout_title = driver.find_element(
        By.CLASS_NAME, "title"
    ).text

    assert checkout_title == "Checkout: Overview"


    # Finish the order
    driver.find_element(By.ID, "finish").click()
    
# Verify order confirmation
    confirmation = driver.find_element(
    By.CLASS_NAME, "complete-header"
).text

    assert confirmation == "Thank you for your order!"
