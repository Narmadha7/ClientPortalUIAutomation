import time

from selenium.webdriver.common.by import By


class SuccessPage:
    def __init__(self, driver):
        self.driver = driver
        self.success_msg = (By.CSS_SELECTOR, ".hero-primary")

    def validate_success_msg(self):
        msg = self.driver.find_element(*self.success_msg).text
        print(msg)
        assert "THANKYOU" in msg
        time.sleep(4)