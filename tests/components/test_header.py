import pytest
import time

from config.settings import settings
from locators.components.header_locators import LocatorsForHeader
from pages.components.header import HeaderComponents


@pytest.mark.smoke
def test_header_city_modal(browser):
    """
    Проверить, что:
        по клику на лого в хедере открывается главная страница сайта
    """

    # Предварительные шаги до начала тестирования:
    browser.get(f'{settings.base_url}/catalog/')     # Сперва открываю любую страницу
    header = HeaderComponents(browser)

    url_before_click_logo = browser.current_url#; print(f'\nURL`а до клика по лого: {url_before_click_logo}')

    header.click_logo()

    url_after_click_logo = browser.current_url#; print(f'URL`а после клика по лого: {url_after_click_logo}')

    assert url_before_click_logo != url_after_click_logo, "URL`а не изменилась"


@pytest.mark.smoke
def test_header_city_modal(browser):
    """
    Проверить, что:
        по клику "Выбрать город" в хедере открывается модалка выбора города
    """

    header = HeaderComponents(browser)

    (
        header.open_main_page()
        .open_city_modal()
    )

    assert header.is_visible(LocatorsForHeader.CITY_MODAL), "Модалка выбора города не открылась"


@pytest.mark.smoke
def test_header_call_request_hover(browser):
    """
    Проверить, что:
        при наведении курсора на номер в хедере открывается выпадашка, в которой есть кнопка "Заказать звонок"
    """

    header = HeaderComponents(browser)

    header.open_main_page()

    # Проверяю, что до наведения курсора на номер в хедере кнопки "Заказать звонок" нет
    assert not header.is_call_request_visible(), "Кнопка 'Заказать звонок' видна до наведения курсора"

    header.hover_phone()

    # После наведения курсора кнопка должна появиться
    assert header.is_call_request_visible(), "Кнопка 'Заказать звонок' не появилась"
