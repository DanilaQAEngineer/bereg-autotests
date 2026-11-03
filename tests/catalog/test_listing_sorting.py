import pytest


from pages.catalog.listing_page import ListingPage


@pytest.mark.smoke
def test_asc_sort_by_price(browser):
    """
        Проверить, что:
            ASC-сортировка по параметру "Сначала дешёвые" работает корректно -- эта сортировка применяется на странице по умолчанию, ничего выбирать не нужно (просто убедиться, что она работает корректно)
    """

    page = ListingPage(browser)

    (
        page.open_page_category_with_sorting_filters()
    )

    #    1. Проверяю, что на странице раздела есть карточки товаров:
    assert page.get_product_count() > 0, 'На странице раздела нет карточек товаров'

    #    2. Собираю цены на странице и убеждаюсь, что карточки на странице отображаются от самой дешёвой к самой дорогой:
    prices = page.sort_panel.get_all_prices_as_floats()#; print(f'\nЦены товаров на странице: {prices}')
    assert prices == sorted(prices, reverse=False), 'ASC-сортировка "Сначала дешёвые" не работает'

@pytest.mark.smoke
def test_desc_sort_by_price(browser):
    """
        Проверить, что:
            DESC-сортировка по параметру "Сначала дорогие" работает корректно
    """

    page = ListingPage(browser)

    (
        page.open_page_category_with_sorting_filters()
    )

    #    1. Проверяю, что на странице раздела есть карточки товаров:
    assert page.get_product_count() > 0, 'На странице раздела нет карточек товаров'

    #    2. Выполняю сортировку, используя компонент "SortPanelComponent" == page.sort_panel.нужный метод:

    (
        page.sort_panel.click_sort_button_on_catalog_page()
        .select_desc_sort_price()
    )

    #    3. Собираю цены на странице и убеждаюсь, что карточки на странице отображаются от самой дорогой к самой дешёвой:
    prices = page.sort_panel.get_all_prices_as_floats()#; print(f'\nЦены товаров на странице: {prices}')
    assert prices == sorted(prices, reverse=True), 'DESC-сортировка "Сначала дорогие" не работает'
