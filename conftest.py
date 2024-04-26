import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', choices=["chrome", "firefox"], action='store',
                     default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    browser_name = request.config.getoption("--browser_name")
    options = None

    if browser_name == "firefox":
        options = FirefoxOptions()
    else:
        options = ChromeOptions()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080")

    if browser_name == "firefox":
        driver = webdriver.Firefox(options=options)
    else:
        driver = webdriver.Chrome(options=options)

    request.cls.driver = driver
    yield driver
    driver.quit()
