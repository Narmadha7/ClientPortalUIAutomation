from pages.LoginPage import LoginPage


def test_negative(browserInstance):
    driver = browserInstance

    loginpage = LoginPage(driver)
    loginpage.wrong_email_check("brainandbeauty.com", "Brain@1234")
    loginpage.wrong_pass_check("brainandbeauty@test.com", "Brain@12")