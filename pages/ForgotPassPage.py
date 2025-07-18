import time

from selenium.webdriver.common.by import By

from BasePage.BasePage import BasePage


class ForgotPassPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.title = (By.XPATH, "//h3[text()='Enter New Password']")
        self.label_email = (By.XPATH, "//label[text()='Email']")
        self.label_password = (By.XPATH, "//label[text()='Password']")
        self.label_confirm_pass = (By.XPATH, "//label[text()='Confirm Password']")
        self.email = (By.XPATH, "//input[@type='email']")
        self.password = (By.CSS_SELECTOR, "#userPassword")
        self.confirm_pass = (By.ID, "confirmPassword")
        self.forgot_pass = (By.XPATH, "//a[text()='Forgot password?']")
        self.submit_button = (By.CSS_SELECTOR, ".btn")
        self.login_link = (By.LINK_TEXT, "Login")
        self.register_link = (By.LINK_TEXT, "Register")

    def login(self):
        assert "client" in self.driver.current_url
        print("Title is:", self.driver.title)

    def validate_email(self):
        # assert self.driver.find_element(*self.label_email).text.title() == "Email"
        # email = self.driver.find_element(*self.email)
        # email.is_displayed()
        # print(email.get_attribute("placeholder"))
        # email.send_keys("brainandbeauty@test")
        # time.sleep(2)
        self.type(self.email, "brainandbeauty@test")
        time.sleep(2)

    def validate_password(self):
        # assert self.driver.find_element(*self.label_password).text.title() == "Password"
        # password = self.driver.find_element(*self.password)
        # password.is_displayed()
        # print(password.get_attribute("placeholder"))
        # password.send_keys("Brain@1234")
        # time.sleep(2)
        self.type(self.password, "Brain@1234")
        time.sleep(2)

    def validate_confirm_password(self):
        # assert self.label_confirm_pass == "Confirm Password"
        # confirm_password = self.driver.find_element(*self.confirm_pass)
        # confirm_password.is_displayed()
        self.is_displayed(self.confirm_pass)
        # print(confirm_password.get_attribute("placeholder"))
        # confirm_password.send_keys("Brain@12")
        self.type(self.confirm_pass, "Brain@12")
        time.sleep(2)

    def click_submit(self):
        # button = self.driver.find_element(*self.submit_button)
        # assert button.is_enabled()
        self.is_enabled(self.submit_button)
        # button.click()
        self.click(self.submit_button)

    def validate_login_link(self):
        # self.driver.find_element(*self.login_link).is_displayed()
        self.is_displayed(self.login_link)

    def validate_register_link(self):
        # self.driver.find_element(*self.register_link).is_displayed()
        self.is_displayed(self.register_link)
