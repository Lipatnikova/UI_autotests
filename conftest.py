import datetime
import allure
import pytest
from helpers.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption('--browser_name', choices=["chrome", "firefox", "edge"], action='store',
                     default="chrome", help="Choose browser: chrome, firefox, edge")
    parser.addoption('--hub_address', action='store', default=None,
                     help="Selenium Grid Hub address")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser_name")
    hub_address = request.config.getoption("--hub_address")

    driver = DriverFactory.create_driver(browser_name, hub_address)

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call' and result.failed:
        if 'driver' in item.fixturenames and call.excinfo is not None:
            browser = item.funcargs['driver']
            allure.attach(
                browser.get_screenshot_as_png(),
                name=f'screenshot_{datetime.datetime.utcnow()}',
                attachment_type=allure.attachment_type.PNG
            )
