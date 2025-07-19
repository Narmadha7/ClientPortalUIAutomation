import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("selenium_driver")
class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.CSS_SELECTOR, ".login-title")
        self.firstname_label = (By.XPATH, "//label[text()='First Name']")
        self.firstname_txt = (By.ID, "firstName")
        self.lastname_label = (By.XPATH, "//label[text()='Last Name']")
        self.lastname_txt = (By.ID, "lastName")
        self.email_label = (By.XPATH, "//label[text()='Email']")
        self.email_txt = (By.ID, "userEmail")
        self.phone_label = (By.XPATH, "//label[text()='Phone Number']")
        self.phone_txt = (By.ID, "userMobile")
        self.occupation_label = (By.XPATH, "//label[text()='Occupation']")
        self.occupation_txt = (By.XPATH, "//select[@formcontrolname='occupation']")
        self.password_label = (By.XPATH, "//label[text()='Password']")
        self.password_txt = (By.ID, "userPassword")
        self.confirm_password_label = (By.XPATH, "//label[text()='Confirm Password']")
        self.confirm_password_txt = (By.ID, "confirmPassword")
        self.gender_label = (By.XPATH, "//label[text()='Gender']")
        self.female_radio = (By.XPATH, "//input[@value='Female']")
        self.input_checkbox = (By.XPATH, "//input[@type='checkbox']")
        self.checkbox_text = (By.XPATH, "//div[contains(text(),'I am 18 year or Older')]")
        self.submit_button = (By.ID, "login")
        self.login_link = (By.CSS_SELECTOR, ".login-wrapper-footer-text")
        self.success_msg = (By.CSS_SELECTOR, ".headcolor")
        self.login_button = (By.XPATH, "//button[text()='Login']")

    def validate_firstname(self):
        assert self.driver.find_element(*self.firstname_label).text.title() == "First Name"
        assert self.driver.find_element(*self.firstname_txt).get_attribute("placeholder") == "First Name"

    def validate_lastname(self):
        assert self.driver.find_element(*self.lastname_label).text.title() == "Last Name"
        assert self.driver.find_element(*self.lastname_txt).get_attribute("placeholder") == "Last Name"

    def validate_email(self):
        assert self.driver.find_element(*self.email_label).text.title() == "Email"
        assert self.driver.find_element(*self.email_txt).get_attribute("placeholder") == "email@example.com"

    def validate_phone(self):
        assert self.driver.find_element(*self.phone_label).text.title() == "Phone Number"
        assert self.driver.find_element(*self.phone_txt).get_attribute("placeholder") == "enter your number"

    def validate_password(self):
        assert self.driver.find_element(*self.password_label).text.title() == "Password"
        assert self.driver.find_element(*self.password_txt).get_attribute("placeholder") == "Passsword"

    def validate_confirm_password(self):
        assert self.driver.find_element(*self.confirm_password_label).text.title() == "Confirm Password"
        assert self.driver.find_element(*self.confirm_password_txt).get_attribute("placeholder") == "Confirm Passsword"

    def validate_occupation(self):
        assert self.driver.find_element(*self.occupation_label).text.title() == "Occupation"

    def validate_gender(self):
        assert self.driver.find_element(*self.gender_label).text.title() == "Gender"

    def enter_firstname(self, firstname):
        name = self.driver.find_element(*self.firstname_txt)
        name.is_displayed()
        name.send_keys(firstname)

    def enter_lastname(self, lastname):
        name = self.driver.find_element(*self.lastname_txt)
        name.is_displayed()
        name.send_keys(lastname)

    def enter_email(self, email_id):
        email = self.driver.find_element(*self.email_txt)
        email.is_displayed()
        email.send_keys(email_id)

    def enter_phone(self, phone_number):
        phone = self.driver.find_element(*self.phone_txt)
        phone.is_displayed()
        phone.send_keys(phone_number)

    def enter_password(self, password):
        passwd = self.driver.find_element(*self.password_txt)
        passwd.is_displayed()
        passwd.send_keys(password)

    def enter_confirm_password(self, confirm_pass):
        confirm_pwd = self.driver.find_element(*self.confirm_password_txt)
        confirm_pwd.is_displayed()
        confirm_pwd.send_keys(confirm_pass)

    def select_occupation(self):
        occupation_dropdown = Select(self.driver.find_element(*self.occupation_txt))
        occupation_dropdown.select_by_visible_text("Engineer")
        time.sleep(5)

    def select_gender(self):
        self.driver.find_element(*self.female_radio).click()
        time.sleep(2)

    def checkbox_age_txt(self):
        print(self.driver.find_element(*self.checkbox_text).text)

    def select_checkbox(self):
        self.driver.find_element(*self.input_checkbox).click()

    def click_submit(self):
        submit_button = self.driver.find_element(*self.submit_button)
        assert submit_button.is_enabled()
        submit_button.click()
        time.sleep(3)

    def verify_login_link(self):
        try:
            return self.driver.find_element(*self.login_link).text
        except None:
            return None

    time.sleep(4)

    def verify_success_msg(self):
        return self.driver.find_element(*self.success_msg).text

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
