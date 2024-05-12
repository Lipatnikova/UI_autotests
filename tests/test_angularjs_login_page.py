import allure
import pytest

from config.links import Links
from generator.generator import create_person
from pages.angularjs_login_page import AngularjsLoginPage


class TestAngularjsLoginPage:
    @allure.epic("Управление пользователями")
    @allure.feature("Авторизация angularjs")
    @allure.story("Отправка формы авторизации и проверка сообщений об успешной авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("U3_1")
    @allure.description(
            """
    Цель: проверить авторизацию с вводом валидных данных.
    Предусловие: открыть браузер.
    Шаги:
    1. Открыть https://www.way2automation.com/angularjs-protractor/registeration/#/login .
    2. Заполнить поле username.
    3. Заполнить поле password.
    4. Заполнить поле username description.
    5. Нажать кнопку LOGIN.
    6. Проверить отображаемое сообщение об успешной авторизации и 
    текущий url после заполнения формы авторизации.
        """)
    def test_verify_angularjs_login_and_success_message(self, driver):
        username = "angular"
        password = "password"
        info = next(create_person())
        user_desc = info.last_name

        page_login = AngularjsLoginPage(driver)
        page_login.open(Links.URL_LOGIN)
        page_login.fill_username(username)
        page_login.fill_password(password)
        page_login.fill_username_description(user_desc)
        page_login.click_button_login()
        current_url = page_login.get_current_url()
        with allure.step("Проверить отображаемое сообщение об успешной авторизации и "
                         "текущий url после заполнения формы авторизации валидными данными"):
            assert page_login.get_message_you_logged_in(), \
                "Login failed, the message: \"You're logged in!!\" not visible"
            assert "angularjs-protractor/registeration" in current_url, \
                "Current url hasn\'t expected endpoint \"angularjs-protractor/registeration\""

    @allure.epic("Управление пользователями")
    @allure.feature("Авторизация angularjs")
    @allure.story("Отправка формы авторизации с невалидными данными и проверка сообщения об ошибке")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("U3_2")
    @allure.description(
        """
    Цель: проверить авторизацию с вводом не валидных данных (данных отсутствующих в БД).
    Предусловие: открыть браузер.
    Шаги:
    1. Открыть https://www.way2automation.com/angularjs-protractor/registeration/#/login .
    2. Заполнить поле username (данными отсутствующими в БД).
    3. Заполнить поле password (данными отсутствующими в БД).
    4. Заполнить поле username description.
    5. Нажать кнопку LOGIN.
    6. Проверить отображаемое сообщение и текущий url после заполнения формы авторизации невалидными данными.
    """)
    @pytest.mark.parametrize("username, password", [("12345", "12345"),
                                                    ("angularANG", "passwordPAS")])
    def test_verify_angularjs_login_not_valid_data(self, driver, username, password):
        info = next(create_person())
        user_desc = info.last_name

        page_login = AngularjsLoginPage(driver)
        page_login.open(Links.URL_LOGIN)
        page_login.fill_username(username)
        page_login.fill_password(password)
        page_login.fill_username_description(user_desc)
        page_login.click_button_login()
        current_url = page_login.get_current_url()
        with allure.step("Проверить отображаемое сообщение и текущий url после "
                         "заполнения формы авторизации невалидными данными"):
            assert page_login.get_message_incorrect_username_or_password() == "Username or password is incorrect", \
                "The message \"Username or password is incorrect\" doesn\'t show"
            assert "login" in current_url, \
                "Current url hasn\'t expected endpoint \"login\""

    @allure.epic("Управление пользователями")
    @allure.feature("Авторизация angularjs")
    @allure.story("Проверить фокус на поле username")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("U6_1")
    @allure.description("""
    Цель: Проверить фокус на поле username.
    Шаги:
    1. Открыть https://www.way2automation.com/angularjs-protractor/registeration/#/login .
    2. Проверить, что фокус на поле username отсутствует.
    3. Заполнить поле username.
    4. Проверить, что фокус находится на поле username.
    5. Удалить фокус из поля username.
    6. Проверить, что фокус на поле username отсутствует. 
    """)
    def test_verify_focus_on_username_field(self, driver):
        info = next(create_person())
        page_login = AngularjsLoginPage(driver)
        page_login.open(Links.URL_LOGIN)
        with allure.step("Проверить, что фокус на поле username отсутствует"):
            assert page_login.is_username_has_focus() is False, \
                "Username field shouldn't have focus initially"
        page_login.fill_username(info.username)
        with allure.step("Проверить, что фокус находится на поле username"):
            assert page_login.is_username_has_focus() is True, \
                "Username field should have focus after filling it"
        page_login.remove_focus_on_username_field()
        with allure.step("Проверить, что фокус на поле username отсутствует"):
            assert page_login.is_username_has_focus() is False, \
                "Username field shouldn't have focus after removing focus"

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
