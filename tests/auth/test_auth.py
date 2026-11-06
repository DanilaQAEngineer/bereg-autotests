import pytest


from pages.components.header import HeaderComponents
from pages.components.auth_modal import AuthModalComponent

@pytest.mark.smoke
@pytest.mark.parametrize(
    'login, password', [
        ('itsamono@gmail.com', 'parol_808'),    # Корректный логин + Некорректный пароль
        ('itsamon@gmail.com', 'Parol_808'),    # Некорректный логин + Корректный пароль
        ('itsamon@gmail.com', 'parol_808')    # Некорректный логин + Некорректный пароль
    ]
)
def test_check_error_notification(browser, login, password):
    """
        Проверить, что:
            при авторизации с недействительными данными отображается уведомление: "Неверный логин или пароль."
    """

    header = HeaderComponents(browser)
    auth_modal = AuthModalComponent(browser)

    (
        header.open_main_page()    # Предусловие: перейти на сам сайт
        .click_voity_button()    # Нажимаю кнопку "Войти" в хедере
    )

    (
        auth_modal.enter_login(login)    # Ввожу логин
        .enter_password(password)    # Ввожу пароль
        .click_auth_button()    # Нажимаю кнопку "Войти"
    )

    assert auth_modal.check_error_notification(), 'Уведомление о не успешности авторизации отсутствует'


@pytest.mark.smoke
def test_check_error_messages(browser):
    """
        Проверить, что:
            авторизация недоступна, если обязательные поля не заполнены
    """

    header = HeaderComponents(browser)
    auth_modal = AuthModalComponent(browser)

    (
        header.open_main_page()    # Предусловие: перейти на сам сайт
        .click_voity_button()    # Нажимаю кнопку "Войти" в хедере
    )

    auth_modal.click_auth_button()

    assert auth_modal.check_error_message_login(), 'Под полем "Логин" отсутствует сообщение об ошибке'
    assert auth_modal.check_error_message_password(), 'Под полем "Пароль" отсутствует сообщение об ошибке'
