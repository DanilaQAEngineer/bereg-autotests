import pytest


from pages.catalog_pages.catalog_page_section_accessories import SectionAccessoriesInCatalogPage



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
