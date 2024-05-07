import allure
import requests

from pages.base_page import BasePage


class AuthPage(BasePage):
    BUTTON_DISPLAY_IMAGE = ("xpath", "//*[@id='displayImage']")

    def click_display_image_button(self) -> None:
        with allure.step("Нажать на кнопку Display Image"):
            self.click_button(self.BUTTON_DISPLAY_IMAGE)

    @staticmethod
    def authorization_basic(username, password):
        with allure.step("Отправить запрос авторизации"):
            response = requests.get(
                f"https://{username}:{password}@www.httpwatch.com/httpgallery/authentication/#showExample10"
            )
            header = response.request.headers["Authorization"]
            status_code = response.status_code
            return header, status_code
