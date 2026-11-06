import pytest


from pages.catalog.listing_page import ListingPage
from pages.product.product_page import ProductPage


@pytest.mark.smoke
def test_product_page_ui(browser):
    """
        Проверить, что:
            базовый UI карточки товара отображается корректно:
                есть ХК, есть заголовок
    """

    listing = ListingPage(browser)
    product = ProductPage(browser)

    (
        listing.open_page_category_with_sorting_filters()    # Предусловие: перейти в каталог с товарами
        .product_card.open_first_card()    # Со страницы каталога проваливаюсь в карточку первого товара
    )

    assert product.check_breadcrumbs(), 'Хлебные крошки отсутствуют'
    title_card = product.get_title_card()
    assert title_card != '', 'Название товара отсутствует'; print(f'\nНазвание карточки товара: {title_card}')


@pytest.mark.smoke
def test_product_tabs_switch(browser):
    """
        Проверить, что:
            табы в карточке товара корректно переключаются
    """

    listing = ListingPage(browser)
    product = ProductPage(browser)

    (
        listing.open_page_category_with_sorting_filters()    # Предусловие: перейти в каталог с товарами
        .product_card.open_first_card()    # Со страницы каталога проваливаюсь в карточку первого товара
    )

    assert product.check_text_in_tab_description(), 'В табе "Описание" отсутствует содержание'

    product.click_tab_otz()
    #assert product.check_text_in_tab_dost(), 'В табе "Отзывы" отсутствует содержание'    # пока закомментил проверку, т.к. содержания в табе нет (только текстовка, что пусто)

    product.click_tab_opl()
    assert product.check_text_in_tab_opl(), 'В табе "Оплата" отсутствует содержание'

    product.click_tab_dost()
    assert product.check_text_in_tab_dost(), 'В табе "Доставка" отсутствует содержание'

    product.click_tab_vopr()
    assert product.check_text_in_tab_vopr(), 'В табе "Вопросы о товаре" отсутствует содержание'


@pytest.mark.smoke
def test_add_card_in_basket(browser):
    """
        Проверить, что:
            по клику кнопки "Добавить в корзину" товар добавляется в корзину
    """

    listing = ListingPage(browser)
    product = ProductPage(browser)

    (
        listing.open_page_category_with_sorting_filters()    # Предусловие: перейти в каталог с товарами
        .product_card.open_first_card()    # Со страницы каталога проваливаюсь в карточку первого товара
    )

    product.click_button_in_basket()    # Добавление товара в корзину

    assert product.check_notification_after_added_card_in_basket(), 'Уведомления о добавлении товара в корзину отсутствует'

    title_notification = product.check_title_in_notification()
    #print(f'\nУведомление заголовка: {title_notification}')
    assert title_notification != '', 'Заголовок в уведомлении отсутствует'

    text_notification = product.check_name_card_in_notification()
    #print(f'Содержание уведомления заголовка: {text_notification}')
    assert text_notification == product.get_title_card(), 'Название в уведомлении не совпадает с заголовком карточки'
