import allure

from pages.base_page import BasePage


class AlertPage(BasePage):
    SIMPLE_ALERT = ("xpath", "//*[@href='#example-1-tab-1']")
    INPUT_ALERT = ("xpath", "//*[@href='#example-1-tab-2']")
    IFRAME_1 = ("xpath", "//*[@class='demo-frame']")
    IFRAME_2 = ("css selector", "#example-1-tab-2 > div > iframe")
    BUTTON_TO_DEMONSTRATE_THE_INPUT_BOX = ("xpath", "//*[@onclick='myFunction()']")
    CUSTOM_MESSAGE = ("css selector", "#demo")

    def click_input_alert(self) -> None:
        with allure.step("Нажать Input Alert"):
            self.element_is_visible(self.INPUT_ALERT).click()

    def switch_to_iframe_alert_for_simple_alert(self) -> None:
        with allure.step("Переключиться в iframe Alert"):
            self.element_is_visible(self.IFRAME_1)
            self.switch_to_iframe(self.IFRAME_1)

    def switch_to_iframe_alert_for_input_alert(self) -> None:
        with allure.step("Переключиться в iframe Alert"):
            self.element_is_visible(self.IFRAME_2)
            self.switch_to_iframe(self.IFRAME_2)

    def click_button_to_demonstrate_the_input_box(self) -> None:
        with allure.step("Нажать кнопку Button to demonstrate the input box"):
            self.element_is_visible(self.BUTTON_TO_DEMONSTRATE_THE_INPUT_BOX).click()

    def fill_alert_custom_text(self, new_name: str) -> None:
        with allure.step("Заполнить Alert кастомным текстом, подтвердить"):
            self.fill_alert_and_accept(new_name)

    def extract_text_custom_message(self) -> str:
        with allure.step("Получить текст сообщения после ввода Alerta"):
            return self.get_text(self.CUSTOM_MESSAGE)
