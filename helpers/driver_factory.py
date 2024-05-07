from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class DriverFactory:
    @staticmethod
    def create_driver(browser_name, hub_address=None):
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

        return driver
