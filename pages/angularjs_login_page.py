import allure

from pages.base_page import BasePage


class AngularjsLoginPage(BasePage):
    USERNAME_INPUT = ("css selector", "#username")
    PASSWORD_INPUT = ("css selector", "#password")
    USERNAME_DES_INPUT = ("css selector", "input#formly_1_input_username_0")
    LOGIN_BTN = ("xpath", "//*[@ng-click='Auth.login()']")
    MESSAGE_LOGGED_IN = ("xpath", "//div/p[@class='ng-scope'][1]")
    MESSAGE_INCORRECT = ("css selector", ".alert-danger.ng-binding.ng-scope")

    def fill_username(self, username: str) -> None:
        with allure.step("Заполнить поле Username"):
            self.clear_input_and_send_keys(self.USERNAME_INPUT, username)

    def fill_password(self, password: str) -> None:
        with allure.step("Заполнить поле Password"):
            self.clear_input_and_send_keys(self.PASSWORD_INPUT, password)

    def fill_username_description(self, username_desc) -> None:
        with allure.step("Заполнить поле Username description"):
            self.clear_input_and_send_keys(self.USERNAME_DES_INPUT, username_desc)

    def click_button_login(self) -> None:
        with allure.step("Нажать кнопку Login"):
            self.click_button(self.LOGIN_BTN)

    def get_message_you_logged_in(self) -> str:
        with allure.step("Получить текст сообщения после авторизации"):
            return self.get_text(self.MESSAGE_LOGGED_IN)

    def get_message_incorrect_username_or_password(self) -> str:
        with allure.step("Получить текст сообщения об ошибке \"Username or password is incorrect\""):
            return self.get_text(self.MESSAGE_INCORRECT)

    def is_username_has_focus(self) -> bool:
        with allure.step("Проверить, что поле Username имеет фокус"):
            username = self.element_is_visible(self.USERNAME_INPUT)
            return self.is_element_focused(username)

    def remove_focus_on_username_field(self) -> None:
        with allure.step("Убрать фокус с поля Username"):
            username = self.element_is_visible(self.USERNAME_INPUT)
            self.blur_input_field(username)
