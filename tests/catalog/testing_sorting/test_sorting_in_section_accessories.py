import pytest


from pages.catalog_pages.catalog_page_section_accessories import SectionAccessoriesInCatalogPage


#                                               ТЕСТЫ ДЛЯ СОРТИРОВКИ В РАЗДЕЛЕ "АКСЕССУАРЫ":
@pytest.mark.smoke    # ACS-сортировка по стоимости (от самых дешёвых к самым дорогим)
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
    assert accessories_page.get_sort_value() == 'Сначала дешевые', "Значение кнопки_дропдауна != 'Сначала дешевые'"
    assert len(final_prices) > 1, "На странице недостаточно товаров для проверки сортировки"  #
    assert final_prices == sorted(final_prices, reverse=False), f"Сортировка по возрастанию не работает! Цены на странице: {final_prices}"


@pytest.mark.smoke    # DESC-сортировка по стоимости (от самых дорогих к самым дешёвым)
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
    assert accessories_page.get_sort_value() == 'Сначала дорогие', "Значение кнопки_дропдауна != 'Сначала дорогие'"
    assert len(final_prices) > 1, "На странице недостаточно товаров для проверки сортировки"    #
    assert final_prices == sorted(final_prices, reverse=True), f"Сортировка по убыванию не работает! Цены на странице: {final_prices}"


def test_view_by_line(browser):
    """
    ОТОБРАЖЕНИЕ ТОВАРОВ НА СТРАНИЦЕ РАЗДЕЛА: Кликаю на тогл "Строчный вывод"
    """
    accessories_page = SectionAccessoriesInCatalogPage(browser)

    (
        accessories_page.open_catalog_menu()    # Метод открытия страницы + Клик на кнопку "Каталог"
        .go_to_sale_category()
    )
    # 🡳 Создал переменную "УРЛа ДО применения сортировки" + Вызываю метод получения текущей УРЛы: записываю URL, которая была ДО применения сортировки
    url_before_can_sort = accessories_page.current_url()
    # print(f'\nСсылка ДО изменения раскладки товаров на странице: {url_before_can_sort}')

    (
        accessories_page.click_on_view_by_line()    # Метод получения страницы с новой сортировкой по убыванию
    )
    # 🡳 Создал переменную "УРЛа ПОСЛЕ применения сортировки" + Вызываю метод получения текущей УРЛы: записываю URL, которая была ПОСЛЕ применения сортировки
    url_after_can_sort = accessories_page.current_url()
    # print(f'Ссылка ПОСЛЕ изменения раскладки товаров на странице: {url_after_can_sort}')

    #    2.1 Проверки работы сортировки:
    assert url_after_can_sort == 'https://pfbereg.ru/catalog/aksessuary1/?display=list', "URL некорректный"


def test_view_by_price(browser):
    """
    ОТОБРАЖЕНИЕ ТОВАРОВ НА СТРАНИЦЕ РАЗДЕЛА: Кликаю на тогл "Вывод прайсом"
    """
    accessories_page = SectionAccessoriesInCatalogPage(browser)

    (
        accessories_page.open_catalog_menu()    # Метод открытия страницы + Клик на кнопку "Каталог"
        .go_to_sale_category()
    )
    # 🡳 Создал переменную "УРЛа ДО применения сортировки" + Вызываю метод получения текущей УРЛы: записываю URL, которая была ДО применения сортировки
    url_before_can_sort = accessories_page.current_url()
    # print(f'\nСсылка ДО изменения раскладки товаров на странице: {url_before_can_sort}')

    (
        accessories_page.click_on_view_by_prcie()    # Метод получения страницы с новой сортировкой по убыванию
    )
    # 🡳 Создал переменную "УРЛа ПОСЛЕ применения сортировки" + Вызываю метод получения текущей УРЛы: записываю URL, которая была ПОСЛЕ применения сортировки
    url_after_can_sort = accessories_page.current_url()
    # print(f'Ссылка ПОСЛЕ изменения раскладки товаров на странице: {url_after_can_sort}')

    #    2.1 Проверки работы сортировки:
    assert url_after_can_sort == 'https://pfbereg.ru/catalog/aksessuary1/?display=price', "URL некорректный"
