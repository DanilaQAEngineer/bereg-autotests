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
    account.click_btn_write_message()  # Кликаем по кнопке 'Написать сообщение'
    time.sleep(10)

    assert modals.is_ask_question_modal_visible(), 'Модалка не появилась на странице'
    title_in_modal = modals.check_title_in_ask_question_modal(); print(f'\nЗаголовок модалки: {title_in_modal}')
    assert title_in_modal != '', 'Заголовок в модалке "Задать вопрос" пустой'
