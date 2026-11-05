import pytest
from time import sleep


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
        listing.open_page_category_with_sorting_filters()  # Предусловие: перейти в каталог с товарами
        .product_card.open_first_card()    # Со страницы каталога проваливаюсь в карточку первого товара
    )

    assert product.check_breadcrumbs(), 'Хлебные крошки отсутствуют'
    title_card = product.get_title_card()
    assert title_card != '', 'Название товара отсутствует'; print(f'\nНазвание карточки товара: {title_card}')

# @pytest.mark.smoke
# def test_product_tabs_switch(browser):
#     """
#         Проверить, что:
#             табы в карточке товара действительно переключаются
#     """
#
#     listing = ListingPage(browser)
#     product = ProductPage(browser)
#
#     (
#         listing.open_page_category_with_sorting_filters()  # Предусловие: перейти в каталог с товарами
#         .product_card.open_first_card()  # Со страницы каталога проваливаюсь в карточку первого товара
#     )
#
#     ### ПРОДОЛЖИТЬ НА МЕТОДАХ ПЕРЕКЛЮЧЕНИЯ ТАБОВ В КАРТОЧКЕ: ДОПИСАТЬ ЭТИ МЕТОДЫ В ProductPage