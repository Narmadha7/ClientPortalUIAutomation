import time
import pytest

from pages.ForgotPassPage import ForgotPassPage
from pages.LoginPage import LoginPage
from utils import randomString

@pytest.mark.usefixtures("selenium_driver")
class TestForgotPassword:

    def navigate_to_forgot_pass_page(self):
        login_page = LoginPage(self.driver)
        login_page.click_forgot_pass()
        return ForgotPassPage(self.driver)


    @pytest.mark.positive
    def test_forgotPass(self):
        forgot_page = self.navigate_to_forgot_pass_page()
        assert forgot_page.email_is_displayed() is True, "Email field not displayed"
        forgot_page.enter_email("brainandbeauty@test.com")
        assert forgot_page.password_is_displayed() is True, "Password field not displayed"
        assert forgot_page.con_password_is_displayed() is True, "Confirm Password field not displayed"
        password = randomString.random_password_generate() + '#'
        forgot_page.enter_password(password)
        forgot_page.enter_confirm_password(password)
        forgot_page.click_submit()
        time.sleep(4)

    @pytest.mark.positive
    def test_ui_elements(self):
        forgot_page = self.navigate_to_forgot_pass_page()
        assert forgot_page.email_label() ==  "Email"
        assert forgot_page.password_label() == "Password"
        assert forgot_page.con_password_label() == "Confirm Password"

    @pytest.mark.positive
    def test_placeholder(self):
        forgot_page = self.navigate_to_forgot_pass_page()
        assert forgot_page.email_placeholder() == "Enter your email address"
        assert forgot_page.password_placeholder() == "Passsword"
        assert forgot_page.con_password_placeholder() == "Confirm Passsword"



        # try:
        #     assert "login" in self.driver.current_url
        # except AssertionError:
        #     take_screenshot(self.driver, "login_fail")
