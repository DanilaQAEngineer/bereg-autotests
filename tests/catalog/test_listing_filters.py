import pytest
from time import sleep


from pages.catalog.listing_page import ListingPage
from pages.components.header import HeaderComponents
from locators.catalog.listing_locators import LocatorsForListing


@pytest.mark.smoke
def test_filter_by_price_range(browser):
    """
        Проверить, что:
            фильтрация по диапазону цен "от 1000 до 5000" работает корректно
    """

    page = ListingPage(browser)
    page.open_page_category_with_sorting_filters()

    #    Запоминаем количество товаров ДО выставления требований по стоимости
    count_before = page.get_product_count(); print(f'\nТоваров на странице ДО выставления диапазона: {count_before}')

    (
        page.filter_panel.enter_minimal_price('1000')
        .enter_maximal_price('5000')
    )

    sleep(5)  # ВРЕМЕННАЯ ЗАГЛУШКА: убрать, как найду решение, как реализовать небольшое ожидание после выставления фильтров, чтобы подтянулись карточки, соответствующие диапазону цен

    #    Собираем кол-во товаров и цены ПОСЛЕ фильтрации (используем тот же метод из SortPanel, т.к. он собирает новые цены, а в фильтре отображаются именно они)
    count_after = page.get_product_count(); print(f'\nТоваров на странице ПОСЛЕ выставления диапазона: {count_after}')
    final_prices = page.sort_panel.get_all_prices_as_floats(); print(f'\nСписок цен на странице ПОСЛЕ выставления диапазона: {final_prices}')

    assert len(final_prices) > 0, 'После фильтрации не осталось товаров'
    for price in final_prices:
        assert 1000 <= price <= 5000, f"Товар с ценой {price} не должен быть в диапазоне 1000-5000"

    print(f"\nДо фильтра: {count_before} товаров. После фильтра: {len(final_prices)} товаров.")
