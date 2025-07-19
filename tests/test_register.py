import time

import pytest

from BasePage.BasePage import BaseTest
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from utils import randomString
from utils.customLogger import getLogger

@pytest.mark.usefixtures("selenium_driver")
class TestRegisterPage(BaseTest):

    def test_register(self):
        logger = getLogger()
        logger.info("Starting Login Test")
        logger.warning("Password field empty")

        self.driver.maximize_window()

        login_page = LoginPage(self.driver)
        logger.info("Browser initiated")
        login_page.click_register_link()
        time.sleep(3)

        register_page = RegisterPage(self.driver)
        register_page.validate_email()
        register_page.validate_password()
        register_page.validate_phone()
        register_page.validate_firstname()
        register_page.validate_lastname()
        register_page.validate_gender()
        register_page.validate_occupation()
        register_page.validate_confirm_password()
        register_page.enter_firstname("Vedha")
        register_page.enter_lastname("Raj")
        email = randomString.random_email_generate() + '@gmail.com'
        register_page.enter_email(email)
        register_page.enter_phone("1234567564")
        password = 'Brain@' + randomString.random_password_generate()
        register_page.enter_password(password)
        register_page.enter_confirm_password(password)
        register_page.select_occupation()
        register_page.select_gender()
        register_page.select_checkbox()
        register_page.checkbox_age_txt()
        register_page.click_submit()
        link_txt = register_page.verify_login_link
        print(link_txt)

        success_msg = register_page.verify_success_msg()
        print(success_msg)
        assert "register" in self.driver.current_url
        register_page.click_login_button()

        assert "login" in self.driver.current_url
