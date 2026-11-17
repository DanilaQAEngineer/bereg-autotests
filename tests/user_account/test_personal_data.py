import pytest
import allure


from config.settings import settings
from pages.user_account.account_page import AccountPage
from pages.components.modals import ModalsComponent
from locators.user_account.account_locators import LocatorsForAccount


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_check_errors_in_personal_data(authorized_user):
    """Проверить, что под пустыми обязательными полями "ФИО, E-mail, Телефон" есть ошибки"""
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию

    #    Переходим в таб "Личные данные"
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_personal_data()  # Кликаем по табу "Личные данные"
    )

    #    Предусловие: Удалить значения в полях "ФИО, E-mail, Телефон" (сейчас они по умолчанию предзаполнены)
    (
        account.clear_name_field_in_tab_personal_data()
        .clear_email_field_in_tab_personal_data()
        .clear_phone_field_in_tab_personal_data()
    )

    account.click_btn_save_in_tab_personal_data()

    assert account.is_error_message_fio_in_tab_personal_data(), 'Под полем "ФИО" нет ошибки: "This field is required."'
    assert account.is_error_message_email_in_tab_personal_data(), 'Под полем "E-mail" нет ошибки: "This field is required."'
    assert account.is_error_message_phone_in_tab_personal_data(), 'Под полем "Телефон" нет ошибки: "This field is required."'


@allure.feature('')
@allure.story('')
@pytest.mark.parametrize(
    'fio, email, phone', [
        ('Кузнецов Данил Егорович', 'itsamono@gmail.com', '+7 (929) 433-55-11')
    ]
)
@pytest.mark.smoke
def test_enter_data_in_personal_data(authorized_user, fio, email, phone):
    """ Проверить возможность заполнения полей "ФИО, E-mail, Телефон" """
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию

    #    Переходим в таб "Личные данные"
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_personal_data()  # Кликаем по табу "Личные данные"
    )

    #    Предусловие: Удалить значения в полях "ФИО, E-mail, Телефон" (сейчас они по умолчанию предзаполнены)
    (
        account.clear_name_field_in_tab_personal_data()
        .clear_email_field_in_tab_personal_data()
        .clear_phone_field_in_tab_personal_data()
    )

    (
        account.enter_fio_in_personal_data(fio)
        .enter_email_in_personal_data(email)
        .enter_phone_in_personal_data(phone)
    )

    assert account.is_field_filled_in_personal_data(LocatorsForAccount.INPUT_NAME_IN_TAB_PERSONAL_DATA), 'Поле "ФИО" пустое!'
    assert account.is_field_filled_in_personal_data(LocatorsForAccount.INPUT_EMAIL_IN_TAB_PERSONAL_DATA), 'Поле "E-mail" пустое!'
    assert account.is_field_filled_in_personal_data(LocatorsForAccount.INPUT_PHONE_IN_TAB_PERSONAL_DATA), 'Поле "Телефон" пустое!'


@allure.feature('')
@allure.story('')
@pytest.mark.parametrize(
    'fio, email, phone', [
        ('Кузнецов Данил Егорович', 'itsamono@gmail.com', '+7 (929) 433-55-11')
    ]
)
@pytest.mark.smoke
def test_saving_new_data_in_personal_data(authorized_user, fio, email, phone):
    """ Проверить возможность сохранения изменений """
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию

    #    Переходим в таб "Личные данные"
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_personal_data()  # Кликаем по табу "Личные данные"
    )

    #    Предусловие: Удалить значения в полях "ФИО, E-mail, Телефон" (сейчас они по умолчанию предзаполнены)
    (
        account.clear_name_field_in_tab_personal_data()
        .clear_email_field_in_tab_personal_data()
        .clear_phone_field_in_tab_personal_data()
    )

    (
        account.enter_fio_in_personal_data(fio)
        .enter_email_in_personal_data(email)
        .enter_phone_in_personal_data(phone)
        .click_btn_save_in_tab_personal_data()
    )

    assert account.is_success_message_after_saving_data(), 'Сообщения "Изменения сохранены" на странице не появилось'
