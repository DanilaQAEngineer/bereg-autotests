import pytest
from pages.catalog.listing_page import ListingPage


@pytest.mark.smoke
def test_desc_sort_by_price(browser):
    """
        Проверить, что:
            DESC-сортировка по параметру "Сначала дорогие" работает корректно
    """

    page = ListingPage(browser)

    (
        page.open_page_category_with_sort_and_cart()
    )

    #    1. Проверяю, что товары вообще есть на странице:
    assert page.get_product_count() > 0, 'На странице раздела нет карточек товаров'

    #    2. Выполняю сортировку, используя компонент "SortPanelComponent" == page.sort_panel.нужный метод:

    page.sort_panel.click_sort_button()
    page.sort_panel.select_desc_sort_price()

    #    3. Собираю цены на странице и убеждаюсь, что карточки на странице отображаются от самой дорогой к самой дешёвой:
    prices = page.sort_panel.get_all_prices_as_floats(); print(f'\nЦены товаров на странице: {prices}')
    assert prices == sorted(prices, reverse=True), 'DESC-сортировка "Сначала дорогие" не работает'
