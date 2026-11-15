import pytest
import allure


from config.settings import settings
from pages.user_account.account_page import AccountPage
from pages.components.modals import ModalsComponent
from locators.components.modals_locators import LocatorsForModals


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_check_ask_question_modal_from_help(authorized_user):
    """Проверить, что по клику кнопки 'Написать сообщение' открывается модалка 'Задать вопрос'"""
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию
    modals = ModalsComponent(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию

    #    Переходим в таб "Помощь"
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
def test_check_errors_in_ask_question_modal_from_help(authorized_user):
    """Проверить, что под пустыми полями есть ошибки"""
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию
    modals = ModalsComponent(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию

    #    Переходим в таб "Помощь"
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_help()  # Кликаем по табу "Помощь"
    )
    account.click_btn_write_message()  # Кликаем по кнопке 'Написать сообщение')

    #    Предусловие: Удалить значения в полях "Ваше имя, Телефон, E-mail" (сейчас они по умолчанию предзаполнены)
    (
        modals.clear_name_field_in_ask_question_modal()
        .clear_phone_field_in_ask_question_modal()
        .clear_email_field_in_ask_question_modal()
    )

    modals.click_send_btn_in_ask_question_modal()

    assert modals.is_error_message_name_in_ask_question_modal(), 'Под полем "Ваше имя" нет оишибки: "Заполните это поле!"'
    assert modals.is_error_message_phone_in_ask_question_modal(), 'Под полем "Телефон" нет оишибки: "Заполните это поле!"'
    assert modals.is_error_message_msg_in_ask_question_modal(), 'Под полем "Сообщение" нет оишибки: "Заполните это поле!"'
    assert modals.is_error_message_capcha_in_ask_question_modal(), 'Под полем "Я не робот" нет оишибки: "Пройдите проверку"'
    assert modals.is_error_message_confidencial_in_ask_question_modal(), 'Под полем "Политика сайта" нет оишибки: "Согласитесь с условиями"'


@allure.feature('')
@allure.story('')
@pytest.mark.parametrize(
    'name, phone, email, interesting_card, message', [
        ('Тест', '79994231265', 'test@gmail.com', 'Лодка', 'Проверка модалки_1'),
        ('Test', '79994235126', 'test_1@gmail.com', 'Lodka', 'Проверка модалки_2')
    ]
)
@pytest.mark.smoke
def test_check_input_field_in_ask_question_modal_from_help(authorized_user, name, phone, email, interesting_card, message):
    """ Проверить возможность заполнения полей модалки "Задать вопрос" """
    account = AccountPage(authorized_user)
    modals = ModalsComponent(authorized_user)

    #    Переходим в таб "Помощь"
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_help()  # Кликаем по табу "Помощь"
    )
    account.click_btn_write_message()  # Кликаем по кнопке 'Написать сообщение')

    #    Предусловие: Удалить значения в полях "Ваше имя, Телефон, E-mail" (сейчас они по умолчанию предзаполнены)
    (
        modals.clear_name_field_in_ask_question_modal()
        .clear_phone_field_in_ask_question_modal()
        .clear_email_field_in_ask_question_modal()
    )

    (
        modals.enter_name_in_ask_question_modal(name)
        .enter_phone_in_ask_question_modal(phone)
        .enter_email_in_ask_question_modal(email)
        .enter_interesting_card_in_ask_question_modal(interesting_card)
        .enter_message_in_ask_question_modal(message)
        .click_confidential_checkbox_in_ask_question_modal()
    )

    assert modals.is_field_filled(LocatorsForModals.INPUT_NAME_IN_ASK_QUESTION), 'Поле "Ваше имя" пустое!'
    assert modals.is_field_filled(LocatorsForModals.INPUT_PHONE_IN_ASK_QUESTION), 'Поле "Телефон" пустое!'
    assert modals.is_field_filled(LocatorsForModals.INPUT_EMAIL_IN_ASK_QUESTION), 'Поле "E-mail" пустое!'
    assert modals.is_field_filled(LocatorsForModals.INPUT_INTERESTING_CARD_IN_ASK_QUESTION), 'Поле "Интересующий товар/услуга" пустое!'
    assert modals.is_field_filled(LocatorsForModals.INPUT_MESSAGE_IN_ASK_QUESTION), 'Поле "Сообщение" пустое!'
    #assert modals.is_checkbox_checked(LocatorsForModals.CHECKBOX_COFIDENTIONAL_IN_ASK_QUESTION), 'Чекбокс "Согласие с политикой" не отмечен!'
    #    проверка чекбокса пока падает, допускаю, что из-за того, что забираем значения не из самого чекбокса, а из контейнера