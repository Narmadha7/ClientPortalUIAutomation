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
        return driver

    # @staticmethod
    # def get_driver_details(config_options):   # fixture name
    #     driver = None
    #     if config_options["browser"] == "chrome":
    #         driver = webdriver.Chrome()
    #     elif config_options["browser"] == "firefox":
    #         driver = webdriver.Firefox()
    #     return driver




