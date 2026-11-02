import pytest
import time


from config.settings import settings
from locators.components.header_locators import LocatorsForHeader
from pages.components.header import HeaderComponents


#    smoke-тесты для функционала хедера:
@pytest.mark.smoke
def test_header_logo_navigation(browser):
    """
    Проверить, что:
        по клику на лого в хедере открывается главная страница сайта https://pfbereg.ru/
    """

    # Предварительные шаги до начала тестирования:
    browser.get(f'{settings.base_url}/catalog/')     # Сперва открываю любую страницу != https://pfbereg.ru/
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

    header.open_main_page()    # Вызываю метод раскрытия выпадающего меню "Номер телефона" в хедере

    # Проверяю, что до наведения курсора на номер в хедере кнопки "Заказать звонок" нет
    assert not header.is_call_request_visible(), "Кнопка 'Заказать звонок' видна до наведения курсора"

    header.hover_phone()

    # После наведения курсора кнопка должна появиться
    assert header.is_call_request_visible(), "Кнопка 'Заказать звонок' не появилась"


@pytest.mark.smoke
def test_check_search_dropdown(browser):
    """
        Проверить, что:
            1) при вводе действительного значения в поисковую строку появляется выпадающий список с результатами поиска
            2) в выпадающем_результирующем списке действительно есть карточки товаров
    """

    header = HeaderComponents(browser)

    (
        header.open_main_page()
        .search_input('Палатка')
    )

    #    1. Проверяю, что выпадающий_результирующий список появился на странице
    assert header.is_search_dropdown_result_visible(), 'Выпадающий список с результатами поиска отсутствует'

    #    2. Проверяю, что в выпадающем_результирующем списке действительно есть карточки товаров
    count_tovarov = header.get_search_results_count()#; print(f"В выпадающем_результирующем списке {count_tovarov} карточек товаров")    # Выведется при запуске с флагом -s
    assert count_tovarov > 0, 'В выпадающем_результирующем списке нет карточек товаров'


@pytest.mark.smoke
def test_click_clear_button_in_search(browser):
    """
        Проверить, что:
            запрос из поисковой строки удаляется по клику кнопки "х" (очистить поле)
    """

    header = HeaderComponents(browser)

    (
        header.open_main_page()
        .search_input('Палатка')
    )

    #    Проверяю, что в поисковой строке появился запрос:
    assert header.get_search_input_value() != '', 'В поисковой строке нет запроса'
    # assert header.get_search_input_value() == "Палатка", 'В поисковой строке нет запроса "Палатка"'

    header.click_clear_button()

    #    Проверяю, что по клику "х" запрос удалился из поисковой строки:
    assert header.get_search_input_value() == '', 'Клик по кнопке "х" не сработал: в поисковой строке есть запрос'
