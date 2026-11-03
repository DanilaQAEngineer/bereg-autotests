import pytest


from pages.catalog.listing_page import ListingPage
from pages.components.header import HeaderComponents


@pytest.mark.smoke
def test_search_results_page_has_products(browser):
    """
        Проверить, что:
            на странице с результатами поиска действительно есть карточки товаров
    """

    page = ListingPage(browser)
    page.open_search_results_page('Палатка')

    #    1. Проверяю, что на странице с результатами есть карточки товаров:
    count = page.get_product_count(); print(f'\nПо запросу "Палатка" на странице с результатами отображается {count} товаров')
    assert count > 0, 'На странице с результатами нет карточек товаров'


@pytest.mark.smoke
def test_search_results_asc_sorting_by_price(browser):
    """
        Проверить, что:
            на странице с результатами поиска корректно работает ASC-сортировка "Сначала дешёвые"
    """

    page = ListingPage(browser)
    page.open_search_results_page('Палатка')

    #    Сортирую по убыванию цены, используя ТОТ ЖЕ компонент, что и в категориях
    page.sort_panel.click_sort_button_on_result_search_page()
    page.sort_panel.select_asc_sort_price()

    #    Собираю цены на странице и убеждаюсь, что карточки на странице отображаются от самой дешёвой к самой дорогой:
    prices = page.sort_panel.get_all_prices_as_floats(); print(f'\nЦены товаров на странице: {prices}')
    assert len(prices) > 0, "Не удалось собрать цены на странице поиска"
    assert prices == sorted(prices, reverse=False), 'ASC-сортировка "Сначала дешёвые" не работает'


@pytest.mark.smoke
def test_search_results_desc_sorting_by_price(browser):
    """
        Проверить, что:
            на странице с результатами поиска корректно работает DESC-сортировка "Сначала дорогие"
    """

    page = ListingPage(browser)
    page.open_search_results_page('Палатка')

    #    Сортирую по убыванию цены, используя ТОТ ЖЕ компонент, что и в категориях
    page.sort_panel.click_sort_button_on_result_search_page()
    page.sort_panel.select_desc_sort_price()

    #    Собираю цены на странице и убеждаюсь, что карточки на странице отображаются от самой дорогой к самой дешёвой:
    prices = page.sort_panel.get_all_prices_as_floats(); print(f'\nЦены товаров на странице: {prices}')
    assert len(prices) > 0, "Не удалось собрать цены на странице поиска"
    assert prices == sorted(prices, reverse=True), 'DESC-сортировка "Сначала дорогие" не работает'