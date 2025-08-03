import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("selenium_driver")
class AccountSuccess:
    def __init__(self, driver):
        self.driver = driver
        self.success_msg = (By.CSS_SELECTOR, ".headcolor")
        self.login_button = (By.XPATH, "//button[text()='Login']")


    def validate_success_msg(self):
        return self.driver.find_element(*self.success_msg).text

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
