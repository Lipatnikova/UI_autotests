import allure

from pages.droppable_page import DroppablePage
from config.links import Links


class TestDroppablePage:
    @allure.epic("Работа с элементами на странице")
    @allure.feature("Drag n Drop (IFrame)")
    @allure.story("Перетанскивание элемента на другой элемент")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("U10")
    @allure.description("""
    Цель: перетащить элемент в принимающий элемент.
    Предусловия: открыть браузер.
    Шаги:
    1.	Открыть http://way2automation.com/way2auto_jquery/droppable.php .
    2.	Перетащить элемент в принимающий.
    3.	Убедиться, что текст принимающего элемента изменился.
    """)
    def test_verify_text_second_element_after_drag_and_drop(self, driver):
        page = DroppablePage(driver)
        page.open(Links.URL_DROPPABLE)
        page.switch_to_iframe_default()
        message_before = page.extract_message_about_dropped()
        page.drag_and_drop()
        message_after = page.extract_message_about_dropped()
        with allure.step("Проверить, что текст у принимающего элемента изменился"):
            assert message_before != message_after, \
                "The message doesn't changed after drag and drop."
            assert message_after == "Dropped!", \
                (f"The message after drag and drop contains incorrect text."
                 f"Actual message text: {message_after}"
                 f"Expected message text: Dropped!")

    @allure.epic("Работа с элементами на странице")
    @allure.feature("Drag n Drop (IFrame)")
    @allure.story("Перетанскивание элемента на другой элемент по координатам падающий кейс")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("U4_2")
    @allure.description("""
       Цель: перетащить элемент в принимающий элемент.
       Предусловия: открыть браузер.
       Шаги:
       1.	Открыть http://way2automation.com/way2auto_jquery/droppable.php .
       2.	Перетащить элемент в принимающий по координатам х, у.
       3.	Убедиться, что текст принимающего элемента изменился.
       """)
    def test_verify_text_second_element_after_drag_and_drop_by_x_y(self, driver):
        page = DroppablePage(driver)
        page.open(Links.URL_DROPPABLE)
        page.switch_to_iframe_default()
        message_before = page.extract_message_about_dropped()
        page.drag_and_drop_by_x_y()
        message_after = page.extract_message_about_dropped()
        with allure.step("Проверить, что текст у принимающего элемента изменился"):
            assert message_before != message_after, \
                "The message doesn't changed after drag and drop."
            assert message_after == "Dropped!", \
                (f"The message after drag and drop contains incorrect text."
                 f"Actual message text: {message_after}"
                 f"Expected message text: Dropped!")
