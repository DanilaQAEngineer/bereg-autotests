import pytest


from pages.components.header import HeaderComponents
from pages.components.auth_modal import AuthModalComponent


@pytest.mark.smoke
def test_uncorrected_authorization(browser):
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
