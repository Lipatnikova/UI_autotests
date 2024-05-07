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
        alert_page.switch_to_iframe_alert_for_input_alert()
        alert_page.click_button_to_demonstrate_the_input_box()
        alert_page.fill_alert_custom_text(first_name)
        message = alert_page.extract_text_custom_message()
        with (allure.step(f"Проверить, что текст: {first_name}, введенный в Alert применился")):
            assert first_name in message, \
                (f"The message hasn't contains expected text: {first_name}."
                 f"Actual message: {message}")

    @allure.epic("Работа с элементами на странице")
    @allure.feature("Alerts")
    @allure.story("Проверить текст в Alert падающий кейс")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("U4_1")
    @allure.description("""
        Цель: убедиться, что Alert содержит текст \"I am an alert box!\".
        Предусловия: открыть браузер.
        Шаги:
        1.	Открыть http://way2automation.com/way2auto_jquery/alert.php
        2.	Нажать Simple Alert.
        3.	Проверить, что Alert содержит текст \"I am an alert box!\".
        4.	Нажать кнопку ОК.
        """)
    def test_verify_message_in_simple_alert(self, driver):
        alert_page = AlertPage(driver)
        alert_page.open(Links.URL_ALERT)
        alert_page.switch_to_iframe_alert_for_simple_alert()
        alert_page.click_button_to_demonstrate_the_input_box()
        alert_text = alert_page.get_alert_text_and_accept()
        expected_text = "I am NOT an alert box!"
        with allure.step(f"Проверить, что Alert содержит текст {expected_text}"):
            assert alert_text == expected_text, \
                (f"The message in Alert hasn't contains expected text: {expected_text}."
                 f"Actual message: {alert_text}")
