import allure

from config.links import Links
from generator.generator import create_person
from pages.alert_page import AlertPage


class TestAlertPage:
    @allure.epic("Работа с элементами на странице")
    @allure.feature("Alerts")
    @allure.story("Ввести кастомный текст в Alert")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("U12")
    @allure.description("""
    Цель: убедиться, что введенный в Alert текст применился на странице.
    Предусловия: открыть браузер.
    Шаги:
    1.	Открыть http://way2automation.com/way2auto_jquery/alert.php
    2.	Нажать Input Alert.
    3.	Нажать кнопку Button to demonstrate the input box.
    4.  Заполнить Alert кастомным текстом, подтвердить.
    4.	Убедиться, что текст применился.
    """)
    def test_verify_message_after_fill_custom_text_in_alert(self, driver):
        info = next(create_person())
        first_name = info.first_name

        alert_page = AlertPage(driver)
        alert_page.open(Links.URL_ALERT)
        alert_page.click_input_alert()
        alert_page.switch_to_iframe_alert()
        alert_page.click_button_to_demonstrate_the_input_box()
        alert_page.fill_alert_custom_text(first_name)
        message = alert_page.extract_text_custom_message()
        with (allure.step(f"Проверить, что текст: {first_name}, введенный в Alert применился")):
            assert first_name in message, \
                (f"The message hasn't contains expected text: {first_name}."
                 f"Actual message: {message}")
