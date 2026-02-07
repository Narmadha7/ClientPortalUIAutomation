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
        self.submit_button = (By.CSS_SELECTOR, ".btn")
        self.login_link = (By.LINK_TEXT, "Login")
        self.register_link = (By.LINK_TEXT, "Register")

    def verify_page(self):
        return self.driver.current_url

    def verify_title(self):
        return self.driver.title

    def email_label(self):
        return self.driver.find_element(*self.label_email).text.title()

    def email_placeholder(self):
        return self.driver.find_element(*self.email).get_attribute("placeholder")

    def email_is_displayed(self):
        return self.driver.find_element(*self.email).is_displayed()

    def enter_email(self, email_input):
        # assert self.driver.find_element(*self.label_email).text.title() == "Email"
        # assert self.get_text(self.label_email) == "Email"
        self.driver.find_element(*self.email).send_keys(email_input)
        time.sleep(2)

    def password_label(self):
        return self.driver.find_element(*self.label_password).text.title()

    def password_placeholder(self):
        return self.driver.find_element(*self.password).get_attribute("placeholder")

    def password_is_displayed(self):
        return self.driver.find_element(*self.password).is_displayed()

    def enter_password(self, passwd):
        # assert self.driver.find_element(*self.label_password).text.title() == "Password"
        # assert self.get_text(self.label_password) == "Password"
        self.driver.find_element(*self.password).send_keys(passwd)
        time.sleep(2)

    def con_password_label(self):
        return self.driver.find_element(*self.label_confirm_pass).text.title()

    def con_password_placeholder(self):
        return self.driver.find_element(*self.confirm_pass).get_attribute("placeholder")

    def con_password_is_displayed(self):
        return self.driver.find_element(*self.confirm_pass).is_displayed()

    def enter_confirm_password(self, conpass):
        # assert self.driver.find_element(*self.label_confirm_pass).text.title() == "Confirm Password"
        # assert self.get_text(self.label_confirm_pass) == "Confirm Password"
        # print(self.get_text(self.label_confirm_pass))
        self.driver.find_element(*self.confirm_pass).send_keys(conpass)
        time.sleep(2)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def is_enabled(self):
        return self.driver.find_element(*self.submit_button).is_enabled()
        # self.is_enabled(self.submit_button)
        # button.click()
        # self.click(self.submit_button)

    def validate_login_link(self):
        return self.driver.find_element(*self.login_link).is_displayed()
        # self.is_displayed(self.login_link)

    def validate_register_link(self):
        return self.driver.find_element(*self.register_link).is_displayed()
        # self.is_displayed(self.register_link)
