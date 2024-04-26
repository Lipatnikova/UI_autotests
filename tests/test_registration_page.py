import pytest

from config.links import Links
from generator.generator import create_person
from pages.registration_page import RegistrationPage


class TestRegistration:
    @pytest.mark.ui
    def test_check_count_of_error_messages_after_filling_required_fields_registration_form(self, driver):
        """
        Цель: проверить отсутствие сообщений об ошибке при заполнении
        обязательных полей формы регистрации.
        Предусловие: открыть браузер.
        Шаги:
        1. Открыть страницу https://www.way2automation.com/way2auto_jquery/registration.php#load_box .
        2. Заполнить поле First name.
        3. Заполнить поле Last name.
        4. Выбрать случайным образом чек-бокс Hobby.
        5. Заполнить поле Phone number.
        6. Заполнить поле Username.
        7. Заполнить поле Email.
        8. Заполнить поле Password.
        9. Заполнить поле Confirm password.
        10. Нажать кнопку Submit.
        11. Проверить количество сообщений об ошибках на странице.
        Ожидаемый результат: Сообщения об ошибках на странице отсутствуют, количество сообщений 0.
        """
        info = next(create_person())
        first_name = info.first_name
        last_name = info.last_name
        phone = info.phone
        username = info.username
        email = info.email
        password = info.password

        reg_page = RegistrationPage(driver)
        reg_page.open(Links.URL_REGISTRATION)
        reg_page.fill_first_name(first_name)
        reg_page.fill_last_name(last_name)
        reg_page.choose_hobby()
        reg_page.fill_phone(phone)
        reg_page.fill_username(username)
        reg_page.fill_email(email)
        reg_page.fill_password(password)
        reg_page.fill_confirm_password(password)
        reg_page.click_submit()
        count_error_messages = reg_page.find_count_error_messages_by_page()
        assert count_error_messages == 0, \
            (f"Actual count error messages: {count_error_messages}."
             f"Expected: error messages should not be displayed after filling out "
             f"the required fields of the registration form")
