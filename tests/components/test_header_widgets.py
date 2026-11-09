import pytest
import allure
import time


from config.settings import settings
from pages.components.header import HeaderComponents
from pages.catalog.listing_page import ListingPage


### В ЭТИ ТЕСТЫ НАДО ЕЩЁ БУДЕТ ПРОВЕРОК НАКИНУТЬ ЧУТЬ ПОЗЖЕ:
### Корзина: 1) можно проверить, кнопка меняется на "- 1 +"; 2) в дропдауне есть стоимоть товара
### ТАКЖЕ У ВСЕХ МОЖНО ПРОВЕРИТЬ, ЧТО ПОЯВЛЯЕТСЯ УВЕДОМЛЕНИЕ ОБ УСПЕШНОСТИ ДОБАВЛЕНИЯ ТОВАРА В СРАВНЕНИЕ/ИЗБРАННОЕ/КОРЗИНУ - реализовал


@allure.feature('Виджеты: "В сравнение/избранное/корзину"')
@allure.story('Проверить, что виджет "В сравнение" работает корректно: При добавлении товара в сравнение появляется иконка "1"; При наведении курсора на иконку открывается выпадающий список с добавленными в сравнение товарами; По клику на название товара редиректит на страницу карточки этого товара; По клику "В сравнение" редиректит на страницу раздела "Главная–Каталог–Сравнение товаров"; По клику "удалить" товар удаляется из списка добавленных')
@pytest.mark.smoke
def test_compare_widget(browser):
    """
    Проверить, что:
        виджет "В сравнение" работает корректно:
            1) При добавлении товара в сравнение появляется иконка "1";
            2) При наведении курсора на иконку открывается выпадающий список с добавленными в сравнение товарами;
            3) В выпадающем списке есть добавленный товар;
            4) По клику на название товара редиректит на страницу карточки этого товара;
            5) По клику "В сравнение" редиректит на страницу раздела "Главная–Каталог–Сравнение товаров"
            6) По клику "удалить" товар удаляется из списка добавленных;
    """

    #    Предварительные шаги до начала тестирования:
    listing = ListingPage(browser)
    header = HeaderComponents(browser)

    #    Предварительные шаги до начала тестирования: Добавить 1 товар в сравнение
    (
        listing.open_page_category_with_sorting_filters()    # Перейти на страницу каталога
        .product_card.click_button_add_cart_in_compare()    # Кликнуть кнопку "В сравнение" у любого товара (по умолчанию кликает по первому попавшемуся)
    )
    #    Проверка 1: Появился ли счетчик
    assert listing.product_card.check_notification_after_added_in_compare(), 'Уведомления об успешности добавления товара в сравнение не появилось'
    count = header.get_compare_counter_value()
    print(f'\nВ иконке с количеством добавленных товаров виджета "В сравнении": {count}')
    assert count != '', 'Иконка с количеством добавленных товаров в виджете сравнения отсутствует'

    #    Проверки 2,3: Появился ли дропдаун + Есть ли в нём карточка товара
    header.compare_widget.hover_icon()    # Навожу курсор на иконку виджета "В сравнении"
    assert header.compare_widget.check_dropdown(), 'Выпадающий список с добавленными в сравнение товарами не появился'
    assert header.compare_widget.check_card_in_widget(), 'В выпадающем списке нет товаров'

    #    Проверка 4: Происходит ли переход в карточку товара по клику на его название
    url_before_click_title_card = browser.current_url
    print(f'\nURL до клика по названию товара: {url_before_click_title_card}')
    header.compare_widget.click_title_card_in_dropdown()    # Кликаю по название товара
    url_after_click_title_card = browser.current_url
    print(f'\nURL до клика по названию товара: {url_after_click_title_card}')
    assert url_before_click_title_card != url_after_click_title_card, 'URL после перехода в карточку товара не изменился'

    #    Проверка_5: Открывается ли страница раздела "Главная–Каталог–Сравнение товаров" по клику кнопки "В сравнение"
    url_before_click_button_in_compare = browser.current_url
    print(f'\nURL до клика кнопки "В сравнение": {url_before_click_button_in_compare}')
    (
        header.compare_widget.hover_icon()    # Повторно навожу курсор на виджет "В сравнении"
        .click_btn_in_widget()    # Кликаю кнопку "В сравнение"
    )
    url_after_click_button_in_compare = browser.current_url
    print(f'\nURL после клика кнопки "В сравнение": {url_after_click_button_in_compare}')
    assert url_before_click_button_in_compare != url_after_click_button_in_compare, 'URL после клика кнопки "В сравнение" не изменился'

    #    Проверка_6: Удаляется ли товар из виджета "В сравнении"
    (
        header.compare_widget.hover_icon()  # Повторно проваливаюсь в дропдаун виджета "В сравнении"
        .click_remove_button_in_dropdown()  # Кликаю кнопку "Удалить" у первого товара в выпадающем списке
    )
    assert header.compare_widget.is_empty(), 'Товар не удалился из виджета сравнения!'


@allure.feature('Виджеты: "В сравнение/избранное/корзину"')
@allure.story('Проверить, что виджет "В избранное" работает корректно: При добавлении товара в избранное появляется иконка "1"; При наведении курсора на иконку открывается выпадающий список с добавленными в избранное товарами; По клику на название товара редиректит на страницу карточки этого товара; По клику "В избранное" редиректит на страницу раздела "Главная–Личный кабинет–Избранные товары"; По клику "удалить" товар удаляется из списка добавленных')
@pytest.mark.smoke
def test_favorite_widget(browser):
    """
    Проверить, что:
        виджет "В сравнение" работает корректно:
            1) При добавлении товара в избранное появляется иконка "1";
            2) При наведении курсора на иконку открывается выпадающий список с добавленными в избранное товарами;
            3) В выпадающем списке есть добавленный товар;
            4) По клику на название товара редиректит на страницу карточки этого товара;
            5) По клику "В избранное" редиректит на страницу раздела "Главная–Личный кабинет–Избранные товары"
            6) По клику "удалить" товар удаляется из списка добавленных;
    """

    #    Предварительные шаги до начала тестирования:
    listing = ListingPage(browser)
    header = HeaderComponents(browser)

    #    Предварительные шаги до начала тестирования: Добавить 1 товар в сравнение
    (
        listing.open_page_category_with_sorting_filters()    # Перейти на страницу каталога
        .product_card.click_button_add_cart_in_favorite()    # Кликнуть кнопку "В избранное" у любого товара (по умолчанию кликает по первому попавшемуся)
    )
    #    Проверка 1: Появился ли счетчик
    assert listing.product_card.check_notification_after_added_in_favorite(), 'Уведомления об успешности добавления товара в избранное не появилось'
    count = header.get_favorite_counter_value()
    print(f'\nВ иконке с количеством добавленных товаров виджета "В избранное": {count}')
    assert count != '', 'Иконка с количеством добавленных товаров в виджете сравнения отсутствует'

    #    Проверки 2,3: Появился ли дропдаун + Есть ли в нём карточка товара
    header.favorite_widget.hover_icon()    # Навожу курсор на иконку виджета "В избранное"
    assert header.favorite_widget.check_dropdown(), 'Выпадающий список с добавленными в сравнение товарами не появился'
    assert header.favorite_widget.check_card_in_widget(), 'В выпадающем списке нет товаров'

    #    Проверка 4: Происходит ли переход в карточку товара по клику на его название
    url_before_click_title_card = browser.current_url
    print(f'\nURL до клика по названию товара: {url_before_click_title_card}')
    header.favorite_widget.click_title_card_in_dropdown()    # Кликаю по название товара
    url_after_click_title_card = browser.current_url
    print(f'\nURL до клика по названию товара: {url_after_click_title_card}')
    assert url_before_click_title_card != url_after_click_title_card, 'URL после перехода в карточку товара не изменился'

    #    Проверка_5: Открывается ли страница раздела "Главная–Личный кабинет–Избранные товары" по клику кнопки "В избранное"
    url_before_click_button_in_favorite = browser.current_url
    print(f'\nURL до клика кнопки "В избранное": {url_before_click_button_in_favorite}')
    (
        header.favorite_widget.hover_icon()    # Повторно навожу курсор на виджет "В избранное"
        .click_btn_in_widget()    # Кликаю кнопку "В избранное"
    )
    url_after_click_button_in_favorite = browser.current_url
    print(f'\nURL после клика кнопки "В избранное": {url_after_click_button_in_favorite}')
    assert url_before_click_button_in_favorite != url_after_click_button_in_favorite, 'URL после клика кнопки "В избранное" не изменился'

    #    Проверка_6: Удаляется ли товар из виджета "В избранное"
    (
        header.favorite_widget.hover_icon()  # Повторно проваливаюсь в дропдаун виджета "В избранное"
        .click_remove_button_in_dropdown()  # Кликаю кнопку "Удалить" у первого товара в выпадающем списке
    )
    assert header.favorite_widget.is_empty(), 'Товар не удалился из виджета избранное!'


@allure.feature('Виджеты: "В сравнение/избранное/корзину"')
@allure.story('Проверить, что виджет "В избранное" работает корректно: При добавлении товара в корзину появляется иконка "1"; При наведении курсора на иконку открывается выпадающий список с добавленными в корзину товарами; По клику на название товара редиректит на страницу карточки этого товара; По клику "В корзину" редиректит на страницу раздела "Корзина"; По клику "удалить" товар удаляется из списка добавленных')
@pytest.mark.smoke
def test_basket_widget(browser):
    """
    Проверить, что:
        виджет "В корзину" работает корректно:
            1) При добавлении товара в корзину появляется иконка "1";
            2) При наведении курсора на иконку открывается выпадающий список с добавленными в корзину товарами;
            3) В выпадающем списке есть стоимость товара;
            4) В выпадающем списке есть добавленный товар;
            5) По клику на название товара редиректит на страницу карточки этого товара;
            6) По клику "В корзину" редиректит на страницу раздела "Корзина" товары;
            7) По клику "удалить" товар удаляется из списка добавленных;
    """

    #    Предварительные шаги до начала тестирования:
    listing = ListingPage(browser)
    header = HeaderComponents(browser)

    #    Предварительные шаги до начала тестирования: Добавить 1 товар в корзину
    (
        listing.open_page_category_with_sorting_filters()    # Перейти на страницу каталога
        .product_card.click_button_add_cart_in_basket()    # Кликнуть кнопку "В корзину" у любого товара (по умолчанию кликает по первому попавшемуся)
    )
    #    Проверка 1: Появился ли счетчик
    assert listing.product_card.check_notification_after_added_in_basket(), 'Уведомления об успешности добавления товара в корзину не появилось'
    count = header.get_basket_counter_value()
    print(f'\nВ иконке с количеством добавленных товаров виджета "В корзину": {count}')
    assert count != '', 'Иконка с количеством добавленных товаров в виджете сравнения отсутствует'

    #    Проверки 2,3,4: Появился ли дропдаун + Есть ли в нём стоимость товара + Есть ли в нём карточка товара
    header.basket_widget.hover_icon()    # Навожу курсор на иконку виджета "В корзину"
    assert header.basket_widget.check_dropdown(), 'Выпадающий список с добавленными в корзину товарами не появился'
    assert header.basket_widget.check_card_in_widget(), 'В выпадающем списке нет товаров'
    final_price = header.basket_widget.get_sum_card()
    print(f'Стоимость товара в корзине: {final_price}')
    assert final_price != '', 'В дропдауне корзины нет стоимости товара'

    #    Проверка 4: Происходит ли переход в карточку товара по клику на его название
    url_before_click_title_card = browser.current_url
    print(f'\nURL до клика по названию товара: {url_before_click_title_card}')
    header.basket_widget.click_title_card_in_dropdown()    # Кликаю по название товара
    url_after_click_title_card = browser.current_url
    print(f'\nURL до клика по названию товара: {url_after_click_title_card}')
    assert url_before_click_title_card != url_after_click_title_card, 'URL после перехода в карточку товара не изменился'

    #    Проверка_5: Открывается ли страница раздела "Корзина" товары по клику кнопки "В корзину"
    url_before_click_button_in_basket = browser.current_url
    print(f'\nURL до клика кнопки "В корзину": {url_before_click_button_in_basket}')
    (
        header.basket_widget.hover_icon()    # Повторно навожу курсор на виджет "В корзину"
        .click_btn_in_widget()    # Кликаю кнопку "В корзину"
    )
    url_after_click_button_in_basket = browser.current_url
    print(f'\nURL после клика кнопки "В корзину": {url_after_click_button_in_basket}')
    assert url_before_click_button_in_basket != url_after_click_button_in_basket, 'URL после клика кнопки "В корзину" не изменился'

    #    Проверка_6: Удаляется ли товар из виджета "В корзину"
    listing.open_page_category_with_sorting_filters()    # Повторно возвращаюсь на страницу каталога, т.к. в корзине исчезают все виджеты из хедера
    (
        header.basket_widget.hover_icon()  # Повторно проваливаюсь в дропдаун виджета "В корзину"
        .click_remove_button_in_dropdown()  # Кликаю кнопку "Удалить" у первого товара в выпадающем списке
    )
    assert header.basket_widget.is_empty(), 'Товар не удалился из виджета корзина!'

