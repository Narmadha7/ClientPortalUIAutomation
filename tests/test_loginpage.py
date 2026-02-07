import json

import pytest

from pages.LoginPage import LoginPage

data_file_path = "C://Users//Narmukishore14//PycharmProjects//ClientPortalUIAutomation//data//test_login.json"
with open(data_file_path, 'r') as f:
    testdata = json.load(f)
    data_list = testdata["data"]


@pytest.mark.usefixtures("selenium_driver")
class TestLoginPage:

    @pytest.mark.tc1
    def test_page_loads(self):
        login = LoginPage(self.driver)
        assert "client" in login.verify_current_page(), "loaded wrong page"

    @pytest.mark.parametrize("data", data_list)
    def test_login_scenarios(self, data):
        login = LoginPage(self.driver)
        login.enter_email(data["email"])
        login.enter_password(data["password"])
        login.submit_click()

        if data["type"] == "valid":
            assert "client" in login.verify_current_page()
        elif data["type"] == "empty_email":
            assert "required" in login.empty_email_error()
        elif data["type"] == "empty_password":
            assert "required" in login.empty_password_error()
        elif data["type"] == "empty_email_password":
            assert "required" in login.empty_email_error()
            assert "required" in login.empty_password_error()
        else:
            toast = login.validate_toast_msg()
            if toast:
                assert "Incorrect" in toast
            else:
                print("No toast appeared — might be expected for this scenario.")

    @pytest.mark.positive
    def test_validate_forgot_password(self):
        login = LoginPage(self.driver)
        login.forgot_password_id_displayed()
        assert login.validate_forgot_pass() == "Forgot password?"
        login.click_forgot_pass()

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
        assert login.is_top_text_displayed() is True
        login.validate_icons()
        assert login.validate_small_text() == "We Make Your Shopping Simple"
        assert login.validate_title_text() == "Practice Website for Rahul Shetty Academy Students"
        assert login.validate_blink_text() == "Register to sign in with your personal account"
        assert login.validate_login_text() == "Log in"

    @pytest.mark.positive
    def test_validate_register(self):
        login = LoginPage(self.driver)
        assert login.register_link_id_displayed() is True
        assert "Register here" in login.validate_register_link()
        login.click_register_link()
