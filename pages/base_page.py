import random
from typing import List

import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
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

    def is_element_present(self, locator: WebElement or tuple[str, str]) -> bool:
        """
        This method checks if the specified element is present on the webpage.
        It uses the `element_is_present` method to find the element and returns `True`
        if the element is found within the specified timeout, otherwise, it returns `False`.
        """
        try:
            self.element_is_present(locator)
            return True
        except TimeoutException:
            return False

    def open(self, url) -> None:
        """This method opens a browser by the provided link"""
        with allure.step(f"Открыть страницу {url}"):
            self.driver.get(url)

    def get_current_url(self) -> str:
        """This method gets current url"""
        with allure.step("Получить URL текущей страницы"):
            return self.driver.current_url

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

    def switch_to_iframe(self, locator: WebElement or tuple[str, str]) -> None:
        """ This method switches to an iframe element"""
        self.driver.switch_to.frame(self.element_is_visible(locator))

    def action_drag_and_drop_to_element(self, what: WebElement, where: WebElement) -> None:
        """Drag and drop element to element"""
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    def action_drag_and_drop_by_offset(self, elem: WebElement, x, y):
        """
        Holds down the left mouse button on the source element,
        then moves to the target offset and releases the mouse button.
        """
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(elem, x, y)
        action.perform()

    def get_text(self, locator: WebElement or tuple[str, str]) -> str:
        """ This method gets the text from the element"""
        return self.element_is_visible(locator).text

    def fill_alert_and_accept(self, name: str) -> None:
        """ This method switches to an alert, send keys in input alert and accept alert"""
        alert = self.driver.switch_to.alert
        alert.send_keys(name)
        alert.accept()

    def get_alert_text_and_accept(self) -> str:
        """ This method switches to an alert, gets text and accept alert"""
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def switch_to_the_x_window(self, index: int) -> None:
        """ This method switches to a window by index window"""
        self.driver.switch_to.window(self.driver.window_handles[index])

    def get_count_windows(self) -> int:
        """ This method gets the count of windows"""
        return len(self.driver.window_handles)
