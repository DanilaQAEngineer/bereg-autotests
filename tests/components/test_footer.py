import allure
import pytest


from config.settings import settings
from pages.components.footer import FooterPage
from locators.components.footer_locators import LocatorsForFooterMenu


@allure.feature('Футер-меню')
@allure.story('')
@pytest.mark.smoke
def test_check_subscribes_in_footer(browser):
    """ Проверить, что в футере есть форма подписки на рассылку """
    footer = FooterPage(browser)

    #    Переходим на главную страницу сайта
    browser.get(settings.base_url)
    #    Предусловие: скроллим до футера:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    assert footer.is_visible_element(LocatorsForFooterMenu.TITLE_SUBSCRIBES_IN_FOOTER), 'Заголовка "Подписаться на новости и акции" в футере нет'
    assert footer.is_visible_element(LocatorsForFooterMenu.INPUT_EMAIL_IN_FOOTER), 'Поля ввода почты в футере нет'
    assert footer.is_visible_element(LocatorsForFooterMenu.BTN_SUBSCRIBES_IN_FOOTER), 'Кнопки "Подписаться" в футере нет'


@allure.feature('Футер-меню')
@allure.story('')
@pytest.mark.parametrize(
    'email', [
        ('itsamono@gmail.com')
    ]
)
@pytest.mark.smoke
def test_enter_email_for_subscribes_in_footer(browser, email):
    """ Проверить, что в поле с почтой доступен ввод данных """
    footer = FooterPage(browser)

    #    Переходим на главную страницу сайта
    browser.get(settings.base_url)
    #    Предусловие: скроллим до футера:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    footer.enter_text(LocatorsForFooterMenu.INPUT_EMAIL_IN_FOOTER, email)

    assert footer.is_field_filled(LocatorsForFooterMenu.INPUT_EMAIL_IN_FOOTER), 'Поле с почтой пустое'


@allure.feature('Модалка подписки на рассыку в футере')
@allure.story('')
@pytest.mark.smoke
def test_open_modal_subscribes(browser):
    """ Проверить, что по клику кнопки "Подписаться" открывается модалка подписки на рассылку """
    footer = FooterPage(browser)

    #    Переходим на главную страницу сайта
    browser.get(settings.base_url)
    #    Предусловие: скроллим до футера:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    footer.click_element(LocatorsForFooterMenu.BTN_SUBSCRIBES_IN_FOOTER)

    assert footer.is_visible_element(LocatorsForFooterMenu.MODAL_SUBSCRIBES), 'Модалка подписки на рассылку не открылась'
    title_modal = footer.check_text(LocatorsForFooterMenu.TITLE_IN_MODAL_SUBSCRIBES)#; print(f'\nЗаголовок модалки: {title_modal}')
    assert "подписка на рассылку" in title_modal.lower(), f'Ожидали заголовок про подписка на рассылку, получили: "{title_modal}"'
    assert footer.is_visible(LocatorsForFooterMenu.INPUT_EMAIL_IN_MODAL_SUBSCRIBES), 'Поле с почтой в модалке подписки отсутствует'
    assert footer.is_visible(LocatorsForFooterMenu.CHECKBOX_IN_MODAL_SUBSCRIBES), 'Чекбокс согласия с политикой сайта в модалке подписки отсутствует'
    assert footer.is_visible(LocatorsForFooterMenu.BTN_SUBSCRIBES_IN_MODAL_SUBSCRIBES), 'Кнопка "Подписаться" в модалке подписки отсутствует'
    assert footer.is_visible(LocatorsForFooterMenu.BTN_CLOSE_MODAL_SUBSCRIBES), 'Кнопка закрытия модалки в модалке подписки отсутствует'


@allure.feature('Модалка подписки на рассыку в футере')
@allure.story('')
@pytest.mark.smoke
def test_close_modal_subscribes(browser):
    """ Проверить, что по клику кнопки "Х" модалка подписки на рассылку закрывается """
    footer = FooterPage(browser)

    #    Переходим на главную страницу сайта
    browser.get(settings.base_url)
    #    Предусловие: скроллим до футера:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    footer.click_element(LocatorsForFooterMenu.BTN_SUBSCRIBES_IN_FOOTER)
    assert footer.is_visible_element(LocatorsForFooterMenu.MODAL_SUBSCRIBES), 'Модалка подписки на рассылку не открылась'

    footer.click_element(LocatorsForFooterMenu.BTN_CLOSE_MODAL_SUBSCRIBES)
    assert footer.wait_until_invisible(LocatorsForFooterMenu.MODAL_SUBSCRIBES), 'Модалка подписки на рассылку не закрылась'


@allure.feature('Модалка подписки на рассыку в футере')
@allure.story('')
@pytest.mark.parametrize(
    'email', [
        ('itsamono@gmail.com')
    ]
)
@pytest.mark.smoke
def test_enter_data_modal_subscribes(browser, email):
    """ Проверить, что в инпут-поля доступен ввод значений + Чекбоксы меняют состояние по клику """
    footer = FooterPage(browser)

    #    Переходим на главную страницу сайта
    browser.get(settings.base_url)
    #    Предусловие: скроллим до футера:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    (
        footer.click_element(LocatorsForFooterMenu.BTN_SUBSCRIBES_IN_FOOTER)
        .enter_text(LocatorsForFooterMenu.INPUT_EMAIL_IN_MODAL_SUBSCRIBES, email)
        .click_element(LocatorsForFooterMenu.CHECKBOX_IN_MODAL_SUBSCRIBES)
    )

    assert footer.is_field_filled(LocatorsForFooterMenu.INPUT_EMAIL_IN_MODAL_SUBSCRIBES), 'После ввода почты в поле не появилось значение'
    assert footer.is_checkbox_checked(LocatorsForFooterMenu.CHECKED_CHECKBOX_IN_MODAL_SUBSCRIBES), 'Флажок в чекбоксе не появился'


@allure.feature('Модалка подписки на рассыку в футере')
@allure.story('')
@pytest.mark.parametrize(
    'locator, expected_text, field_name',
    [
        (LocatorsForFooterMenu.ERROR_UNDER_INPUT_EMAIL_IN_MODAL_SUBSCRIBES, 'заполните это поле', 'Email'),
        (LocatorsForFooterMenu.ERROR_UNDER_CAPTCHA_IN_MODAL_SUBSCRIBES, 'пройдите проверку', 'Капча'),
        (LocatorsForFooterMenu.ERROR_UNDER_CHECKBOX_IN_MODAL_SUBSCRIBES, 'согласитесь с условиями', 'Чекбокс')
    ]
)
@pytest.mark.smoke
def test_check_all_errors_modal_subscribes(browser, locator, expected_text, field_name):
    """ Проверить, что по клику кнопки "Подписаться" (без заполнения всех обязательных полей) под полями отображаются ошибки """
    footer = FooterPage(browser)

    #    Переходим на главную страницу сайта
    browser.get(settings.base_url)
    #    Предусловие: скроллим до футера:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    (
        footer.enter_text(LocatorsForFooterMenu.INPUT_EMAIL_IN_MODAL_SUBSCRIBES, "invalid_email")  # прокинул в тест некорректную почту, чтоб наверняка ошибка появилась, т.к. временами падает
        .click_element(LocatorsForFooterMenu.BTN_SUBSCRIBES_IN_FOOTER)
        .click_element(LocatorsForFooterMenu.BTN_SUBSCRIBES_IN_MODAL_SUBSCRIBES)
    )

    error_msg = footer.check_errors(locator)
    assert expected_text in error_msg.lower(), f'Ожидаемый текст ошибки "{expected_text}" под полем "{field_name}", получили: "{error_msg}"'


@allure.feature('Модалка подписки на рассыку в футере')
@allure.story('')
@pytest.mark.parametrize(
    'email',
    [
        ('abcdgmail.com'),
        ('абвгд@mail.ru')
    ]
)
@pytest.mark.smoke
def test_check_errors_email_modal_subscribes(browser, email):
    """ Проверить, что при вводе некорректной почты под полем "E-mail" отображается ошибка: "Неверный формат!" """
    footer = FooterPage(browser)

    #    Переходим на главную страницу сайта
    browser.get(settings.base_url)
    #    Предусловие: скроллим до футера:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    (
        footer.click_element(LocatorsForFooterMenu.BTN_SUBSCRIBES_IN_FOOTER)
        .enter_text(LocatorsForFooterMenu.INPUT_EMAIL_IN_MODAL_SUBSCRIBES, email)
        .click_element(LocatorsForFooterMenu.BTN_SUBSCRIBES_IN_MODAL_SUBSCRIBES)
    )

    error_msg = footer.check_errors(LocatorsForFooterMenu.ERROR_UNDER_INPUT_EMAIL_IN_MODAL_SUBSCRIBES)
    assert 'неверный формат' in error_msg.lower(), f'Ожидали ошибку про неверный формат, получили: "{error_msg}"'
