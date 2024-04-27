import allure

from config.links import Links
from pages.authentication_page import AuthPage


class TestAuthPage:
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
    def test_verify_authorization_image_is_displayed_after_authorization_by_basic_auth(self, driver):
        auth_page = AuthPage(driver)
        auth_page.open(Links.URL_AUTH)
        auth_page.click_display_image_button()
        auth_page.authorization_basic()
        with (allure.step("Проверить, что авторизация прошла успешно: "
                          "картинка об авторизации отображается на странице")):
            assert auth_page.authorization_image_is_displayed(), \
                "The authorization image doesn't displayed on page"
