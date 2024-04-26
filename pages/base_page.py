import random
from typing import List

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from config.config import Config


class BasePage:
    def __init__(self, driver):
        """This method initializes the BasePage object"""
        self.driver = driver

    def go_to_element(self, element: WebElement or tuple[str, str]) -> None:
        """ This method scrolls the page to the selected element, making it visible to the user. """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def element_is_present(
            self, locator: WebElement or tuple[str, str], timeout: int = Config.WAIT_TIMEOUT
    ) -> WebElement:
        """
        This method expects to verify that the element is present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the element.
        Timeout - the duration it will wait for.
        """
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_visible(
            self, locator: WebElement or tuple[str, str], timeout: int = Config.WAIT_TIMEOUT
    ) -> WebElement:
        """
        This method expects to verify that the element is present in the DOM tree, visible, and displayed on the page.
        Visibility means that the element is not only displayed but also has a height and width greater than 0.
        Locator - is used to find the element.
        Timeout - the duration it will wait for.
        """
        self.go_to_element(self.element_is_present(locator))
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(
            self, locator: WebElement or tuple[str, str], timeout: int = Config.WAIT_TIMEOUT) -> List[WebElement]:
        """
        This method expects to verify that the elements are present in the DOM tree, visible and displayed on the page.
        Visibility means that the elements are not only displayed but also have a height and width greater than 0.
        Locator - is used to find the elements.
        Timeout - the duration it will wait for.
        """
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def open(self, url) -> None:
        """This method opens a browser by the provided link"""
        with allure.step(f"Открыть страницу {url}"):
            self.driver.get(url)

    def clear_input_and_send_keys(self, locator: WebElement or tuple[str, str], text: str) -> None:
        """This method clears the input field, clicks on it, and then sends the provided text to the input field"""
        input_field = self.element_is_visible(locator)
        input_field.click()
        input_field.clear()
        input_field.send_keys(text)

    def select_random_checkbox(self, locator: WebElement or tuple[str, str]) -> None:
        """ This method selects a random checkbox from the provided list of checkboxes"""
        checkboxes = self.elements_are_visible(locator)
        checkbox = random.choice(checkboxes)
        checkbox.click()

    def click_button(self, locator: WebElement or tuple[str, str]) -> None:
        """ This method clicks on the provided button"""
        self.element_is_visible(locator).click()
