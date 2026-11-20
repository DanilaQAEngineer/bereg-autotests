import allure
import pytest


from config.settings import settings
from pages.base_page import BasePage
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
    page_title = registration.check_text(LocatorsForAuthModal.TITLE_IN_REGISTRATION_PAGE)#; print(f'Заголовок на странице раздела: {page_title}')
    assert "регистрация" in page_title.lower(), f'Ожидали заголовок про регистрация, получили: "{page_title}"'


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
        (LocatorsForAuthModal.ERROR_MSG_UNDER_CHECKBOX_2_IN_REGISTRATION_PAGE, 'заполните это поле', 'Чекбокс 2'),
    ]
)
@pytest.mark.smoke
def test_check_errors(browser, locator, expected_text, field_name):
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


### ДОБАВИТЬ ТЕСТОВ ДЛЯ ОШИБОК: ПАРОЛЬ ДЛИННЫЙ/КОРОТКИ И Т.П. ###


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
