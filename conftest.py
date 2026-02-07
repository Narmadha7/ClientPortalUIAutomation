import pytest

from BasePage.DriverClass import DriverClass


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser selection")
    parser.addoption("--report_path", action="store", default="reports/report.html", help="report generated path")
    parser.addoption("--test_scenario", action="store", default="register", help="a particular test")


def pytest_configure(config):
    pytest.browser = config.getoption("browser")
    path = config.getoption("report_path")
    config.option.html_path = path

# @pytest.fixture(scope="class")
# def config_options(request):
#     return {
#         "browser": request.config.getoption("browser"),
#         "report_path": request.config.getoption("report_path"),
#         "test_scenario": request.config.getoption("test_scenario"),
#     }


@pytest.fixture(scope="function")
def selenium_driver(request):
    driver_obj = DriverClass()
    driver = driver_obj.get_driver_details()
    request.cls.driver = driver
    driver.get("https://rahulshettyacademy.com/client")
    driver.maximize_window()
    yield
    driver.close()
    del driver_obj