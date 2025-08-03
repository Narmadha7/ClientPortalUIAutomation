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
        self.toast_msg = (By.CSS_SELECTOR, "#toast-container")
        self.email_valid_error = (By.XPATH, "//div[contains(text(), '*Email is required')]")
        self.password_valid_error = (By.XPATH, "//div[contains(text(), '*Password is required')]")
        self.firstname_valid_error = (By.XPATH, "//div[contains(text(), '*First Name is required')]")
        self.phone_valid_error = (By.XPATH, "//div[contains(text(), '*Phone Number is required')]")
        self.confirm_password_valid_error = (By.XPATH, "//div[contains(text(), 'Confirm Password is required')]")
        self.age_checkbox_valid_error = (By.XPATH, "//div[contains(text(), '*Please check above checkbox')]")
        self.password_mismatch_error = (By.XPATH, "//div[contains(text(), 'Password and Confirm Password must match with each other.')]")

    def firstname_label_check(self):
        return self.driver.find_element(*self.firstname_label).text.title()

    def get_firstname_placeholder(self):
        return self.driver.find_element(*self.firstname_txt).get_attribute("placeholder")

    def is_firstname_displayed(self):
        return self.driver.find_element(*self.firstname_txt).is_displayed()

    def enter_firstname(self, email_input):
        self.driver.find_element(*self.firstname_txt).send_keys(email_input)

    def empty_firstname_error(self):
        return self.driver.find_element(*self.firstname_valid_error).text

    def lastname_label_check(self):
        return self.driver.find_element(*self.lastname_label).text.title()

    def get_lastname_placeholder(self):
        return self.driver.find_element(*self.lastname_txt).get_attribute("placeholder")

    def is_lastname_displayed(self):
        return self.driver.find_element(*self.lastname_txt).is_displayed()

    def enter_lastname(self, email_input):
        self.driver.find_element(*self.lastname_txt).send_keys(email_input)

    def email_label_check(self):
        return self.driver.find_element(*self.email_label).text.title()

    def get_email_placeholder(self):
        return self.driver.find_element(*self.email_txt).get_attribute("placeholder")

    def is_email_displayed(self):
        return self.driver.find_element(*self.email_txt).is_displayed()

    def enter_email(self, email_input):
        self.driver.find_element(*self.email_txt).send_keys(email_input)

    def empty_email_error(self):
        return self.driver.find_element(*self.email_valid_error).text

    def phone_label_check(self):
        return self.driver.find_element(*self.phone_label).text.title()

    def get_phone_placeholder(self):
        return self.driver.find_element(*self.phone_txt).get_attribute("placeholder")

    def is_phone_displayed(self):
        return self.driver.find_element(*self.phone_txt).is_displayed()

    def enter_phone(self, email_input):
        self.driver.find_element(*self.phone_txt).send_keys(email_input)

    def empty_phone_error(self):
        return self.driver.find_element(*self.phone_valid_error).text

    def password_label_check(self):
        return self.driver.find_element(*self.password_label).text.title()

    def get_password_placeholder(self):
        return self.driver.find_element(*self.password_txt).get_attribute("placeholder")

    def is_password_displayed(self):
        return self.driver.find_element(*self.password_txt).is_displayed()

    def enter_password(self, email_input):
        self.driver.find_element(*self.password_txt).send_keys(email_input)

    def empty_password_error(self):
        return self.driver.find_element(*self.password_valid_error).text

    def confirm_password_label_check(self):
        return self.driver.find_element(*self.confirm_password_label).text.title()

    def get_confirm_password_placeholder(self):
        return self.driver.find_element(*self.confirm_password_txt).get_attribute("placeholder")

    def is_confirm_password_displayed(self):
        return self.driver.find_element(*self.confirm_password_txt).is_displayed()

    def enter_confirm_password(self, email_input):
        return self.driver.find_element(*self.confirm_password_txt).send_keys(email_input)

    def empty_confirm_password_error(self):
        return self.driver.find_element(*self.confirm_password_valid_error).text

    def occupation_label_check(self):
        return self.driver.find_element(*self.occupation_label).text.title()

    def gender_label_check(self):
        return self.driver.find_element(*self.gender_label).text.title()

    def is_occupation_displayed(self):
        return self.driver.find_element(*self.occupation_txt).is_displayed()


    def select_occupation(self):
        occupation_dropdown = Select(self.driver.find_element(*self.occupation_txt))
        occupation_dropdown.select_by_visible_text("Engineer")
        time.sleep(5)

    def select_gender(self):
        return self.driver.find_element(*self.female_radio).click()

    def checkbox_age_txt(self):
        return self.driver.find_element(*self.checkbox_text).text

    def select_checkbox(self):
        self.driver.find_element(*self.input_checkbox).click()

    def empty_age_checkbox_error(self):
        return self.driver.find_element(*self.age_checkbox_valid_error).text

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()
        time.sleep(3)

    def is_button_enabled(self):
        return self.driver.find_element(*self.submit_button).is_enabled()

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

    def verify_password_mismatch_error(self):
        return self.driver.find_element(*self.password_mismatch_error).text
