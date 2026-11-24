import pytest
import allure


from pages.catalog.listing_page import ListingPage
from pages.user_account.account_page import AccountPage


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_orders_filters(authorized_user):
    """ Проверить, что фильтры в разделе "Заказы" работают корректно """
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию

    #    Переходим в ЛК (таб "Заказы")
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_orders()  # Кликаем по табу "Заказы"
    )

    url_before_make_filters = authorized_user.current_url#; print(f"\nURL до применения фильтров: {url_before_make_filters}")

    (
        account.click_dropdown_order_status()  # Кликаем по дропдауну "Статус заказа"
        .select_otmena_in_dropdown_status_order()  # Выбираем параметр "Отменен"
        .click_dropdown_payment_status()  # Кликаем по дропдауну "Статус оплаты"
        .select_dont_payment_in_dropdown_status_payment()  # Выбираем параметр "Не оплачен"
        .click_dropdown_period()  # Кликаем по дропдауну "Период"
        .select_2026_in_dropdown_period()  # Выбираем параметр "2026"
    )

    url_after_make_filters = authorized_user.current_url  # ; print(f"\nURL до применения фильтров: {url_after_make_filters}")
    statuses = account.get_all_order_statuses()  # Собираю все статусы заказов со страницы

    assert url_before_make_filters != url_after_make_filters, 'URL не изменился после применения фильтров'
    for status in statuses:  # Проверяю КАЖДЫЙ статус в списке
        assert status == 'Отменен', f'На странице раздела есть заказ со статусом != "Отменен": {status}'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_empty_orders_page(authorized_user):
    """ Проверить, что если нет заказов, соответствующиих параметрам фильтрации, то отображается пустая страница с текстовкой: "Нет заказов, удовлетворяющих условиям" """
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию

    #    Переходим в ЛК (таб "Избранные товары")
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_orders()  # Кликаем по табу "Заказы"
        .click_dropdown_order_status()  # Кликаем по дропдауну "Статус заказа"
        .select_vypolnen_in_dropdown_status_order()  # Выбираем параметр "Выполнен"
    )

    assert account.is_orders_empty(), 'Текстовки "Нет заказов, удовлетворяющих условиям" на странице раздела нет'