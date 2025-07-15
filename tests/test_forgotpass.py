from pages.ForgotPassPage import ForgotPassPage


def test_forgotPass(browserInstance):
    driver = browserInstance

    forgot_page = ForgotPassPage(driver)
    forgot_page.click_forgot_pass()
    forgot_page.login()
    forgot_page.validate_email()
    forgot_page.validate_password()
    forgot_page.validate_confirm_password()

