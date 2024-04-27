import allure
import requests

from config.links import Links
from pages.base_page import BasePage


class AuthPage(BasePage):
    BUTTON_DISPLAY_IMAGE = ("xpath", "//*[@id='displayImage']")
    AUTH_IMAGE = ("xpath", "//*[@id='downloadImg']")

    USERNAME = "httpwatch"
    PASSWORD = "httpwatch"
    STATUS_CODE_OK = 200

    def click_display_image_button(self) -> None:
        with allure.step("Нажать на кнопку Display Image"):
            self.click_button(self.BUTTON_DISPLAY_IMAGE)

    def authorization_basic(self) -> None:
        with allure.step("Отправить запрос авторизации"):
            response = requests.get(Links.URL_AUTH, auth=(self.USERNAME, self.PASSWORD))
            status_code = response.status_code
            assert status_code == self.STATUS_CODE_OK, \
                f'Response status code is incorrect, actual: {status_code}, expected : {self.STATUS_CODE_OK}'

    def authorization_image_is_displayed(self) -> bool:
        with allure.step("Проверить, есть ли картинка авторизации на странице"):
            return self.is_element_present(self.AUTH_IMAGE)
