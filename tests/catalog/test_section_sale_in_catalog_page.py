import pytest


from pages.catalog_page_section_sale import SectionSaleInCatalogPage

@pytest.mark.smoke
def test_open_section_sale_in_catalog_page(driver):
    """
    Проверка раздела каталога 'Распрадажа'
    """

    page = SectionSaleInCatalogPage(driver)


    page.open_catalog_menu()    # Метод открытия страницы + Клик на кнопку "Каталог"
    page.go_to_sale_category()    # Метод клика по разделу меню каталога "Распрадажа"

    #    Проверки на странице раздела "Распродажа":
    assert page.get_title() == "Распродажа", "Заголовок каталога != Распродажа"    # Проверяю, что заголовок не пустой
    assert page.get_product_count() > 0, "В блоке с количеством товаров пусто"
    assert page.is_breadcrumbs_visible(), "Хлебных крошек нет на странице"    # Проверка на то, есть ли на странице элемент "Хлебные крошки"
    assert page.is_sort_1_visible(), "Сортировки по популярности/цене/алфавиту нет на странице"  # Проверка на то, есть ли на странице элемент "Сортировка"
    assert page.is_sort_2_visible(), "Сортировки отображения карточек нет на странице"  # Проверка на то, есть ли на странице элемент "Сортировка"
    assert page.is_filtres_visible(), "Меню фильтров нет на странице"  # Проверка на то, есть ли на странице элемент "Фильтры"


#    Добавить тесты на работу сортировки и фильтров
# @pytest.mark.smoke
# def test_filters_and_sort(driver):

@pytest.mark.smoke
def test_kartochka_tovara(driver):
    """
    Проверка карточки товара
    """
    page = SectionSaleInCatalogPage(driver)

    page.click_first_product()    # Метод клика по названию карточки (переход в карточку товара)

    #    Проверки на странице карточки товара:
    assert page.get_title_card() == 'Арт. 377 Теплый пол Секция 4,3х1,7 б/у', "Название карточки != Арт. 377 Теплый пол Секция 4,3х1,7 б/у"