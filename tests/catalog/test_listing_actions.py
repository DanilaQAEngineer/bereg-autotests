import pytest
from pages.catalog.listing_page import ListingPage
from pages.components.header import HeaderComponents


#                           ДОБАВИТЬ АНАЛОГИЧНЫЕ ТЕСТЫ ДЛЯ ДОБАВЛЕНИЯ ТОВАРА В ИЗБРАННОЕ И СРАВНЕНИЕ
@pytest.mark.smoke
def test_add_first_product_to_cart(browser):
    """
        Проверить, что:
            1) после успешного добавления товара в корзину на странице появляется уведомление
            2) количество товаров в корзине меняется
    """

    page = ListingPage(browser)
    header = HeaderComponents(browser)

    page.open_page_category_with_sort_and_cart()

    #    1. Проверяю, что на странице раздела есть карточки товаров:
    assert page.get_product_count() > 0, 'На странице раздела нет карточек товаров'

    page.product_card.click_button_add_cart_in_basket()

    #    2. Проверяю, что после добавления товара в корзину на странице появилось уведомление об успешности добавления:
    assert page.product_card.check_notification_after_added_in_basket() > 0, 'Уведомление об успешности добавления товара в корзину не появилось на странице'

    #    3. Проверяю счетчик
    counter_value = header.get_cart_counter_value(); print(f'\nТоваров в корзине:  {counter_value}')
    assert counter_value != "", 'Счетчик корзины не появился в иконке "Корзина" или он пуст'
    assert int(counter_value) > 0, f'Счетчик корзины не увеличился, сейчас: {counter_value}'