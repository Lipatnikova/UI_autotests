import allure

from pages.base_page import BasePage


class SqlExLoginPage(BasePage):
    LOGIN_FORM = ("xpath", "//*[@name='frmlogin']")
    BTN_LOGIN_WITHOUT_REGISTRATION = ("xpath", "//*[@name='subm2']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_button_without_registration(self) -> None:
        with allure.step("Нажать кнопку Вход без регистрации"):
            self.click_button(self.BTN_LOGIN_WITHOUT_REGISTRATION)

    def login_form_is_visible(self) -> bool:
        with allure.step("Проверить видимость формы авторизации"):
            return self.is_element_present(self.LOGIN_FORM)
