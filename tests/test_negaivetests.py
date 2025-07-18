from pages.LoginPage import LoginPage


def test_negative(browserInstance):
    driver = browserInstance

    login_page = LoginPage(driver)
    login_page.wrong_email_check("brainandbeauty.com", "Brain@1234")
    login_page.wrong_pass_check("brainandbeauty@test.com", "Brain@12")
