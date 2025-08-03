import time
import pytest

from pages.ForgotPassPage import ForgotPassPage
from pages.LoginPage import LoginPage

@pytest.mark.usefixtures("selenium_driver")
class TestForgotPassword:

    @pytest.mark.positive
    def test_forgotPass(self):
        login_page = LoginPage(self.driver)
        login_page.click_forgot_pass()
        forgot_page = ForgotPassPage(self.driver)
        forgot_page.enter_email("brainandbeauty@test.com")
        forgot_page.enter_password("Brain@1234")
        time.sleep(4)


        # try:
        #     assert "login" in self.driver.current_url
        # except AssertionError:
        #     take_screenshot(self.driver, "login_fail")
