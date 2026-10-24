import pytest


from pages.catalog_pages.catalog_page_section_accessories import SectionAccessoriesInCatalogPage


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


#                                               ТЕСТЫ КАРТОЧКИ ТОВАРА :
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
