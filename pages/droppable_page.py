import allure

from pages.base_page import BasePage


class DroppablePage(BasePage):
    IFRAME_1 = ("xpath", "//*[@id='example-1-tab-1']/div/iframe")
    DRAG_ME = ("xpath", "//*[@id='draggable']")
    DROP_HERE = ("xpath", "//*[@id='droppable']")
    MESSAGE_DROPPED = ("css selector", "#droppable > p")

    def switch_to_iframe_default(self):
        with allure.step("Переключиться в iframe 1"):
            self.switch_to_iframe(self.IFRAME_1)

    def drag_and_drop(self):
        with allure.step("Перетащить элемент в принимающую карточку"):
            drag_me = self.element_is_visible(self.DRAG_ME)
            drop_here = self.element_is_visible(self.DROP_HERE)
            self.action_drag_and_drop_to_element(drag_me, drop_here)

    def extract_message_about_dropped(self):
        with allure.step("Получить текст сообщения в карточке Drop here"):
            return self.get_text(self.MESSAGE_DROPPED)

    def drag_and_drop_by_x_y(self):
        with allure.step("Перетащить элемент в принимающую карточку"):
            drag_me = self.element_is_visible(self.DRAG_ME)
            self.action_drag_and_drop_by_offset(drag_me, 10, 300)
