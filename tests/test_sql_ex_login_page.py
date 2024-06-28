import allure
import pytest

from config.links import Links
from helpers.use_cookies import UseCookies
from pages.sql_ex_login_page import SqlExLoginPage


class TestSqlExLoginPage:

    @pytest.mark.ui_autotests
    @allure.epic("Управление пользователями")
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
    def test_auth_and_save_cookies_to_file(self, driver):
        page_sql_ex = SqlExLoginPage(driver)
        page_sql_ex.open(Links.URL_SQL_EX)
        page_sql_ex.click_button_without_registration()
        use_cookies = UseCookies(driver)
        use_cookies.write_cookies_to_file()
        with allure.step("Проверить, что авторизация прошла успешно: форма авторизации НЕ отображается на странице."):
            assert page_sql_ex.login_form_is_visible() is False, \
                "Authorization FAILED, the authorization form is displayed on the page"

    @pytest.mark.ui_autotests
    @allure.epic("Управление пользователями")
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
    def test_auth_use_cookies(self, driver):
        page_sql_ex = SqlExLoginPage(driver)
        use_cookies = UseCookies(driver)
        page_sql_ex.open(Links.URL_SQL_EX)
        use_cookies.delete_cookies()
        use_cookies.load_cookies_from_file()

        page_sql_ex.refresh_page()

        with allure.step("Проверить, что авторизация прошла успешно: форма авторизации НЕ отображается на странице."):
            assert page_sql_ex.login_form_is_visible() is False, \
                "Authorization FAILED, the authorization form is displayed on the page"

        use_cookies.delete_cookies_file()

    @pytest.mark.ui_autotests
    @allure.epic("Управление пользователями")
    @allure.feature("Авторизация")
    @allure.story("Проверить наличие scroll на странице")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("U6_2_2")
    @allure.description("""
            Цель: проверить наличие scroll на страницие: 
            Предусловия:
            1. Открыть браузер.
            Шаги:
            1. Открыть сайт https://www.sql-ex.ru/ .
            2. Проверить, что на странице есть scroll.
            Ожидаемый результат:
            Scroll есть на странице""")
    def test_verify_is_scroll_by_sql_ex_login_page(self, driver):
        page_sql_ex = SqlExLoginPage(driver)
        page_sql_ex.open(Links.URL_SQL_EX)
        with allure.step("Проверить, что на странице есть scroll"):
            assert page_sql_ex.is_scroll_present() is False, \
                "The page is not scrolled by page"
