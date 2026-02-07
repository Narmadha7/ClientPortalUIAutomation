import json

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.AccountCreateSuccessPage import AccountSuccess
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from utils import randomString

file_path = "C://Users//Narmukishore14//PycharmProjects//ClientPortalUIAutomation//data//register_data.json"
with open(file_path, 'r') as f:
    testdata = json.load(f)
    valid_data_list = testdata["valid_data"]
    invalid_data_list = testdata["invalid_data"]


@pytest.mark.usefixtures("selenium_driver")
class TestRegisterPage:

    def navigate_to_register_page(self):
        lp = LoginPage(self.driver)
        lp.click_register_link()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )
        return RegisterPage(self.driver)

    @pytest.mark.register
    @pytest.mark.positive
    @pytest.mark.parametrize("data", valid_data_list)
    def test_mandatory_field_register(self, data):
        register_page = self.navigate_to_register_page()
        assert register_page.is_firstname_displayed() is True
        register_page.enter_firstname(data["first_name"])
        assert register_page.is_lastname_displayed() is True
        register_page.enter_lastname(data["last_name"])
        assert register_page.is_email_displayed() is True
        unique_email = f"{data['email']}.{randomString.random_email_generate()}@gmail.com"
        register_page.enter_email(unique_email)
        assert register_page.is_phone_displayed() is True
        register_page.enter_phone(data["phone"])
        assert register_page.is_password_displayed() is True
        register_page.enter_password(data["password"])
        assert register_page.is_confirm_password_displayed() is True
        register_page.enter_confirm_password(data["confirm_password"])
        register_page.select_checkbox()
        register_page.click_submit()

    @pytest.mark.positive
    @pytest.mark.register
    @pytest.mark.parametrize("data", valid_data_list)
    def test_validate_success(self, data):
        self.test_mandatory_field_register(data)
        account_success_page = AccountSuccess(self.driver)
        assert "Account Created Successfully" in account_success_page.validate_success_msg()
        account_success_page.click_login()

    @pytest.mark.positive
    @pytest.mark.register
    @pytest.mark.parametrize("data", valid_data_list)
    def test_all_valid_register(self, data):
        register_page = self.navigate_to_register_page()
        register_page.enter_firstname(data["first_name"])
        register_page.enter_lastname(data["last_name"])
        unique_email = f"{data['email']}.{randomString.random_email_generate()}@gmail.com"
        register_page.enter_email(unique_email)
        register_page.enter_phone(data["phone"])
        register_page.select_occupation()
        register_page.select_gender()
        register_page.enter_password(data["password"])
        register_page.enter_confirm_password(data["confirm_password"])
        register_page.select_checkbox()
        register_page.click_submit()

    @pytest.mark.negative
    @pytest.mark.register
    def test_validate_error_msg(self):
        register_page = self.navigate_to_register_page()
        register_page.click_submit()
        assert "required" in register_page.empty_firstname_error()
        assert "required" in register_page.empty_email_error()
        assert "required" in register_page.empty_phone_error()
        assert "required" in register_page.empty_password_error()
        assert "required" in register_page.empty_confirm_password_error()
        assert "check above checkbox" in register_page.empty_age_checkbox_error()

    @pytest.mark.parametrize("data", invalid_data_list)
    def test_register_with_invalid_data(self, data):
        register_page = self.navigate_to_register_page()
        register_page.enter_firstname(data["first_name"])
        register_page.enter_lastname(data["last_name"])
        register_page.enter_email(data["email"])
        register_page.enter_phone(data["phone"])
        register_page.enter_password(data["password"])
        register_page.enter_confirm_password(data["confirm_password"])
        register_page.select_checkbox()
        register_page.click_submit()

        # Add assertions based on expected error messages for each invalid input
        if not data["first_name"]:
            assert "required" in register_page.empty_firstname_error()
        if "@" not in data["email"]:
            assert "Valid Email" in register_page.verify_email_invalid_error()
        if len(data["phone"]) < 10:
            assert "Number must be" in register_page.verify_phone_invalid_error()
        if data["password"] != data["confirm_password"]:
            assert "Password must match" in register_page.verify_password_mismatch_error()

    @pytest.mark.negative
    @pytest.mark.smoke
    def test_validate_placeholder(self):
        register_page = self.navigate_to_register_page()
        assert register_page.get_firstname_placeholder() == "First Name"
        assert register_page.get_lastname_placeholder() == "Last Name"
        assert register_page.get_email_placeholder() == "email@example.com"
        assert register_page.get_phone_placeholder() == "enter your number"
        assert register_page.get_password_placeholder() == "Passsword"
        assert register_page.get_confirm_password_placeholder() == "Confirm Passsword"

    @pytest.mark.negative
    @pytest.mark.smoke
    def test_ui_elements(self):
        register_page = self.navigate_to_register_page()
        assert register_page.firstname_label_check() == "First Name"
        assert register_page.lastname_label_check() == "Last Name"
        assert register_page.email_label_check() == "Email"
        assert register_page.phone_label_check() == "Phone Number"
        assert register_page.password_label_check() == "Password"
        assert register_page.confirm_password_label_check() == "Confirm Password"
        assert register_page.gender_label_check() == "Gender"
