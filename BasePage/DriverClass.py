import pytest
from selenium import webdriver

class DriverClass:
    @staticmethod
    def get_driver_details():
        driver = None
        if pytest.browser == "chrome":
            driver = webdriver.Chrome()
        elif pytest.browser == "firefox":
            driver = webdriver.Firefox()
        driver.implicitly_wait(2)
        return driver