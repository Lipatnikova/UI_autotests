from selenium.common import TimeoutException
from properties.property_registration_page import PropertyRegistrationPage


class RegistrationPage(PropertyRegistrationPage):

    def fill_first_name(self, first_name: str):
        self.clear_input_and_send_keys(self.first_name_input, first_name)

    def fill_last_name(self, last_name: str) -> None:
        self.clear_input_and_send_keys(self.last_name_input, last_name)

    def choose_hobby(self) -> None:
        self.select_random_checkboxes(self.hobby_checkboxes)

    def fill_phone(self, phone: str) -> None:
        self.clear_input_and_send_keys(self.phone_number_input, phone)

    def fill_username(self, username: str) -> None:
        self.clear_input_and_send_keys(self.username_input, username)

    def fill_email(self, email: str) -> None:
        self.clear_input_and_send_keys(self.email_input, email)

    def fill_password(self, password: str) -> None:
        self.clear_input_and_send_keys(self.password_input, password)

    def fill_confirm_password(self, password: str) -> None:
        self.clear_input_and_send_keys(self.confirm_password_input, password)

    def click_submit(self) -> None:
        self.click_button(self.submit_button)

    def find_count_error_messages_by_page(self) -> int:
        try:
            elements = self.error_message_label
            return len(elements)
        except TimeoutException:
            return 0
