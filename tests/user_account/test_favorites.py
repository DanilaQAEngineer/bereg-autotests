import pytest
import allure


from pages.catalog.listing_page import ListingPage
from pages.user_account.account_page import AccountPage


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_clear_favorites_in_account(authorized_user):
    """ Проверить, что после клика "Очистить" в табе "Избранные товары" нет карточек (есть текстовка: "Список избранных элементов пуст") """
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию
    listing = ListingPage(authorized_user)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # Переходим на страницу каталога
        .product_card.click_button_add_cart_in_favorite()  # Добавляем в избранное первую карточку
    )

    #    Переходим в ЛК (таб "Избранные товары")
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_favorite_cards()  # Кликаем по табу "Избранные товары"
    )
    account.click_btn_clear()  # Кликаем по кнопке 'Очистить'

    assert account.is_favorites_empty(), 'Текстовки "Список избранных элементов пуст" на странице раздела нет: карточки не удалились'