import pytest
from time import sleep


from pages.cart.cart_page import Basket
from pages.catalog.listing_page import ListingPage

#    СЮДА ЕЩЁ НУЖНО БУДЕТ ДОБАВИТЬ ТЕСТОВ ДЛЯ УДАЛЕНИЯ/ВОССТАНОВЛЕНИЯ КАРТОЧКИ ИЗ/В КОРЗИНЕ + ПОЛНОЕ ОЧИЩЕНИЕ КОРЗИНЫ
@pytest.mark.smoke
def test_add_check_card_in_basket(browser):
    """
        Проверить, что:
            товар, добавленный со страницы каталога действительно появляется в корзине
    """

    listing = ListingPage(browser)
    cart = Basket(browser)

    #    Предварительный шаг до начала тестирования: добавляю товар в корзину из каталога
    (
        listing.open_page_category_with_sorting_filters()
        .product_card.click_button_add_cart_in_basket()
    )

    #    1. Перехожу в корзину
    cart.open_basket_page()
    #title_card = cart.get_title_first_card()

    assert cart.get_cart_in_basket(), 'Корзина пустая'
    assert cart.get_title_first_card() != '', 'Названия карточки отсутствует';#print(f'\nНазвание карточки первого товара: {title_card}')


@pytest.mark.smoke
def test_add_card_in_basket(browser):
    """
        Проверить, что:
            по клику кнопки "+" добавляется ещё один товар
    """

    listing = ListingPage(browser); cart = Basket(browser)

    (
        listing.open_page_category_with_sorting_filters()
        .product_card.click_button_add_cart_in_basket()
    )

    cart.open_basket_page()    # Переход в корзину
    count_tovarov_before_click_button_pluse = cart.get_count_cart_in_card(); print(f'\nКоличество товаров ДО клика кнопки "+": {count_tovarov_before_click_button_pluse}')
    price_before_click_button_plus = cart.get_price_cart_in_card(); print(f'Цена в карточке товара ДО клика кнопки "+": {price_before_click_button_plus}')
    final_price_before_click_button_plus = cart.get_price_cart_in_card(); print(f'Цена в блоке "Итого" товара ДО клика кнопки "+": {final_price_before_click_button_plus}')

    cart.click_button_plus()    # Клик по кнопке "+"

    sleep(1)

    count_tovarov_after_click_button_pluse = cart.get_count_cart_in_card(); print(f'\nКоличество товаров ДО клика кнопки "+": {count_tovarov_after_click_button_pluse}')
    price_after_click_button_plus = cart.get_price_cart_in_card(); print(f'Цена в карточке товара ПОСЛЕ клика кнопки "+": {price_after_click_button_plus}')
    final_price_after_click_button_plus = cart.get_price_cart_in_card(); print(f'Цена в блоке "Итого" товара ПОСЛЕ клика кнопки "+": {final_price_after_click_button_plus}')


    assert count_tovarov_before_click_button_pluse != count_tovarov_after_click_button_pluse, 'Количество товаров не изменилось'
    assert price_before_click_button_plus != price_after_click_button_plus, 'Цена в карточке товара не изменилась'
    assert final_price_before_click_button_plus != final_price_after_click_button_plus, 'Цена в блоке "Итого" не изменилась'


@pytest.mark.smoke
def test_delete_card_in_basket(browser):
    """
        Проверить, что:
            1) по клику кнопки "урна" (удалить) карточка удаляется из корзины
            2) под полем "Промокод" появляется текстовка: ""
    """

    listing = ListingPage(browser)
    cart = Basket(browser)

    (
        listing.open_page_category_with_sorting_filters()
        .product_card.click_button_add_cart_in_basket()
    )

    (
        cart.open_basket_page()  # Переход в корзину
        .click_button_delete()  # Клик по кнопке "урна" (удалить)
    )

    message = cart.get_text_message_pod_promokod(); print(f'\nТекст сообщения: {message}')

    assert cart.check_message_pod_promokod(), 'Сообщения под полем "Промокод" нет: корзина не пустая'
    assert cart.get_text_message_pod_promokod() != '', 'Сообщение пустое'
