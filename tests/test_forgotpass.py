import time

from pages.ForgotPassPage import ForgotPassPage
from pages.LoginPage import LoginPage
from utils.screenshot_helper import take_screenshot


def test_forgotPass(browserInstance):
    driver = browserInstance

    forgot_page = ForgotPassPage(driver)
    loginpage = LoginPage(driver)
    loginpage.click_forgot_pass()
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
        take_screenshot(driver, "invalid_login_fail")
        raise



