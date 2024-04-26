from typing import List
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from locators.registration_locators import RegistrationLocators as Locator


class PropertyRegistrationPage(BasePage):
    @property
    def first_name_input(self) -> WebElement:
        return self.element_is_visible(Locator.FIRST_NAME)

    @property
    def last_name_input(self) -> WebElement:
        return self.element_is_visible(Locator.LAST_NAME)

    @property
    def hobby_checkboxes(self) -> List[WebElement]:
        return self.elements_are_visible(Locator.HOBBY)

    @property
    def phone_number_input(self) -> WebElement:
        return self.element_is_visible(Locator.PHONE_NUMBER)

    @property
    def username_input(self) -> WebElement:
        return self.element_is_visible(Locator.USERNAME)

    @property
    def email_input(self) -> WebElement:
        return self.element_is_visible(Locator.EMAIL)

    @property
    def password_input(self) -> WebElement:
        return self.element_is_visible(Locator.PASSWORD)

    @property
    def confirm_password_input(self) -> WebElement:
        return self.element_is_visible(Locator.CONFIRM_PASSWORD)

    @property
    def submit_button(self) -> WebElement:
        return self.element_is_visible(Locator.BTN_SUBMIT)

    @property
    def error_message_label(self) -> List[WebElement]:
        return self.elements_are_visible(Locator.MSG_FIELD_IS_REQUIRED)
