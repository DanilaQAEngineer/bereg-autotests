import pytest
import allure


from pages.user_account.account_page import AccountPage
from locators.user_account.account_locators import LocatorsForAccount


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_open_subscribes(authorized_user):
    """ Проверить, что по клику таба "Подписки" открывается страница раздела "Подписки" """
    account = AccountPage(authorized_user)

    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_subscribes()  # Кликаю по табу "Подписки"
    )

    assert "/personal/subscribe/" in authorized_user.current_url, 'Переход в раздел "Подписки" не произошел'
    title_in_tab_subscribes = account.get_title_in_subscribes_tab()#; print(f'Заголовок: {title_in_tab_subscribes}')
    assert "настройки подписки" in title_in_tab_subscribes.lower(), f'Ожидали заголовок про настройки подписки, получили: "{title_in_tab_subscribes}"'


@allure.feature('')
@allure.story('')
@pytest.mark.parametrize(
    'email', [
        ('itsamono@gmail.com')
    ]
)
@pytest.mark.smoke
def test_enter_data_in_subscribes_tab(authorized_user, email):
    """ Проверить возможность заполнения полей "Ваш e-mail, чекбоксов и радиокнопок" """
    account = AccountPage(authorized_user)

    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_subscribes()  # Кликаю по табу "Подписки"
    )

    #    Предусловие: Удалить значения в поле "Ваш e-mail" (сейчас оно по умолчанию предзаполнено)
    account.clear_email_field_in_subscribes_tab()

    (
        account.enter_email_in_subscribes_tab(email)
        .click_checkbox_rub_1_in_subscribes_tab()
        .click_checkbox_rub_2_in_subscribes_tab()
        .click_radio_button_1_in_subscribes_tab()
        .click_radio_button_2_in_subscribes_tab()
    )

    assert account.is_field_filled(LocatorsForAccount.INPUT_EMAIL_IN_TAB_SUBSCRIBES), 'Поле "Ваш e-mail" пустое!'
    assert account.is_checkbox_checked(LocatorsForAccount.CHECKED_CHECKBOX_RUB_1_IN_TAB_SUBSCRIBES), 'В (первом) чекбоксе нет флажка!'


@allure.feature('')
@allure.story('')
@pytest.mark.parametrize(
    'email', [
        ('itsamono@gmail.com')
    ]
)
@pytest.mark.smoke
def test_click_btn_reset_in_subscribes_tab(authorized_user, email):
    """ Проверить, что по клику кнопки "Сброс" значения полей "Ваш e-mail, чекбоксов и радиокнопок" удаляются """
    account = AccountPage(authorized_user)

    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_subscribes()  # Кликаю по табу "Подписки"
    )

    #    Предусловие: Удалить значения в поле "Ваш e-mail" (сейчас оно по умолчанию предзаполнено)
    account.clear_email_field_in_subscribes_tab()

    (
        account.enter_email_in_subscribes_tab(email)
        .click_checkbox_rub_1_in_subscribes_tab()
        .click_checkbox_rub_2_in_subscribes_tab()
        .click_radio_button_1_in_subscribes_tab()
        .click_radio_button_2_in_subscribes_tab()
        .click_btn_reset_in_subscribes_tab()
    )

    #assert not account.is_field_filled(LocatorsForAccount.INPUT_EMAIL_IN_TAB_SUBSCRIBES), 'В поле "Ваш e-mail" есть данные!'
    assert not account.is_checkbox_checked(LocatorsForAccount.CHECKED_CHECKBOX_RUB_1_IN_TAB_SUBSCRIBES), 'В (первом) чекбоксе есть фложок!'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
@pytest.mark.parametrize(
    'email', [
        ('itsamono@gmail.com')
    ]
)
def test_check_error_1_in_subscribes_tab(authorized_user, email):
    """ Проверить отображение ошибки: "Необходимо указать хотя бы одну рубрику подписки." """
    account = AccountPage(authorized_user)

    (
        account.open_account_page()  # Открываю ЛК
        .click_tab_subscribes()  # Кликаю по табу "Подписки"
    )

    #    Проверить, что по клику "Добавить" без выбора рубрик подписки отображается ошибка: "Необходимо указать хотя бы одну рубрику подписки."
    (
        account.enter_email_in_subscribes_tab(email)
        .click_btn_add_in_subscribes_tab()
    )

    error_msg_1 = account.get_errors_in_subscribes_tab()#; print(f'\nТекст ошибки: {error_msg_1}')
    assert "рубрику подписки" in error_msg_1.lower(), f'Ожидали ошибку про рубрику подписки, получили: "{error_msg_1}"'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
@pytest.mark.parametrize(
    'email', [
        ('itsamonogmail.com')
    ]
)
@pytest.mark.smoke
def test_check_error_2_in_subscribes_tab(authorized_user, email):
    """ Проверить отображение ошибки: "Указан неверный адрес подписки" """
    account = AccountPage(authorized_user)

    (
        account.open_account_page()  # Открываю ЛК
        .click_tab_subscribes()  # Кликаю по табу "Подписки"
    )

    #    Проверить, что по клику "Добавить", указав некорректный формат почты отображается ошибка: "Указан неверный адрес подписки"
    (
        account.enter_email_in_subscribes_tab(email)
        .click_checkbox_rub_1_in_subscribes_tab()
        .click_btn_add_in_subscribes_tab()
    )

    error_msg_2 = account.get_errors_in_subscribes_tab()#; print(f'\nТекст ошибки: {error_msg_2}')
    assert "неверный адрес" in error_msg_2.lower(), f'Ожидали ошибку про неверный адрес, получили: "{error_msg_2}"'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
@pytest.mark.parametrize(
    'email', [
        ('itsamono@gmail.com')
    ]
)
@pytest.mark.smoke
def test_check_error_3_in_subscribes_tab(authorized_user, email):
    """ Проверить отображение ошибки: "Адрес подписки уже существует. Пожалуйста, укажите другой адрес." """
    account = AccountPage(authorized_user)

    (
        account.open_account_page()  # Открываю ЛК
        .click_tab_subscribes()  # Кликаю по табу "Подписки"
    )

    #    Проверить, что по клику "Добавить", указав уже используемую в рассылке почту отображается ошибка: "Адрес подписки уже существует. Пожалуйста, укажите другой адрес."
    (
        account.enter_email_in_subscribes_tab(email)
        .click_checkbox_rub_1_in_subscribes_tab()
        .click_btn_add_in_subscribes_tab()
    )

    error_msg_3 = account.get_errors_in_subscribes_tab()#; print(f'\nТекст ошибки: {error_msg_3}')
    assert "уже существует" in error_msg_3.lower(), f'Ожидали ошибку про рубрику подписки, получили: "{error_msg_3}"'


@allure.feature('')
@allure.story('')
@pytest.mark.parametrize(
    'email', [
        ('novikov@mail.ru')
    ]
)
@pytest.mark.skip    ### Этот тест создаёт подписку: скипаем, т.к. это продовый сайт и не надо им плодить в админке подписки-пустышки
def test_success_sub_in_subscribes_tab(authorized_user, email):
    """ Проверить успешность подписки на рассылку """
    account = AccountPage(authorized_user)

    (
        account.open_account_page()  # Открываю ЛК
        .click_tab_subscribes()  # Кликаю по табу "Подписки"
    )

    #    Предусловие: Удалить значения в поле "Ваш e-mail" (сейчас оно по умолчанию предзаполнено)
    account.clear_email_field_in_subscribes_tab()

    (
        account.enter_email_in_subscribes_tab(email)
        .click_checkbox_rub_1_in_subscribes_tab()
        .click_checkbox_rub_2_in_subscribes_tab()
        .click_radio_button_1_in_subscribes_tab()
        .click_radio_button_2_in_subscribes_tab()
        .click_btn_add_in_subscribes_tab()
    )

    msg_after_sub = account.get_success_msg_after_sub_in_subscribes_tab()#; print(f'\nСообщение: {msg_after_sub}')
    assert "код подтверждения" in msg_after_sub.lower(), f'Ожидали сообщение про код подтверждения, получили: "{msg_after_sub}"'

    assert account.is_block_verify_subscribe(), 'Блок "Подтверждение подписки" не появился на странице'
    title_1_block = account.get_title_1_success_msg_after_sub_in_subscribes_tab()#; print(f'\nЗаголовок блока_1: {title_1_block}')
    assert "подтверждение подписки" in title_1_block.lower(), f'Ожидали заголовок про подтверждение подписки, получили: "{title_1_block}"'

    assert account.is_block_status_subscribe(), 'Блок "Состояние подписки" не появился на странице'
    title_2_block = account.get_title_2_success_msg_after_sub_in_subscribes_tab()#; print(f'\nЗаголовок блока_2: {title_2_block}')
    assert "состояние подписки" in title_2_block.lower(), f'Ожидали заголовок про состояние подписки, получили: "{title_2_block}"'
