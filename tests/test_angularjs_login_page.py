import allure
import pytest

from config.links import Links
from generator.generator import create_person
from pages.angularjs_login_page import AngularjsLoginPage


class TestAngularjsLoginPage:
    @allure.epic("Управление пользователями")
    @allure.feature("Авторизация angularjs")
    @allure.story("Отправка формы авторизации и проверка сообщений об авторизации или "
                  "сообщения о вводе некорректных данных")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("U3")
    @allure.description(
            """
    Цель: проверить авторизацию с вводом валидных и невалидных данных.
    Предусловие: открыть браузер.
    Шаги:
    1. Заполнить поле username.
    2. Заполнить поле password.
    3. Заполнить поле username description.
    4. Нажать кнопку LOGIN.
    5. Проверить отображаемое сообщение и текущий url после заполнения формы авторизации.
        """)
    @pytest.mark.parametrize("username, password, message", [("angular", "password", "success"),
                                                             ("angular123", "password123", "failure")])
    def test_verify_angularjs_login(self, driver, username, password, message):
        info = next(create_person())
        user_desc = info.last_name

        page_login = AngularjsLoginPage(driver)
        page_login.open(Links.URL_LOGIN)
        page_login.fill_username(username)
        page_login.fill_password(password)
        page_login.fill_username_description(user_desc)
        page_login.click_button_login()
        current_url = page_login.get_current_url()
        with allure.step("Проверить отображаемое сообщение и текущий url после заполнения формы авторизации"):
            if message == "success":
                assert page_login.get_message_you_logged_in(), \
                    "Login failed, the message: \"You're logged in!!\" not visible"
            elif message == "failure":
                assert page_login.get_message_incorrect_username_or_password() and "login" in current_url, \
                    ('The message "Username or password is incorrect" doesn\'t show or '
                     'current url hasn\'t expected endpoint "login"')

    @allure.epic("Управление пользователями")
    @allure.feature("Авторизация angularjs")
    @allure.story("Проверить фокус на поле username")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("U6_1")
    def test_verify_focus_on_username_field(self, driver):
        info = next(create_person())
        page_login = AngularjsLoginPage(driver)
        page_login.open(Links.URL_LOGIN)
        assert page_login.is_username_has_focus() is False, \
            "Username field shouldn't have focus initially"
        page_login.fill_username(info.username)
        assert page_login.is_username_has_focus() is True, \
            "Username field should have focus after filling it"
        page_login.remove_focus_on_username_field()
        assert page_login.is_username_has_focus() is False, \
            "Username field shouldn't have focus initially"

    @allure.epic("Управление пользователями")
    @allure.feature("Авторизация angularjs")
    @allure.story("Проверить наличие scroll на странице")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("U6_2_1")
    @allure.description("""
            Цель: проверить наличие scroll на страницие:
            Предусловия:
            1. Открыть браузер.
            Шаги:
            1. Открыть сайт https://www.way2automation.com/angularjs-protractor/registeration/#/login .
            2. Проверить, что на странице есть scroll.
            Ожидаемый результат:
            Scroll отсутствует на странице""")
    def test_verify_is_scroll_by_login_page(self, driver):
        page_login = AngularjsLoginPage(driver)
        page_login.open(Links.URL_LOGIN)
        with allure.step("Проверить, что на странице отсутствует scroll"):
            assert page_login.is_scroll_present() is True, \
                "The page is not scrolled by page"
