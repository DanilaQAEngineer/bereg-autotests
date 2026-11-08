import pytest
import allure
import time


from config.settings import settings
from pages.components.header import HeaderComponents
from pages.catalog.listing_page import ListingPage


@allure.feature('Виджеты: "В сравнение/избранное/корзину"')
@allure.story('Проверить, что виджет "В сравнение" работает корректно: При добавлении товара в сравнение появляется иконка "1"; При наведении курсора на иконку открывается выпадающий список с добавленными в сравнение товарами; По клику на название товара редиректит на страницу карточки этого товара; По клику "удалить" товар удаляется из списка добавленных; По клику "В сравнение" редиректит на страницу раздела "В сравнение"')
@pytest.mark.smoke
def test_compare_widget(browser):
    """
    Проверить, что:
        виджет "В сравнение" работает корректно:
            При добавлении товара в сравнение появляется иконка "1";
            При наведении курсора на иконку открывается выпадающий список с добавленными в сравнение товарами;
            По клику на название товара редиректит на страницу карточки этого товара;
            По клику "удалить" товар удаляется из списка добавленных;
            По клику "В сравнение" редиректит на страницу раздела "В сравнение"
    """

    #    Предварительные шаги до начала тестирования:
    listing = ListingPage(browser)
    header = HeaderComponents(browser)

    #    Предварительные шаги до начала тестирования: Перейти на страницу каталога + Кликнуть кнопку "В сравнение"
    (
        listing.open_page_category_with_sorting_filters()
        .product_card.click_button_add_cart_in_compare()
    )

    count = header.compare_widget.check_count_in_widget(); print(f'Товаров в виджете: {count}')
    assert count != '', 'Количества товаров в виджете отсутствует'

    header.compare_widget.hover_icon()    # Навожу курсор на иконку виджета "В сравнении"

    assert header.compare_widget.check_dropdown(), 'Выпадающий список не появился'
    assert header.compare_widget.check_card_in_widget(), 'В выпадающем списке нет товаров'
