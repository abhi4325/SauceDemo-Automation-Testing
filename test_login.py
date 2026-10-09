from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Verify successful login
    products_title = driver.find_element(
        By.CLASS_NAME, "title"
    ).text

    assert products_title == "Products"


def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("wrong_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    # Verify invalid login error
    error_message = driver.find_element(
        By.CSS_SELECTOR, "h3[data-test='error']"
    ).text

    assert "Username and password do not match" in error_message


def test_empty_login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    # Click login without entering username/password
    login_page.click_login()

    # Verify empty login error
    error_message = driver.find_element(
        By.CSS_SELECTOR, "h3[data-test='error']"
    ).text

    assert "Username is required" in error_message
