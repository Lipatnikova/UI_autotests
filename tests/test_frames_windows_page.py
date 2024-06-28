import allure
import pytest

from config.links import Links
from pages.frames_windows_page import FramesWindowsPage


class TestFramesWindowsPage:
    @pytest.mark.ui_autotests
    @allure.epic("Работа с элементами на странице")
    @allure.feature("Frames and windows")
    @allure.story("Переключение в новую вкладку")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("U11")
    @allure.description("""
        Цель: убедиться, что после нажатия на ссылку New Browser Tab открылась новая вкладка.
        Предусловия: открыть браузер.
        Шаги:
        1.	Открыть http://way2automation.com/way2auto_jquery/frames-and-windows.php .
        2.	Нажать на ссылку New Browser Tab.
        3.	Перенести фокус на новую вкладку, нажать ссылку New Browser Tab.
        4.	Убедиться, что открылась третья вкладка.
        """)
    def test_verify_count_windows_after_clicks_by_links(self, driver):
        page = FramesWindowsPage(driver)
        page.open(Links.URL_TABS)
        page.switch_to_iframe_tab()
        page.click_link_new_browser_tab()
        page.switch_to_the_x_window(1)
        page.click_link_new_browser_tab()
        page.switch_to_the_x_window(2)
        actual_count = page.get_count_windows()
        with (allure.step("Проверить, что количество открытых вкладок равно ожидаемому: 3")):
            assert actual_count == 3, \
                (f"Actual count windows: {page.get_count_windows()}. "
                 f"Expected: 3 windows should be opened")
