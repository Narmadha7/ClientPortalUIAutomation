import pytest

from BasePage.DriverClass import DriverClass


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser selection")
    parser.addoption("--html_path", action="store", default="reports/report.html", help="custom report generated")


def pytest_configure(config):
    pytest.browser = config.getoption("browser")
    path = config.getoption("html_path")
    config.option.html_path = path


@pytest.fixture()
def selenium_driver(request):
    driver_obj = DriverClass()
    driver = driver_obj.get_driver_details()
    request.cls.driver = driver

    driver.get("https://rahulshettyacademy.com/client")
