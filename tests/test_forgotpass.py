import time
import pytest

from pages.ForgotPassPage import ForgotPassPage
from pages.LoginPage import LoginPage
from utils.screenshot_file import take_screenshot

class TestForgotPassword:
    def test_forgotPass(browserInstance):
        driver = browserInstance
        print(pytest.browser)

        forgot_page = ForgotPassPage(driver)
        login_page = LoginPage(driver)
        login_page.click_forgot_pass()
        forgot_page.login()
        forgot_page.validate_email()
        forgot_page.validate_password()
        forgot_page.validate_confirm_password()
        forgot_page.validate_login_link()
        forgot_page.validate_register_link()
        forgot_page.click_submit()
        time.sleep(4)

        try:
            assert "login" in driver.current_url
        except AssertionError:
            take_screenshot(driver, "login_fail")
