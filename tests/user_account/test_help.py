import time

import pytest
import allure


from config.settings import settings
from pages.user_account.account_page import AccountPage
from pages.components.modals import ModalsComponent


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_check_ask_question_modal(authorized_user):
    """Проверить, что по клику кнопки 'Написать сообщение' открывается модалка 'Задать вопрос'"""
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию
    modals = ModalsComponent(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию

    # Переходим в Помощь
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_help()  # Кликаем по табу "Помощь"
    )
    account.click_btn_write_message()  # Кликаем по кнопке 'Написать сообщение')

    assert modals.is_ask_question_modal_visible(), 'Модалка "Задать вопрос" не появилась на странице'
    title_in_modal = modals.check_title_in_ask_question_modal(); print(f'\nЗаголовок модалки: {title_in_modal}')
    assert title_in_modal != '', 'Заголовок в модалке "Задать вопрос" пустой'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_check_errors_in_ask_question_modal(authorized_user):
    """Проверить, что под пустыми полями есть ошибки"""
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию
    modals = ModalsComponent(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию

    # Переходим в Помощь
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_help()  # Кликаем по табу "Помощь"
    )
    account.click_btn_write_message()  # Кликаем по кнопке 'Написать сообщение')

    #    Предусловие: Удалить значения в полях "Ваше имя, Телефон, E-mail" (сейчас они по умочанию предзаполнены)
    (
        modals.clear_name_field_in_ask_question_modal()
        .clear_phone_field_in_ask_question_modal()
        .clear_email_field_in_ask_question_modal()
    )

    modals.click_send_btn_in_ask_question_modal()
    time.sleep(5)

    assert modals.is_error_message_name_in_ask_question_modal(), 'Под полем "Ваше имя" нет оишибки: "Заполните это поле!"'
    assert modals.is_error_message_phone_in_ask_question_modal(), 'Под полем "Телефон" нет оишибки: "Заполните это поле!"'
    assert modals.is_error_message_msg_in_ask_question_modal(), 'Под полем "Сообщение" нет оишибки: "Заполните это поле!"'
    assert modals.is_error_message_capcha_in_ask_question_modal(), 'Под полем "Я не робот" нет оишибки: "Пройдите проверку"'
    assert modals.is_error_message_confidencial_in_ask_question_modal(), 'Под полем "Политика сайта" нет оишибки: "Согласитесь с условиями"'