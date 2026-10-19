import pytest


from pages.catalog_page_section_sale import SectionSaleInCatalogPage

@pytest.mark.smoke
def test_open_section_sale_in_catalog_page(driver):
    """Проверка, что каталог открывается, """
    page = SectionSaleInCatalogPage(driver)

    page.open_catalog_menu()    # Метод открытия страницы + Клик на кнопку "Каталог"
    page.go_to_sale_category()    # Метод клика по разделу меню каталога "распрадажа"
    page.get_title()    # Метод получения заголовка на странице раздела "Распродажа"
    page.get_product_count()    # Метод Получения количества результатов товаров на странице

    #    Проверки:
    assert page.get_title() == "Распродажа", "Заголовок каталога != Распродажа"    # Проверяю, что заголовок не пустой
    assert page.get_product_count() > 0, "В блоке с количеством товаров пусто"
