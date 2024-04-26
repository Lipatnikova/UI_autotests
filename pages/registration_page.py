import allure
from selenium.common import TimeoutException
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    FIRST_NAME = ("xpath", "//*[@id='register_form']/fieldset[1]/p[1]/input")
    LAST_NAME = ("xpath", "//*[@id='register_form']//p[2]/input[1]")
    HOBBY = ("xpath", "//*[@name='hobby']")
    PHONE_NUMBER = ("xpath", "//*[@name='phone'and@type='text']")
    USERNAME = ("xpath", "//*[@name='username'and@type='text']")
    EMAIL = ("xpath", "//*[@name='email'and@type='text']")
    PASSWORD = ("xpath", "//*[@type='password'and@name='password']")
    CONFIRM_PASSWORD = ("xpath", "//*[@type='password'and@name='c_password']")
    BTN_SUBMIT = ("xpath", "//*[@value='submit'and@type='submit']")
    MSG_FIELD_IS_REQUIRED = ("css selector", "label.error_p")

    def fill_first_name(self, first_name: str):
        with allure.step("Заполнить поле First name"):
            self.clear_input_and_send_keys(self.FIRST_NAME, first_name)

    def fill_last_name(self, last_name: str) -> None:
        with allure.step("Заполнить поле Last name"):
            self.clear_input_and_send_keys(self.LAST_NAME, last_name)

    def choose_hobby(self) -> None:
        with allure.step("Выбрать случайным образом чек-бокс Hobby"):
            self.select_random_checkbox(self.HOBBY)

    def fill_phone(self, phone: str) -> None:
        with allure.step("Заполнить поле Phone number"):
            self.clear_input_and_send_keys(self.PHONE_NUMBER, phone)

    def fill_username(self, username: str) -> None:
        with allure.step("Заполнить поле Username"):
            self.clear_input_and_send_keys(self.USERNAME, username)

    def fill_email(self, email: str) -> None:
        with allure.step("Заполнить поле Email"):
            self.clear_input_and_send_keys(self.EMAIL, email)

    def fill_password(self, password: str) -> None:
        with allure.step("Заполнить поле Password"):
            self.clear_input_and_send_keys(self.PASSWORD, password)

    def fill_confirm_password(self, password: str) -> None:
        with allure.step("Заполнить поле Confirm password"):
            self.clear_input_and_send_keys(self.CONFIRM_PASSWORD, password)

    def click_submit(self) -> None:
        with allure.step("Нажать кнопку Submit"):
            self.click_button(self.BTN_SUBMIT)

    def find_count_error_messages_by_page(self) -> int:
        with allure.step("Найти количество сообщений \"This field is required.\" на странице"):
            try:
                elements = self.elements_are_visible(self.MSG_FIELD_IS_REQUIRED)
                return len(elements)
            except TimeoutException:
                return 0
