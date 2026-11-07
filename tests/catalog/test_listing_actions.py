import pytest
import allure


from pages.catalog.listing_page import ListingPage
from pages.components.header import HeaderComponents


@allure.feature('Страница раздела каталога')
@allure.story('Проверить, что: 1) после добавления товара в сравнение на странице появляется уведомление об успешности добавления; 2) количество товаров в сравнении меняется (появляется иконка с количеством)')
@pytest.mark.smoke
def test_add_first_product_to_compare(browser):
    """
        Проверить, что:
            1) после добавления товара в сравнение на странице появляется уведомление об успешности добавления
            2) количество товаров в сравнении меняется (появляется иконка с количеством)
    """

    page = ListingPage(browser)
    header = HeaderComponents(browser)

    page.open_page_category_with_sorting_filters()

    #    1. Проверяю, что на странице раздела есть карточки товаров:
    assert page.get_product_count() > 0, 'На странице раздела нет карточек товаров'

    page.product_card.click_button_add_cart_in_compare()

    #    2. Проверяю, что после добавления товара в сравнение на странице появилось уведомление об успешности добавления:
    assert page.product_card.check_notification_after_added_in_compare() > 0, 'Уведомление об успешности добавления товара в сравнение не появилось на странице'

    #    3. Проверяю счетчик
    counter_value = header.get_compare_counter_value(); print(f'\nТоваров в сравнении:  {counter_value}')
    assert counter_value != "", 'Счетчик сравнения не появился в иконке "Сравнение" или он пуст'
    assert int(counter_value) > 0, f'Счетчик сравнения не увеличился, сейчас: {counter_value}'


@allure.feature('Страница раздела каталога')
@allure.story('Проверить, что: 1) после добавления товара в избранное на странице появляется уведомление об успешности добавления; 2) количество товаров в избранном меняется (появляется иконка с количеством)')
@pytest.mark.smoke
def test_add_first_product_to_favorite(browser):
    """
        Проверить, что:
            1) после добавления товара в избранное на странице появляется уведомление об успешности добавления
            2) количество товаров в избранном меняется (появляется иконка с количеством)
    """

    page = ListingPage(browser)
    header = HeaderComponents(browser)

    page.open_page_category_with_sorting_filters()

    #    1. Проверяю, что на странице раздела есть карточки товаров:
    assert page.get_product_count() > 0, 'На странице раздела нет карточек товаров'

    page.product_card.click_button_add_cart_in_favorite()

    #    2. Проверяю, что после добавления товара в избранное на странице появилось уведомление об успешности добавления:
    assert page.product_card.check_notification_after_added_in_favorite() > 0, 'Уведомление об успешности добавления товара в избранное не появилось на странице'

    #    3. Проверяю счетчик
    counter_value = header.get_favorite_counter_value(); print(f'\nТоваров в избранном:  {counter_value}')
    assert counter_value != "", 'Счетчик сравнения не появился в иконке "Избранное" или он пуст'
    assert int(counter_value) > 0, f'Счетчик избранного не увеличился, сейчас: {counter_value}'


@allure.feature('Страница раздела каталога')
@allure.story('Проверить, что: 1) после добавления товара в корзину на странице появляется уведомление об успешности добавления; 2) количество товаров в корзине меняется (появляется иконка с количеством)')
@pytest.mark.smoke
def test_add_first_product_to_basket(browser):
    """
        Проверить, что:
            1) после добавления товара в корзину на странице появляется уведомление об успешности добавления
            2) количество товаров в корзине меняется (появляется иконка с количеством)
    """

    page = ListingPage(browser)
    header = HeaderComponents(browser)

    page.open_page_category_with_sorting_filters()

    #    1. Проверяю, что на странице раздела есть карточки товаров:
    assert page.get_product_count() > 0, 'На странице раздела нет карточек товаров'

    page.product_card.click_button_add_cart_in_basket()

    #    2. Проверяю, что после добавления товара в корзину на странице появилось уведомление об успешности добавления:
    assert page.product_card.check_notification_after_added_in_basket() > 0, 'Уведомление об успешности добавления товара в корзину не появилось на странице'

    #    3. Проверяю счетчик
    counter_value = header.get_basket_counter_value(); print(f'\nТоваров в корзине:  {counter_value}')
    assert counter_value != "", 'Счетчик корзины не появился в иконке "Корзина" или он пуст'
    assert int(counter_value) > 0, f'Счетчик корзины не увеличился, сейчас: {counter_value}'
