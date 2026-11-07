import os
import pytest
import allure
from dotenv import load_dotenv


from pages.components.header import HeaderComponents
from pages.components.auth_modal import AuthModalComponent


load_dotenv()    # Функция, позволяющая читать файлы .env (по умолчанию Python не видит их) и добавлять все пары КЛЮЧ=ЗНАЧЕНИЕ в системные переменные окружения процесса


@allure.feature('Авторизация на сайте')
@allure.story('Проверить, что при вводе действительных данных происходит авторизация на сайте')
@pytest.mark.smoke
def test_correct_authorization(browser):
    """
        Проверить, что:
            при вводе действительных данных происходит авторизация на сайте:
                1. в правом верхнем углу страницы появляется уведомление об успешности авторизации
                ### 2. по клику кнопки "Войти" в хедере открывается страница личного кабинета == ОПИСАТЬ ЭТУ ПРОВЕРКУ, пока не реализовал
    """

    header = HeaderComponents(browser)
    auth_modal = AuthModalComponent(browser)
    true_login = os.getenv('TEST_USER_EMAIL', '')    # Прокидываю корректный логин из файла .env (в него скопипастил из .env.example): os.getenv() ищет все пары КЛЮЧ-ЗНАЧЕНИЕ
    true_password = os.getenv('TEST_USER_PASSWORD', '')    # Прокидываю корректный пароль из файла .env (в него скопипастил из .env.example): os.getenv() ищет все пары КЛЮЧ-ЗНАЧЕНИЕ

    (
        header.open_main_page()    # Предусловие: перейти на сам сайт
        .click_voity_button()    # Нажимаю кнопку "Войти" в хедере
    )

    (
        auth_modal.enter_login(true_login)    # Ввожу корректный логин
        .enter_password(true_password)    # Ввожу корректный пароль
        .click_auth_button()    # Нажимаю кнопку "Войти"
    )

    #login_email = login; print(f'\nЛогин, указанный при авторизации: {login_email}')
    #title_notification_after_auth = auth_modal.check_title_notification_after_auth(); print(f'Заголовок уведомления: {title_notification_after_auth}')

    assert auth_modal.check_notification_after_auth(), 'Уведомление об успешной авторизации отсутствует'
    assert auth_modal.check_title_notification_after_auth() != '', 'Заголовок в уведомлении отсутствует, либо пустой'
    assert auth_modal.check_email_notification_after_auth() == true_login, 'Почта в уведомлении != логину, указанному при авторизации'


@allure.feature('Авторизация на сайте')
@allure.story('Проверить, что при авторизации с недействительными данными в модалке авторизации отображается уведомление: "Неверный логин или пароль."')
@pytest.mark.smoke
@pytest.mark.parametrize(
    'login, password', [
        ('itsamono@gmail.com', 'parol_808'),    # Корректный логин + Некорректный пароль
        ('itsamon@gmail.com', 'Parol_808'),    # Некорректный логин + Корректный пароль
        ('itsamon@gmail.com', 'parol_808')    # Некорректный логин + Некорректный пароль
    ]
)
def test_authorization_with_invalid_data(browser, login, password):
    """
        Проверить, что:
            при авторизации с недействительными данными в модалке авторизации отображается уведомление: "Неверный логин или пароль."
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


@allure.feature('Авторизация на сайте')
@allure.story('Проверить, что авторизация недоступна, если обязательные поля не заполнены: под пустыми полями есть сообщение: "Заполните это поле!"')
@pytest.mark.smoke
def test_authorization_with_empty_required_fields(browser):
    """
        Проверить, что:
            авторизация недоступна, если обязательные поля не заполнены: под пустыми полями есть сообщение: "Заполните это поле!"
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
