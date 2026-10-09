# SauceDemo Automation Testing Project

## Project Overview
This project automates the testing of the SauceDemo e-commerce web application using Selenium WebDriver and Python. Pytest is used to execute and manage test cases.

The project follows the Page Object Model (POM) design pattern to keep test scripts organized and maintainable.

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- pytest-html
- HTML Reports
- Page Object Model (POM)
- VS Code

## Features Tested
- Login with valid credentials
- Login with invalid credentials
- Login with empty credentials
- Product page verification
- Shopping cart testing
- Checkout functionality

## Project Structure
```text
SauceDemo_Automation/
├── assets/
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── conftest.py
├── test_login.py
├── test_products.py
├── test_cart.py
├── test_checkout.py
├── requirements.txt
├── README.md
└── report.html
```

## Installation and Setup

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Tests

Run all test cases:

```bash
python -m pytest -v
```

Generate an HTML test report:

```bash
python -m pytest -v --html=report.html --self-contained-html
```

Open `report.html` in a browser to view the test results.

## Test Results
The project currently contains six automated test cases. All six test cases passed during the latest local test execution.

Test results may vary depending on the application and test environment.

## Application Under Test
https://www.saucedemo.com/

## Author
Abhishek Pandey
