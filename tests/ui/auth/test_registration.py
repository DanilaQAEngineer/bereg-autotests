import allure
import pytest


from config.settings import settings
from pages.components.header import HeaderComponents
from pages.components.auth_modal import AuthModalComponent
from pages.auth.register_page import RegisterPage
from locators.components.auth_locators import LocatorsForAuthModal


@allure.feature('Регистрация')
@allure.story('Открытие страницы регистрации')
@pytest.mark.smoke
def test_open_registration_page(browser):
    """ Проверить, что по клику кнопки "Регистрация" открывается страница с формой регистрации на сайте """
    header = HeaderComponents(browser)
    auth = AuthModalComponent(browser)
    registration = RegisterPage(browser)

    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    header.click_voity_button()  # Жмём кнопку "Войти" в хедере
    auth.click_element(LocatorsForAuthModal.BTN_REGISTRATION)  # В модалке "Вход в личный кабинет" жмём кнопку "Регистрация"

    assert "/auth/registration/" in browser.current_url, 'Переход на страницу "Регистрация" не произошел'
    assert registration.is_visible_element(LocatorsForAuthModal.BREADCRUMBS_IN_REGISTRATION_PAGE), 'Хлебных крошек на странице нет'
    assert "регистрация" in registration.check_text(LocatorsForAuthModal.TITLE_IN_REGISTRATION_PAGE).lower(), f'Ожидали заголовок про регистрация, получили: "{registration.check_text(LocatorsForAuthModal.TITLE_IN_REGISTRATION_PAGE).lower()}"'
    assert registration.is_visible_element(LocatorsForAuthModal.INPUT_FIO_IN_REGISTRATION_PAGE), 'Поля "ФИО" на странице нет'
    assert registration.is_visible_element(LocatorsForAuthModal.INPUT_EMAIL_IN_REGISTRATION_PAGE), 'Поля "E-mail" на странице нет'
    assert registration.is_visible_element(LocatorsForAuthModal.INPUT_PHONE_IN_REGISTRATION_PAGE), 'Поля "Телефон" на странице нет'
    assert registration.is_visible_element(LocatorsForAuthModal.INPUT_PASSWORD_IN_REGISTRATION_PAGE), 'Поля "Пароль" на странице нет'
    assert registration.is_visible_element(LocatorsForAuthModal.INPUT_CONFIRM_PASSWORD_IN_REGISTRATION_PAGE), 'Поля "Подтверждение пароля" на странице нет'
    assert registration.is_visible_element(LocatorsForAuthModal.CHECKBOX_1_IN_REGISTRATION_PAGE), 'Первого чекбокса на странице нет'
    assert registration.is_visible_element(LocatorsForAuthModal.CHECKBOX_2_IN_REGISTRATION_PAGE), 'Второго чекбокса на странице нет'
    assert registration.is_visible_element(LocatorsForAuthModal.BTN_REGISTRATION_IN_REGISTRATION_PAGE), 'Кнопки "Зарегистрироваться" на странице нет'


@allure.feature('Регистрация')
@allure.story('Успешное заполнение формы регистрации')
@pytest.mark.parametrize(
    'fio, email, phone, password, confirm_password', [
        ('Тестов Тест Тестович', 'itsamono@gmail.com', '89294336688', 'Parol_808', 'Parol_808')
    ]
)
@pytest.mark.smoke
def test_enter_data(browser, fio, email, phone, password, confirm_password):
    """ Проверить, что в поля можно ввести данные + Доступен клик по чекбоксам """
    header = HeaderComponents(browser)
    auth = AuthModalComponent(browser)
    registration = RegisterPage(browser)

    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    header.click_voity_button()  # Жмём кнопку "Войти" в хедере
    auth.click_element(LocatorsForAuthModal.BTN_REGISTRATION)  # В модалке "Вход в личный кабинет" жмём кнопку "Регистрация"

    (
        registration.click_element(LocatorsForAuthModal.CHECKBOX_2_IN_REGISTRATION_PAGE)  # Снимаю чекбокс у второго поля
        .enter_text(LocatorsForAuthModal.INPUT_FIO_IN_REGISTRATION_PAGE, fio)  # Заполняю поле "ФИО"
        .enter_text(LocatorsForAuthModal.INPUT_EMAIL_IN_REGISTRATION_PAGE, email)  # Заполняю поле "E-mail"
        .enter_text(LocatorsForAuthModal.INPUT_PHONE_IN_REGISTRATION_PAGE, phone)  # Заполняю поле "Телефон"
        .enter_text(LocatorsForAuthModal.INPUT_PASSWORD_IN_REGISTRATION_PAGE, password)  # Заполняю поле "Пароль"
        .enter_text(LocatorsForAuthModal.INPUT_CONFIRM_PASSWORD_IN_REGISTRATION_PAGE, confirm_password)  # Заполняю поле "Подтверждение пароля"
        .click_element(LocatorsForAuthModal.CHECKBOX_1_IN_REGISTRATION_PAGE)  # Кликаю по первому чекбоксу
        .click_element(LocatorsForAuthModal.CHECKBOX_2_IN_REGISTRATION_PAGE)  # Кликаю по второму чекбоксу
    )

    assert registration.is_field_filled(LocatorsForAuthModal.INPUT_FIO_IN_REGISTRATION_PAGE), 'Поле ФИО осталось пустым после ввода!'
    assert registration.is_field_filled(LocatorsForAuthModal.INPUT_EMAIL_IN_REGISTRATION_PAGE), 'Поле Email осталось пустым после ввода!'
    assert registration.is_field_filled(LocatorsForAuthModal.INPUT_PHONE_IN_REGISTRATION_PAGE), 'Поле Телефон осталось пустым после ввода!'
    assert registration.is_field_filled(LocatorsForAuthModal.INPUT_PASSWORD_IN_REGISTRATION_PAGE), 'Поле Пароль осталось пустым после ввода!'
    assert registration.is_field_filled(LocatorsForAuthModal.INPUT_CONFIRM_PASSWORD_IN_REGISTRATION_PAGE), 'Поле Подтверждение пароля осталось пустым после ввода!'
    assert registration.is_checkbox_checked(LocatorsForAuthModal.CHECK_CHECKBOX_1), 'В первом чекбоксе нет флажка'
    assert registration.is_checkbox_checked(LocatorsForAuthModal.CHECK_CHECKBOX_2), 'Во втором чекбоксе нет флажка'


@allure.feature('Регистрация')
@allure.story('Валидация обязательных полей')
@pytest.mark.parametrize(
    'locator, expected_text, field_name',
    [
        (LocatorsForAuthModal.ERROR_MSG_UNDER_INPUT_FIO_IN_REGISTRATION_PAGE, 'заполните это поле', 'ФИО'),
        (LocatorsForAuthModal.ERROR_MSG_UNDER_INPUT_EMAIL_IN_REGISTRATION_PAGE, 'заполните это поле', 'Email'),
        (LocatorsForAuthModal.ERROR_MSG_UNDER_INPUT_PASSWORD_IN_REGISTRATION_PAGE, 'заполните это поле', 'Пароль'),
        (LocatorsForAuthModal.ERROR_MSG_UNDER_INPUT_CONFIRM_PASSWORD_IN_REGISTRATION_PAGE, 'заполните это поле', 'Подтверждение пароля'),
        (LocatorsForAuthModal.ERROR_MSG_UNDER_INPUT_CAPTCHA_IN_REGISTRATION_PAGE, 'пройдите проверку', 'Капча'),
        (LocatorsForAuthModal.ERROR_MSG_UNDER_CHECKBOX_1_IN_REGISTRATION_PAGE, 'согласитесь с условиями', 'Чекбокс 1'),
        (LocatorsForAuthModal.ERROR_MSG_UNDER_CHECKBOX_2_IN_REGISTRATION_PAGE, 'заполните это поле', 'Чекбокс 2')
    ]
)
@pytest.mark.smoke
def test_check_all_errors(browser, locator, expected_text, field_name):
    """ Проверить, что по клику кнопки "Регистрация" (без заполнения всех обязательных полей) под полями отображаются ошибки """
    header = HeaderComponents(browser)
    auth = AuthModalComponent(browser)
    registration = RegisterPage(browser)

    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    header.click_voity_button()  # Жмём кнопку "Войти" в хедере
    auth.click_element(LocatorsForAuthModal.BTN_REGISTRATION)  # В модалке "Вход в личный кабинет" жмём кнопку "Регистрация"

    (
        registration.click_element(LocatorsForAuthModal.CHECKBOX_2_IN_REGISTRATION_PAGE)  # Снимаю чекбокс у второго поля
        .click_element(LocatorsForAuthModal.BTN_REGISTRATION_IN_REGISTRATION_PAGE)  # Кликаю по кнопке "Зарегистрироваться"
    )

    error_msg = registration.check_errors(locator)
    assert expected_text in error_msg.lower(), f'Ожидаемый текст ошибки "{expected_text}" под полем "{field_name}", получили: "{error_msg}"'


@allure.feature('Регистрация')
@allure.story('Валидация обязательных полей')
@pytest.mark.parametrize(
    'email',
    [
        ('abcdgmail.com'),
        ('абвгд@mail.ru')
    ]
)
@pytest.mark.smoke
def test_check_errors_email(browser, email):
    """ Проверить, что при вводе некорректной почты под полем "E-mail" отображается ошибка: "Неверный формат!" """
    header = HeaderComponents(browser)
    auth = AuthModalComponent(browser)
    registration = RegisterPage(browser)

    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    header.click_voity_button()  # Жмём кнопку "Войти" в хедере
    auth.click_element(LocatorsForAuthModal.BTN_REGISTRATION)  # В модалке "Вход в личный кабинет" жмём кнопку "Регистрация"

    (
        registration.enter_text(LocatorsForAuthModal.INPUT_EMAIL_IN_REGISTRATION_PAGE, email)
        .click_element(LocatorsForAuthModal.BTN_REGISTRATION_IN_REGISTRATION_PAGE)  # Кликаю по кнопке "Зарегистрироваться"
    )

    error_msg = registration.check_errors(LocatorsForAuthModal.ERROR_MSG_UNDER_INPUT_EMAIL_IN_REGISTRATION_PAGE)
    assert 'неверный формат' in error_msg.lower(), f'Ожидали ошибку про неверный формат, получили: "{error_msg}"'


@allure.feature('Регистрация')
@allure.story('Валидация поля "Телефон"')
@pytest.mark.parametrize(
    'phone, expected_error_text',
    [
        ('7929433', 'номер слишком короткий'),  # Номер короткий
        ('792943355111', 'неверный номер'),  # Неверный номер
        ('79292929292929292', 'номер слишком длинный')  # Номер длинный
    ]
)
@pytest.mark.smoke
def test_check_errors_phone(browser, phone, expected_error_text):
    """ Проверить, что при вводе некорректного номера под полем "Телефон" отображаются ошибки: "Номер слишком короткий, Неверный номер, Номер слишком длинный" """
    header = HeaderComponents(browser)
    auth = AuthModalComponent(browser)
    registration = RegisterPage(browser)

    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    header.click_voity_button()  # Жмём кнопку "Войти" в хедере
    auth.click_element(LocatorsForAuthModal.BTN_REGISTRATION)  # В модалке "Вход в личный кабинет" жмём кнопку "Регистрация"

    (
        registration.enter_text(LocatorsForAuthModal.INPUT_PHONE_IN_REGISTRATION_PAGE, phone)
        .click_element(LocatorsForAuthModal.BTN_REGISTRATION_IN_REGISTRATION_PAGE)  # Кликаю по кнопке "Зарегистрироваться"
    )

    error_msg = registration.check_errors(LocatorsForAuthModal.ERROR_MSG_UNDER_INPUT_PHONE_IN_REGISTRATION_PAGE)
    assert expected_error_text in error_msg.lower(), f'Под полем "Телефон" ожидали ошибку "{expected_error_text}", получили: "{error_msg}"'


@allure.feature('Регистрация')
@allure.story('Валидация поля "Телефон"')
@pytest.mark.parametrize(
    'password, expected_error_text',
    [
        ('Parol', 'минимум 6 символов')  # Пароль короткий
    ]
)
@pytest.mark.smoke
def test_check_errors_password(browser, password, expected_error_text):
    """ Проверить, что при вводе короткого пароля под полем "Пароль" отображается ошибка: "Минимум 6 символов!" """
    header = HeaderComponents(browser)
    auth = AuthModalComponent(browser)
    registration = RegisterPage(browser)

    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    header.click_voity_button()  # Жмём кнопку "Войти" в хедере
    auth.click_element(LocatorsForAuthModal.BTN_REGISTRATION)  # В модалке "Вход в личный кабинет" жмём кнопку "Регистрация"

    (
        registration.enter_text(LocatorsForAuthModal.INPUT_PASSWORD_IN_REGISTRATION_PAGE, password)
        .click_element(LocatorsForAuthModal.BTN_REGISTRATION_IN_REGISTRATION_PAGE)  # Кликаю по кнопке "Зарегистрироваться"
    )

    error_msg = registration.check_errors(LocatorsForAuthModal.ERROR_MSG_UNDER_INPUT_PASSWORD_IN_REGISTRATION_PAGE)
    assert expected_error_text in error_msg.lower(), f'Под полем "Пароль" ожидали ошибку "{expected_error_text}", получили: "{error_msg}"'


@allure.feature('Регистрация')
@allure.story('Валидация поля "Телефон"')
@pytest.mark.parametrize(
    'password, confirm_password, expected_error_text',
    [
        ('Parol_808', 'Parol_809', 'пароли не совпадают')  # Разные пароли
    ]
)
@pytest.mark.smoke
def test_check_errors_confirm_password(browser, password, confirm_password, expected_error_text):
    """ Проверить, что при вводе разных паролей под полем "Подтверждение пароля" отображаются ошибки: "Пароли не совпадают!" """
    header = HeaderComponents(browser)
    auth = AuthModalComponent(browser)
    registration = RegisterPage(browser)

    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    header.click_voity_button()  # Жмём кнопку "Войти" в хедере
    auth.click_element(LocatorsForAuthModal.BTN_REGISTRATION)  # В модалке "Вход в личный кабинет" жмём кнопку "Регистрация"

    (
        registration.enter_text(LocatorsForAuthModal.INPUT_PASSWORD_IN_REGISTRATION_PAGE, password)
        .enter_text(LocatorsForAuthModal.INPUT_CONFIRM_PASSWORD_IN_REGISTRATION_PAGE, confirm_password)
        .click_element(LocatorsForAuthModal.BTN_REGISTRATION_IN_REGISTRATION_PAGE)  # Кликаю по кнопке "Зарегистрироваться"
    )

    error_msg = registration.check_errors(LocatorsForAuthModal.ERROR_MSG_UNDER_INPUT_CONFIRM_PASSWORD_IN_REGISTRATION_PAGE)
    assert expected_error_text in error_msg.lower(), f'Под полем "Подтверждение пароля" ожидали ошибку "{expected_error_text}", получили: "{error_msg}"'