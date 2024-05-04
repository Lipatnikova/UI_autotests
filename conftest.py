import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', choices=["chrome", "firefox", "edge"], action='store',
                     default="chrome", help="Choose browser: chrome, firefox, edge")
    parser.addoption('--hub_address', action='store', default=None,
                     help="Selenium Grid Hub address")


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    browser_name = request.config.getoption("--browser_name")
    hub_address = request.config.getoption("--hub_address")
    options = None

    if browser_name == "chrome":
        options = ChromeOptions()
    elif browser_name == "firefox":
        options = FirefoxOptions()
    elif browser_name == "edge":
        options = EdgeOptions()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.to_capabilities()

    driver = None

    if hub_address:
        driver = webdriver.Remote(command_executor=hub_address, options=options)
    else:
        if browser_name == "chrome":
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            driver = webdriver.Firefox(options=options)
        elif browser_name == "edge":
            driver = webdriver.Edge(options=options)

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        if 'driver' in item.fixturenames:
            browser = item.funcargs['driver']
            allure.attach(
                browser.get_screenshot_as_png(),
                name=f'screenshot_{datetime.datetime.utcnow()}',
                attachment_type=allure.attachment_type.PNG
            )
