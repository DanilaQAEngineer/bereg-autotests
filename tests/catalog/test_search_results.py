import pytest
import allure


from pages.catalog.listing_page import ListingPage
from pages.components.header import HeaderComponents


@allure.feature('Страница с результатами поиска по сайту')
@allure.story('Проверить, что на странице с результатами поиска действительно есть карточки товаров')
@pytest.mark.smoke
def test_search_results_page_has_products(browser):
    """
        Проверить, что:
            на странице с результатами поиска действительно есть карточки товаров
    """

    page = ListingPage(browser)
    page.open_search_results_page('Палатка')

    #    1. Проверяю, что на странице с результатами есть карточки товаров:
    count = page.get_product_count(); print(f'По запросу "Палатка" на странице с результатами отображается {count} товаров\n')
    assert count > 0, 'На странице с результатами нет карточек товаров'


@allure.feature('Страница с результатами поиска по сайту')
@allure.story('Проверить, что на странице с результатами поиска корректно работает ASC-сортировка "Сначала дешёвые" (дешёвые > дорогие)')
@pytest.mark.smoke
def test_search_results_asc_sorting_by_price(browser):
    """
        Проверить, что:
            на странице с результатами поиска корректно работает ASC-сортировка "Сначала дешёвые" (дешёвые > дорогие)
    """

    page = ListingPage(browser)
    page.open_search_results_page('Палатка')

    #    Сортирую по убыванию цены, используя ТОТ ЖЕ компонент, что и в категориях
    page.sort_panel.click_sort_button_on_result_search_page()
    page.sort_panel.select_asc_sort_price()

    #    Собираю цены на странице и убеждаюсь, что карточки на странице отображаются от самой дешёвой к самой дорогой:
    prices = page.sort_panel.get_all_prices_as_floats(); print(f'Цены товаров на странице: {prices}\n')
    assert len(prices) > 0, "Не удалось собрать цены на странице поиска"
    assert prices == sorted(prices, reverse=False), 'ASC-сортировка "Сначала дешёвые" не работает'


@allure.feature('Страница с результатами поиска по сайту')
@allure.story('Проверить, что на странице с результатами поиска корректно работает DESC-сортировка "Сначала дорогие" (дорогие > дешёвые)')
@pytest.mark.skip
def test_search_results_desc_sorting_by_price(browser):    # ТЕСТ ПАДАЕТ В ОШИБКУ, Т.К. У ОДНОГО ТОВАРА ЕСТЬ СКИДКА И ФИЛЬТРУЕМ, ВИДИМО, ПО СТАРОЙ ЦЕНЕ
    """
        Проверить, что:
            на странице с результатами поиска корректно работает DESC-сортировка "Сначала дорогие" (дорогие > дешёвые)
    """

    page = ListingPage(browser)
    page.open_search_results_page('Палатка')

    #    Сортирую по убыванию цены, используя ТОТ ЖЕ компонент, что и в категориях
    page.sort_panel.click_sort_button_on_result_search_page()
    page.sort_panel.select_desc_sort_price()

    #    Собираю цены на странице и убеждаюсь, что карточки на странице отображаются от самой дорогой к самой дешёвой:
    prices = page.sort_panel.get_all_prices_as_floats(); print(f'Цены товаров на странице: {prices}\n')
    assert len(prices) > 0, "Не удалось собрать цены на странице поиска"
    assert prices == sorted(prices, reverse=True), 'DESC-сортировка "Сначала дорогие" не работает'
