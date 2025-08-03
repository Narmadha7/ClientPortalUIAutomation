import time

import pytest

from pages.AccountCreateSuccessPage import AccountSuccess
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from utils import randomString


@pytest.mark.usefixtures("selenium_driver")
class TestRegisterPage:

    @pytest.mark.register
    @pytest.mark.positive
    def test_mandatory_field_register(self):
        lp = LoginPage(self.driver)
        lp.click_register_link()
        time.sleep(5)
        register_page = RegisterPage(self.driver)
        assert register_page.is_firstname_displayed() == bool("True")
        register_page.enter_firstname("Vedha")
        assert register_page.is_lastname_displayed() == bool("True")
        register_page.enter_lastname("Raj")
        assert register_page.is_email_displayed() == bool("True")
        email = randomString.random_email_generate() + '@gmail.com'
        register_page.enter_email(email)
        assert register_page.is_phone_displayed() == bool("True")
        register_page.enter_phone("1234567564")
        assert register_page.is_password_displayed() == bool("True")
        register_page.enter_password("Brain#143")
        assert register_page.is_confirm_password_displayed() == bool("True")
        register_page.enter_confirm_password("Brain#143")
        register_page.select_checkbox()
        register_page.click_submit()

    @pytest.mark.positive
    @pytest.mark.register
    def test_validate_success(self):
        self.test_mandatory_field_register()
        account_success_page = AccountSuccess(self.driver)
        assert "Account Created Successfully" in account_success_page.validate_success_msg()
        account_success_page.click_login()

    @pytest.mark.positive
    @pytest.mark.register
    def test_all_valid_register(self):
        lp = LoginPage(self.driver)
        lp.click_register_link()
        time.sleep(5)
        register_page = RegisterPage(self.driver)
        register_page.enter_firstname("Vedha")
        register_page.enter_lastname("Raj")
        email = randomString.random_email_generate() + '@gmail.com'
        register_page.enter_email(email)
        register_page.enter_phone("1234567564")
        register_page.select_occupation()
        register_page.select_gender()
        register_page.enter_password("Brain#143")
        register_page.enter_confirm_password("Brain#143")
        register_page.select_checkbox()
        register_page.click_submit()

    @pytest.mark.negative
    @pytest.mark.register
    def test_validate_error_msg(self):
        lp = LoginPage(self.driver)
        lp.click_register_link()
        time.sleep(5)
        register_page = RegisterPage(self.driver)
        register_page.click_submit()
        assert "required" in register_page.empty_firstname_error()
        assert "required" in register_page.empty_email_error()
        assert "required" in register_page.empty_phone_error()
        assert "required" in register_page.empty_password_error()
        assert "required" in register_page.empty_confirm_password_error()
        assert "check above checkbox" in register_page.empty_age_checkbox_error()

    @pytest.mark.negative
    @pytest.mark.register
    def test_password_checks(self):
        lp = LoginPage(self.driver)
        lp.click_register_link()
        time.sleep(5)
        register_page = RegisterPage(self.driver)
        register_page.enter_password("Brain#143")
        register_page.enter_confirm_password("Brain#1434")
        register_page.click_submit()
        time.sleep(3)
        assert "Password must match" in register_page.verify_password_mismatch_error()

    @pytest.mark.negative
    @pytest.mark.smoke
    def test_validate_placeholder(self):
        lp = LoginPage(self.driver)
        lp.click_register_link()
        time.sleep(5)
        register_page = RegisterPage(self.driver)
        assert register_page.get_firstname_placeholder() == "First Name"
        assert register_page.get_lastname_placeholder() == "Last Name"
        assert register_page.get_email_placeholder() == "email@example.com"
        assert register_page.get_phone_placeholder() == "enter your number"
        assert register_page.get_password_placeholder() == "Passsword"
        assert register_page.get_confirm_password_placeholder() == "Confirm Passsword"

    @pytest.mark.negative
    @pytest.mark.smoke
    def test_ui_elements(self):
        lp = LoginPage(self.driver)
        lp.click_register_link()
        time.sleep(5)
        register_page = RegisterPage(self.driver)
        assert register_page.firstname_label_check() == "First Name"
        assert register_page.lastname_label_check() == "Last Name"
        assert register_page.email_label_check() == "Email"
        assert register_page.phone_label_check() == "Phone Number"
        assert register_page.password_label_check() == "Password"
        assert register_page.confirm_password_label_check() == "Confirm Password"
        assert register_page.gender_label_check() == "Gender"
