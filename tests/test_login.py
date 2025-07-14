from pages.LoginPage import LoginPage


def test_login(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/client")
    driver.maximize_window()

    assert "client" in driver.current_url
    print("Title is:", driver.title)

    # object creation for LoginPage class
    login_page = LoginPage(driver)
    login_page.login()

    assert "dash" in driver.current_url
