import allure
import pytest

from config.links import Links
from helpers.use_cookies import UseCookies
from pages.sql_ex_page import SqlExPage


class TestUseCookies:

    @allure.epic("Работа с Cookies")
    @allure.feature("Авторизация")
    @allure.story("Авторизация запись Cookies в файл")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("U5")
    @allure.description("""
    Цель: авторизоваться и записать в файл Cookies.
    Предусловие: открыть браузер.
    Шаги:
    1. Открыть сайт https://www.sql-ex.ru/ .
    2. Нажать кнопку Вход без регистрации.
    3. Записать файлы Cookies в файл.
    4. Проверить, что авторизация прошла успешно: форма авторизации НЕ отображается на странице.
    Ожидаемый результат:
    Авторизация прошла успешно: форма авторизации НЕ отображается на странице.
    """)
    @pytest.mark.dependency(name="test1")
    def test_save_cookies_to_file(self, driver):
        page_sql_ex = SqlExPage(driver)
        page_sql_ex.open(Links.URL_SQL_EX)
        page_sql_ex.click_button_without_registration()
        use_cookies = UseCookies(driver)
        use_cookies.write_cookies_to_file()
        with allure.step("Проверить, что авторизация прошла успешно: форма авторизации НЕ отображается на странице."):
            assert page_sql_ex.login_form_is_visible() is False, \
                "Authorization FAILED, the authorization form is displayed on the page"

    @allure.epic("Работа с Cookies")
    @allure.feature("Авторизация")
    @allure.story("Авторизация перезапись Cookies сессии")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("U5")
    @allure.description("""
        Цель: авторизоваться на сайте, используя Cookies из файла.
        Предусловие: 
        1. Пройден тест test_save_cookies_to_file, имеется файл с Cookies.
        2. Открыть браузер.
        Шаги:
        1. Открыть сайт https://www.sql-ex.ru/ .
        2. Удалить Cookies сессии.
        3. Перезаписать Cookies сессии из файла.
        4. Проверить, что авторизация прошла успешно: форма авторизации НЕ отображается на странице.
        Ожидаемый результат:
        Авторизация прошла успешно: форма авторизации НЕ отображается на странице.
        """)
    @pytest.mark.dependency(depends=["test1"])
    def test_use_cookie(self, driver):
        page_sql_ex = SqlExPage(driver)
        use_cookies = UseCookies(driver)
        page_sql_ex.open(Links.URL_SQL_EX)
        use_cookies.delete_cookies()
        use_cookies.load_cookies_from_file()

        page_sql_ex.refresh_page()

        with allure.step("Проверить, что авторизация прошла успешно: форма авторизации НЕ отображается на странице."):
            assert page_sql_ex.login_form_is_visible() is False, \
                "Authorization FAILED, the authorization form is displayed on the page"

        use_cookies.delete_cookies_file()
