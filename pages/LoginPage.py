import time

from selenium.webdriver.common.by import By

from pages.ForgotPassPage import ForgotPassPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email = (By.ID, "userEmail")
        self.password = (By.ID, "userPassword")
        self.submit = (By.ID, "login")
        self.label_email = (By.XPATH, "//label[@for='email']")
        self.label_password = (By.XPATH, "//label[@for='password']")
        self.mail_top_text = (By.XPATH, "//div[@class='top-tab']/span[1]/a")
        self.top_icons =(By.CSS_SELECTOR, ".fa")
        self.small_text = (By.XPATH, "//h3[text()='We Make Your Shopping Simple']")
        self.title_text = (By.XPATH, "(//h1[@class='title'])[1]")
        self.blink_text = (By.CSS_SELECTOR, ".blink_me")
        self.login_title = (By.CSS_SELECTOR, ".login-title")
        self.page_title = ()
        self.forgot_pass = (By.XPATH, "//a[text()='Forgot password?']")
        self.register_link = (By.CSS_SELECTOR, ".login-wrapper p")

    def valid_email_check(self):
        assert self.driver.find_element(*self.label_email).text.title() == "Email"
        email = self.driver.find_element(*self.email)
        assert email.is_displayed()
        assert email.get_attribute("placeholder") == "email@example.com"
        email.send_keys("brainandbeauty@test.com")


    def valid_password_check(self):
        assert self.driver.find_element(*self.label_password).text.title() == "Password"
        password = self.driver.find_element(*self.password)
        assert password.is_displayed()
        assert password.get_attribute("placeholder") == "enter your passsword"
        password.send_keys("Brain@123")


    def submit_check(self):
        submit_button = self.driver.find_element(*self.submit)
        assert submit_button.is_enabled()
        submit_button.click()
        time.sleep(3)


    def top_text(self):
        mail_text = self.driver.find_element(*self.mail_top_text)
        assert mail_text.is_displayed()

    def validate_icons(self):
        icons = self.driver.find_elements(*self.top_icons)
        assert len(icons) >= 4

        for i, icon in enumerate(icons[:4]):
            href = icon.find_element(By.XPATH, "..").get_attribute("href")
            print(f"{icon.get_attribute('class')} = {href}")

    def validate_page_texts_and_ui(self):
        assert self.driver.find_element(*self.small_text).text == "We Make Your Shopping Simple"
        assert self.driver.find_element(*self.title_text).text == "Practice Website for Rahul Shetty Academy Students"
        assert self.driver.find_element(*self.blink_text).text == "Register to sign in with your personal account"
        assert self.driver.find_element(*self.login_title).text == "Log in"

    def validate_forgot_pass(self):
        forgot_pass = self.driver.find_element(*self.forgot_pass)
        forgot_pass.is_displayed()
        assert forgot_pass.text in self.driver.page_source

    def validate_register_link(self):
        register_link = self.driver.find_element(*self.register_link)
        register_link.is_displayed()
        assert register_link.text == "Don't have an account? Register here"


    def login(self):
        assert "client" in self.driver.current_url
        print("Title is:", self.driver.title)





