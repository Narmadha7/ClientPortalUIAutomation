import time

from selenium.webdriver.common.by import By

class ForgotPassPage:

    def __init__(self, driver):
        self.driver = driver
        self.title = (By.XPATH, "//h3[text()='Enter New Password']")
        self.label_email = (By.XPATH, "//label[text()='Email']")
        self.label_password = (By.XPATH, "//label[text()='Password']")
        self.label_confirm_pass = (By.XPATH, "//label[text()='Confirm Password']")
        self.email = (By.XPATH, "//input[@type='email']")
        self.password = (By.CSS_SELECTOR, "#userPassword")
        self.confirm_pass = (By.ID, "confirmPassword")
        self.forgot_pass = (By.XPATH, "//a[text()='Forgot password?']")

    def click_forgot_pass(self):
        forgot_pass = self.driver.find_element(*self.forgot_pass)
        forgot_pass.click()
        time.sleep(4)

    def login(self):
        assert "client" in self.driver.current_url
        print("Title is:", self.driver.title)

    def validate_email(self):
        # assert self.label_email == "Email"
        email = self.driver.find_element(*self.email)
        email.is_displayed()
        print(email.get_attribute("placeholder"))
        email.send_keys("brainandbeauty@test.com")
        time.sleep(4)

    def validate_password(self):
        # assert self.label_password == "Password"
        password = self.driver.find_element(*self.password)
        password.is_displayed()
        print(password.get_attribute("placeholder"))
        password.send_keys("Brain@1234")
        time.sleep(4)

    def validate_confirm_password(self):
        # assert self.label_confirm_pass == "Confirm Password"
        confirm_password = self.driver.find_element(*self.confirm_pass)
        confirm_password.is_displayed()
        print(confirm_password.get_attribute("placeholder"))
        confirm_password.send_keys("Brain@1234")
        time.sleep(4)


