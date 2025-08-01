import time

import pytest
from selenium.webdriver.common.by import By

from BasePage.BasePage import BaseTest
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("selenium_driver")
class TestLoginPage(BaseTest):

    # def setup_method(self, selenium_driver):
    #     self.driver = selenium_driver  # grab driver from fixture
    #     self.login = LoginPage(self.driver)  # for obj creation

    @pytest.mark.tc1
    def test_page_loads(self):
        login = LoginPage(self.driver)
        assert "client" in login.verify_current_page(), "loaded wrong page"

    @pytest.mark.positive
    def test_valid_login(self):
        login = LoginPage(self.driver)
        assert login.is_email_displayed() == bool("True")
        login.enter_email("brainandbeauty@test.com")
        assert login.is_password_displayed() == bool("True")
        login.enter_password("Brain@1234")
        assert login.is_button_enabled() == bool("True")
        login.submit_click()
        toast_msg = login.validate_toast_msg()
        print(toast_msg)
        # assert "Login" in toast_msg

    @pytest.mark.negative
    def test_invalid_login(self):
        login = LoginPage(self.driver)
        login.enter_email("brainandbeauty12@test.com")
        login.enter_password("Brain@12")
        login.submit_click()

    @pytest.mark.negative
    def test_invalid_email(self):
        login = LoginPage(self.driver)
        login.enter_email("brainandbeauty12@test.com")
        login.enter_password("Brain@1234")
        login.submit_click()

    @pytest.mark.negative
    def test_invalid_password(self):
        login = LoginPage(self.driver)
        login.enter_email("brainandbeauty@test.com")
        login.enter_password("Brain@12")
        login.submit_click()

    @pytest.mark.negative
    def test_invalid_email_password(self):
        login = LoginPage(self.driver)
        login.enter_email("brainandbeauty123@test.com")
        login.enter_password("Brain@12")
        login.submit_click()

    @pytest.mark.negative
    def test_empty_email(self):
        login = LoginPage(self.driver)
        login.enter_password("Brain@1234")
        login.submit_click()
        assert "required" in login.empty_email_error()

    @pytest.mark.negative
    def test_empty_password(self):
        login = LoginPage(self.driver)
        login.enter_email("brainandbeauty@test.com")
        login.submit_click()
        assert "required" in login.empty_password_error()

    @pytest.mark.positive
    def test_validate_forgot_password(self):
        login = LoginPage(self.driver)
        login.forgot_password_id_displayed()
        assert login.validate_forgot_pass() == "Forgot password?"
        login.click_forgot_pass()

    # @pytest.mark.pos
    # def test_keyboard_action(self):
    #     login = LoginPage(self.driver)
    #     login.navigate_using_keyboard("brainandbeauty@test.com")
    #     time.sleep(5)

    @pytest.mark.smoke
    def test_validate_placeholder(self):
        login = LoginPage(self.driver)
        assert login.get_email_placeholder() == "email@example.com"
        assert login.get_password_placeholder() == "enter your passsword"

    @pytest.mark.smoke
    def test_ui_elements(self):
        login = LoginPage(self.driver)
        assert login.email_label_check() == "Email"
        assert login.password_label_check() == "Password"
        assert login.login_button_text() == "Login"
        assert login.is_top_text_displayed() == bool("True")
        login.validate_icons()
        assert login.validate_small_text() == "We Make Your Shopping Simple"
        assert login.validate_title_text() == "Practice Website for Rahul Shetty Academy Students"
        assert login.validate_blink_text() == "Register to sign in with your personal account"
        assert login.validate_login_text() == "Log in"

    @pytest.mark.positive
    def test_validate_register(self):
        login = LoginPage(self.driver)
        assert login.register_link_id_displayed() == bool("True")
        assert "Register here" in login.validate_register_link()
        login.click_register_link()

    # @pytest.mark.positive
    # def test_validate_register(self):
    #     login = LoginPage(self.driver)
    #     assert login.register_link_id_displayed() == bool("True")
    #     assert "Register here" in login.validate_register_link()
    #     login.click_register_link()





