import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_successful_login(browser):
    browser.get("https://your-web-app.com/login")
    username_input = browser.find_element_by_id("username")
    password_input = browser.find_element_by_id("password")
    login_button = browser.find_element_by_id("login-button")
    username_input.send_keys("your_valid_username")
    password_input.send_keys("your_valid_password")
    login_button.click()
    assert "Dashboard" in browser.title

def test_invalid_password(browser):
    browser.get("https://your-web-app.com/login")
    username_input = browser.find_element_by_id("username")
    password_input = browser.find_element_by_id("password")
    login_button = browser.find_element_by_id("login-button")
    username_input.send_keys("your_valid_username")
    password_input.send_keys("invalid_password")
    login_button.click()

    assert "Invalid credentials" in browser.page_source

def test_blank_fields(browser):
    browser.get("https://your-web-app.com/login")
    login_button = browser.find_element_by_id("login-button")
    login_button.click()
    assert "Please enter both username and password" in browser.page_source

def test_remembered_credentials(browser):
    browser.get("https://your-web-app.com/login")
    username_input = browser.find_element_by_id("username")
    password_input = browser.find_element_by_id("password")
    remember_checkbox = browser.find_element_by_id("remember-checkbox")
    login_button = browser.find_element_by_id("login-button")
    username_input.send_keys("your_valid_username")
    password_input.send_keys("your_valid_password")
    remember_checkbox.click()
    login_button.click()
    assert "Dashboard" in browser.title

def test_password_reset(browser):
    browser.get("https://your-web-app.com/login")
    username_input = browser.find_element_by_id("username")
    forgot_password_link = browser.find_element_by_id("forgot-password-link")
    username_input.send_keys("your_valid_username")
    forgot_password_link.click()
    password_input = browser.find_element_by_id("password")
    login_button = browser.find_element_by_id("login-button")
    password_input.send_keys("new_password")
    login_button.click()
    assert "Dashboard" in browser.title

def test_social_media_login(browser):
    browser.get("https://your-web-app.com/login")
    facebook_login_button = browser.find_element_by_id("facebook-login-button")
    facebook_login_button.click()
    assert "Dashboard" in browser.title
