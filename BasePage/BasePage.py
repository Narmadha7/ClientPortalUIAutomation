from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except TimeoutException:
            raise Exception(f"Element {locator} not clickable")

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except None:
            return False

    def is_enabled(self, locator):
        try:
            return self.find(locator).is_enabled()
        except None:
            return False