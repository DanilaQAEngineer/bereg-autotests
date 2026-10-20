import pytest


from pages.catalog_page_section_sale import SectionSaleInCatalogPage


@pytest.mark.smoke
def test_open_section_sale_in_catalog_page(browser):
    """
    1) Проверка раздела каталога 'Распрадажа'
    """

    page = SectionSaleInCatalogPage(browser)

    page.open_catalog_menu()    # Метод открытия страницы + Клик на кнопку "Каталог"

    url_before_click_section_sale = page.current_url()    # Создал переменную "УРЛа до перехода в раздел "Распродажа"" + Вызываю метод получения текущей УРЛы: сохраняю URL, которая была до перехода в раздел "Распродажа"

    page.go_to_sale_category()    # Метод клика по разделу меню каталога "Распрадажа"

    #    Проверки на странице раздела "Распродажа":
    assert page.current_url() != url_before_click_section_sale, "URL один и тот же: перехода в раздел не произошло"    # Добавил проверку, что текущая URL != той, что была до перехода (что это не одна и та же страница)
    assert page.get_title() != "", "В разделе 'Распродажа' нет заголовка"    # Проверяю, что заголовок не пустой
    assert page.get_product_count() > 0, "В разделе 'Распродажа' нет количества товаров"
    assert page.is_breadcrumbs_visible(), "В разделе 'Распродажа' нет хлебных крошек"    # Проверка на то, есть ли на странице элемент "Хлебные крошки"
    assert page.is_sort_1_visible(), "Сортировки по популярности/цене/алфавиту нет на странице"  # Проверка на то, есть ли на странице элемент "Сортировка"
    assert page.is_sort_2_visible(), "Сортировки отображения карточек нет на странице"  # Проверка на то, есть ли на странице элемент "Сортировка"
    assert page.is_filtres_visible(), "Меню фильтров нет на странице"  # Проверка на то, есть ли на странице элемент "Фильтры"


#    Добавить тесты на работу сортировки и фильтров
@pytest.mark.smoke
def test_sort_and_filters(browser):
    """
    2) Проверка работы сортировки и фильтров
    """
    page = SectionSaleInCatalogPage(browser)

    (
        page.open_catalog_menu()  # Метод открытия страницы + Клик на кнопку "Каталог"
        .go_to_sale_category()
        .click_on_sort_button()
        .click_sort_alphabet()
     )

    #    2.1 Проверки работы сортировки:
    assert page.is_new_sort() == 'С начала алфавита', "В кнопке сортировки != С начала алфавита"

    (
        page.search_and_input_min_price()
        .search_and_input_max_price()
    )

    #    2.2 Проверки работы фильтров:
    assert page.get_message_bez_resultatov() != "", "Сообщение != К сожалению, раздел пуст"

@pytest.mark.smoke
def test_click_first_product(browser):
    """
    3) Проверка карточки товара
    """
    page = SectionSaleInCatalogPage(browser)

    (
        page.open_catalog_menu()  # Метод открытия страницы + Клик на кнопку "Каталог"
        .go_to_sale_category()
    )

    url_before_click_first_product = page.current_url()  # Создал переменную "УРЛа до перехода в карточку товара" + Вызываю метод получения текущей УРЛы: сохраняю URL, которая была ДО перехода в карточку товара

    page.click_first_product()    # Метод клика по названию карточки (переход в карточку товара)


    #    Проверки на странице карточки товара:
    assert page.current_url() != url_before_click_first_product, "URL один и тот же: перехода в карточку не произошло"
    assert page.get_title_card() != "", "Название карточки != Арт. 377 Теплый пол Секция 4,3х1,7 б/у"
