import pytest


from pages.catalog_page_section_accessories import SectionAccessoriesInCatalogPage


#                                               ТЕСТЫ РАЗДЕЛА "АКСЕССУАРЫ" :
@pytest.mark.smoke
def test_open_section_accessories_in_catalog_page(browser):
    """
    1) Проверка раздела каталога 'Аксессуары': Переход в раздел "Гл.страница > Каталог > Аксессуары"
    """

    accessories_page = SectionAccessoriesInCatalogPage(browser)

    accessories_page.open_catalog_menu()    # Метод открытия страницы + Клик на кнопку "Каталог"

    url_before_click_section_sale = accessories_page.current_url()    # Создал переменную "УРЛа до перехода в раздел "Распродажа"" + Вызываю метод получения текущей УРЛы: сохраняю URL, которая была до перехода в раздел "Распродажа"

    accessories_page.go_to_sale_category()    # Метод клика по разделу меню каталога "Распрадажа"

    #    Проверки на странице раздела "Распродажа":
    assert accessories_page.current_url() != url_before_click_section_sale, "URL один и тот же: перехода в раздел не произошло"    # Добавил проверку, что текущая URL != той, что была до перехода (что это не одна и та же страница)
    assert accessories_page.get_title() != "", "В разделе 'Распродажа' нет заголовка"    # Проверяю, что заголовок не пустой
    assert accessories_page.get_product_count() > 0, "В разделе 'Распродажа' нет количества товаров"
    assert accessories_page.is_breadcrumbs_visible(), "В разделе 'Распродажа' нет хлебных крошек"    # Проверка на то, есть ли на странице элемент "Хлебные крошки"
    assert accessories_page.is_sort_1_visible(), "Сортировки по популярности/цене/алфавиту нет на странице"  # Проверка на то, есть ли на странице элемент "Сортировка"
    assert accessories_page.is_sort_2_visible(), "Сортировки отображения карточек нет на странице"  # Проверка на то, есть ли на странице элемент "Сортировка"
    assert accessories_page.is_filtres_visible(), "Меню фильтров нет на странице"  # Проверка на то, есть ли на странице элемент "Фильтры"


#                                               ТЕСТЫ ДЛЯ СОРТИРОВКИ В РАЗДЕЛЕ "АКСЕССУАРЫ":
@pytest.mark.smoke
def test_asc_sort_by_price(browser):
    """
    СОРТИРОВКА: Проверка работы сортировки по стоимости 'Сначала дешевые' (она применяется по умолчанию при переходе в раздел, выбирать её не нужно): "Гл.страница > Каталог > 'Аксессуары'"
    """
    accessories_page = SectionAccessoriesInCatalogPage(browser)

    (
        accessories_page.open_catalog_menu()  # Метод открытия страницы + Клик на кнопку "Каталог"
        .go_to_sale_category()
        .get_all_prices_as_floats()  # Метод получения страницы с новой сортировкой по убыванию
    )

    final_prices = accessories_page.get_all_prices_as_floats(); print(final_prices)  # Собираем все цены со страницы

    #    2.1 Проверки работы сортировки:
    assert len(final_prices) > 1, "На странице недостаточно товаров для проверки сортировки"  #
    assert final_prices == sorted(final_prices, reverse=False), f"Сортировка по возрастанию не работает! Цены на странице: {final_prices}"


@pytest.mark.smoke
def test_desc_sort_by_price(browser):
    """
    СОРТИРОВКА: Проверка работы сортировки по стоимости 'Сначала дорогие': "Гл.страница > Каталог > 'Аксессуары' > Клик по дропдауну 'Сортировка' > Выбор 'Сначала дорогие'"
    """
    accessories_page = SectionAccessoriesInCatalogPage(browser)

    (
        accessories_page.open_catalog_menu()    # Метод открытия страницы + Клик на кнопку "Каталог"
        .go_to_sale_category()
        .click_on_sort_button()    # Клик по кнопке-дропдауну "Сортировка"
    )
    # 🡳 Создал переменную "УРЛа ДО применения сортировки" + Вызываю метод получения текущей УРЛы: записываю URL, которая была ДО применения сортировки
    url_before_can_sort = accessories_page.current_url()
    # print(f'До применения сортировки: {url_before_can_sort}')

    (
        accessories_page.click_desc_sort_by_price()    # Выбор сортировки "По убыванию" в выпадающем списке
        .get_all_prices_as_floats()    # Метод получения страницы с новой сортировкой по убыванию
    )
    # 🡳 Создал переменную "УРЛа ПОСЛЕ применения сортировки" + Вызываю метод получения текущей УРЛы: записываю URL, которая была ПОСЛЕ применения сортировки
    url_after_can_sort = accessories_page.current_url()
    # print(f'После применения сортировки: {url_after_can_sort}')

    final_prices = accessories_page.get_all_prices_as_floats(); print(final_prices)    # Собираем все цены со страницы

    #    2.1 Проверки работы сортировки:
    assert url_after_can_sort != url_before_can_sort, "URL один и тот же: сортировка не применилась"
    assert accessories_page.is_new_sort_value() == 'Сначала дорогие', "Новое значение в кнопке сортировки != Сначала дорогие"
    assert len(final_prices) > 1, "На странице недостаточно товаров для проверки сортировки"    #
    assert final_prices == sorted(final_prices, reverse=True), f"Сортировка по убыванию не работает! Цены на странице: {final_prices}"


#                                               ТЕСТЫ ДЛЯ ФИЛЬТРАЦИИ В РАЗДЕЛЕ "АКСЕССУАРЫ":
@pytest.mark.smoke
def test_click_first_product(browser):
    """
    3) Проверка карточки товара
    """
    accessories_page = SectionAccessoriesInCatalogPage(browser)

    (
        accessories_page.open_catalog_menu()  # Метод открытия страницы + Клик на кнопку "Каталог"
        .go_to_sale_category()
    )

    url_before_click_first_product = accessories_page.current_url()  # Создал переменную "УРЛа до перехода в карточку товара" + Вызываю метод получения текущей УРЛы: сохраняю URL, которая была ДО перехода в карточку товара

    accessories_page.click_first_product()    # Метод клика по названию карточки (переход в карточку товара)


    #    Проверки на странице карточки товара:
    assert accessories_page.current_url() != url_before_click_first_product, "URL один и тот же: перехода в карточку не произошло"
    assert accessories_page.get_title_card() != "", "Название карточки != Арт. 377 Теплый пол Секция 4,3х1,7 б/у"
