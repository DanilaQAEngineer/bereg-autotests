import pytest
import allure


from config.settings import settings
from pages.components.header import HeaderComponents
from pages.catalog.listing_page import ListingPage


@allure.feature('Виджеты: "В сравнение/избранное/корзину"')
@allure.story('Проверить, что виджет "В сравнение" работает корректно: При добавлении товара в сравнение появляется иконка "1"; При наведении курсора на иконку открывается выпадающий список с добавленными в сравнение товарами; По клику на название товара редиректит на страницу карточки этого товара; По клику "В сравнение" редиректит на страницу раздела "В сравнение"; По клику "удалить" товар удаляется из списка добавленных')
@pytest.mark.smoke
def test_compare_widget(browser):
    """
    Проверить, что:
        виджет "В сравнение" работает корректно:
            1) При добавлении товара в сравнение появляется иконка "1";
            2) При наведении курсора на иконку открывается выпадающий список с добавленными в сравнение товарами;
            3) В выпадающем списке есть добавленный товар;
            4) По клику на название товара редиректит на страницу карточки этого товара;
            5) По клику "В сравнение" редиректит на страницу раздела "В сравнение"
            6) По клику "удалить" товар удаляется из списка добавленных;
    """

    #    Предварительные шаги до начала тестирования:
    listing = ListingPage(browser)
    header = HeaderComponents(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()    # Перейти на страницу каталога
        .product_card.click_button_add_cart_in_compare()    # Кликнуть кнопку "В сравнение" у любого товара (по умолчанию кликает по первому попавшемуся)
    )

    count = header.compare_widget.check_count_in_widget(); print(f'\nВ иконке с количеством добавленных товаров виджета "В сравнении": {count}')
    assert count != '', 'Иконка с количеством добавленных товаров в виджете сравнения отсутствует'    # Проверка_1

    header.compare_widget.hover_icon()    # Навожу курсор на иконку виджета "В сравнении"

    assert header.compare_widget.check_dropdown(), 'Выпадающий список с добавленными в сравнение товарами не появился'    # Проверка_2
    assert header.compare_widget.check_card_in_widget(), 'В выпадающем списке нет товаров'    # Проверка_3

    url_before_click_title_card = browser.current_url; print(f'\nURL до клика по названию товара: {url_before_click_title_card}')
    header.compare_widget.click_title_card_in_dropdown()    # Кликаю по название товара
    url_after_click_title_card = browser.current_url; print(f'\nURL до клика по названию товара: {url_after_click_title_card}')
    assert url_before_click_title_card != url_after_click_title_card, 'URL после перехода в карточку товара не изменился'    # Проверка_4

    url_before_click_button_in_compare = browser.current_url; print(f'\nURL до клика кнопки "В сравнение": {url_before_click_button_in_compare}')
    (
        header.compare_widget.hover_icon()    # Повторно навожу курсор на виджет "В сравнении"
        .click_btn_in_widget()    # Кликаю кнопку "В сравнение"
    )
    url_after_click_button_in_compare = browser.current_url; print(f'\nURL после клика кнопки "В сравнение": {url_after_click_button_in_compare}')
    assert url_before_click_button_in_compare != url_after_click_button_in_compare, 'URL после клика кнопки "В сравнение" не изменился'    # Проверка_5

    (
        header.compare_widget.hover_icon()  # Повторно проваливаюсь в дропдаун виджета "В сравнении"
        .click_remove_button_in_dropdown()  # Кликаю кнопку "Удалить" у первого товара в выпадающем списке
    )
    assert header.compare_widget.is_compare_empty(), 'Товар не удалился из виджета сравнения!'    # Проверка_6: Вызываю метод ожидания исчезновения карточек товаров после удаления (проверка того, что виджет сравнения пуст)
