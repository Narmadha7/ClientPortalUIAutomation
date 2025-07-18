import pytest

from selenium import webdriver


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")
    parser.addoption("--html_path", action="store", default="reports/report.html", help="custom report generated")


@pytest.hookimpl
def pytest_configure(config):
    path = config.getoption("--html_path")
    config.option.html_path = path


@pytest.fixture()
def browserInstance(pytestconfig):
    driver = None
    browser_name = pytestconfig.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.implicitly_wait(3)
    driver.get("https://rahulshettyacademy.com/client")
    driver.maximize_window()
    yield driver
    driver.close()
