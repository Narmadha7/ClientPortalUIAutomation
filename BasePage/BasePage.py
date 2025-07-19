from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest:

    def maximize_windows(self):
        self.driver.maximize_window()

    def find(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    # button click
    def click(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except TimeoutException:
            raise Exception(f"Element {locator} not clickable")

    # find-element and send keys - input box
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    # label text checking
    def get_text(self, locator):
        return self.find(locator).text

    # element display check
    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except None:
            return False

    # button enabled check
    def is_enabled(self, locator):
        try:
            return self.find(locator).is_enabled()
        except None:
            return False
