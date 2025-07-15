from pages.LoginPage import LoginPage


def test_login(browserInstance):
    driver = browserInstance

    # object creation for LoginPage class
    login_page = LoginPage(driver)
    login_page.login()
    login_page.top_text()
    login_page.validate_icons()
    login_page.validate_page_texts_and_ui()
    login_page.valid_email_check()
    login_page.valid_password_check()
    link = login_page.validate_forgot_pass()
    login_page.validate_register_link()
    login_page.submit_check()

    assert "password-new" in driver.current_url
