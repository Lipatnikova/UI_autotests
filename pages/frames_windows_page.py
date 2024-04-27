import allure

from pages.base_page import BasePage


class FramesWindowsPage(BasePage):
    IFRAME = ("css selector", "#example-1-tab-1 > div > iframe")
    NEW_BROWSER_TAB_LINK = ("xpath", "//*[text()[contains(.,'New Browser Tab')]]")

    def switch_to_iframe_tab(self) -> None:
        with allure.step("Переключиться в iframe tab"):
            self.element_is_visible(self.IFRAME)
            self.switch_to_iframe(self.IFRAME)

    def click_link_new_browser_tab(self) -> None:
        with allure.step("Нажать ссылку New Browser Tab"):
            self.element_is_visible(self.NEW_BROWSER_TAB_LINK).click()
