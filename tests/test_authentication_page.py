import allure
import pytest

from config.links import Links
from generator.generator import create_person
from pages.authentication_page import AuthPage


class TestAuthPage:
    @pytest.mark.ui_autotests
    @allure.epic("Работа с элементами на странице")
    @allure.feature("Basic auth")
    @allure.story("Пройти авторизацию используя Basic auth")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("U13")
    @allure.description("""
    Цель: убедиться, что авторизация работает корректно.
    Предусловия: открыть браузер.
    Шаги:
    1.	Открыть https://www.httpwatch.com/httpgallery/authentication/#showExample10
    2.	Нажать на кнопку "Display Image".
    3.	Пройти авторизацию (логин "httpwatch" пароль "httpwatch").
    4.	Убедиться, что авторизация прошла успешно.

    """)
    def test_verify_authorization_by_basic_auth(self, driver):
        info = next(create_person())
        username = "httpwatch"
        password = info.password

        auth_page = AuthPage(driver)
        auth_page.open(Links.URL_AUTH)
        auth_page.click_display_image_button()
        header, status_code = auth_page.authorization_basic(username, password)
        with allure.step("Проверить, что авторизация прошла успешно"):
            assert "Basic" in header, \
                "Headers hasn't expected header Authorization: Basic ... "
            assert status_code == 200, \
                f'Response status code is incorrect, actual: {status_code}, expected : 200'
