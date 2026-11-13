import time

import pytest
import allure


from config.settings import settings
from pages.user_account.account_page import AccountPage


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_account_tabs_navigation(authorized_user):
    """
    Проверить, что:
        переход по табам личного кабинета работает корректно
    """
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию
    account.open_account_page()

    #    Проверяю, что при переходе в ЛК попадаем на таб "Личный кабинет"
    get_title_in_tab_my_cabinet = account.get_title()  # ; print(f'Заголовок в личном кабинете: {get_title_in_tab_my_cabinet}')
    assert get_title_in_tab_my_cabinet != '', 'Заголовок в разделе таба пустой'

    #    1. Переключение на таб "Личные данные":
    url_before_click_tab_personal_data = authorized_user.current_url#; print(f'URL до клика таба "Личные данные": {url_before_click_tab_personal_data}')
    account.click_tab_personal_data()
    url_after_click_tab_personal_data = authorized_user.current_url#; print(f'URL после клика таба "Личные данные": {url_after_click_tab_personal_data}')
    get_title_in_tab_personal_data = account.get_title()#; print(f'Заголовок в личном кабинете: {get_title_in_tab_personal_data}')
    assert url_before_click_tab_personal_data != url_after_click_tab_personal_data, 'URL не изменился при переходе в таб "Личные данные"'
    assert get_title_in_tab_personal_data != '', 'Заголовок в разделе таба пустой'

    #    2. Переключение на таб "Личный счёт":
    url_before_click_tab_personal_check = authorized_user.current_url#; print(f'URL до клика таба "Личный счёт": {url_before_click_tab_personal_check}')
    account.click_tab_personal_check()
    url_after_click_tab_personal_check = authorized_user.current_url#; print(f'URL после клика таба "Личный счёт": {url_after_click_tab_personal_check}')
    get_title_in_tab_personal_check = account.get_title()#; print(f'Заголовок в личном кабинете: {get_title_in_tab_personal_check}')
    assert url_before_click_tab_personal_check != url_after_click_tab_personal_check, 'URL не изменился при переходе в таб "Личный счёт"'
    assert get_title_in_tab_personal_check != '', 'Заголовок в разделе таба пустой'
    #    Постусловие:
    account.click_personal_cabinet_in_breadcrumbs()  # Кликнуть в ХК на "Личный кабинет", т.к. бокового меню с табами на странице этого раздела нет

    #    3. Переключение на таб "Заказы":
    url_before_click_tab_orders = authorized_user.current_url#; print(f'URL до клика таба "Заказы": {url_before_click_tab_orders}')
    account.click_tab_orders()
    url_after_click_tab_orders = authorized_user.current_url#; print(f'URL после клика таба "Заказы": {url_after_click_tab_orders}')
    get_title_in_tab_orders = account.get_title()#; print(f'Заголовок в личном кабинете: {get_title_in_tab_orders}')
    assert url_before_click_tab_orders != url_after_click_tab_orders, 'URL не изменился при переходе в таб "Заказы"'
    assert get_title_in_tab_orders != '', 'Заголовок в разделе таба пустой'

    #    4. Переключение на таб "Профили заказов":
    url_before_click_tab_profile_orders = authorized_user.current_url#; print(f'URL до клика таба "Профили заказов": {url_before_click_tab_profile_orders}')
    account.click_tab_profile_orders()
    url_after_click_tab_profile_orders = authorized_user.current_url#; print(f'URL после клика таба "Профили заказов": {url_after_click_tab_profile_orders}')
    get_title_in_tab_profile_orders = account.get_title()#; print(f'Заголовок в личном кабинете: {get_title_in_tab_profile_orders}')
    assert url_before_click_tab_profile_orders != url_after_click_tab_profile_orders, 'URL не изменился при переходе в таб "Профили заказов"'
    assert get_title_in_tab_profile_orders != '', 'Заголовок в разделе таба пустой'

    #    5. Переключение на таб "Подписки":
    url_before_click_tab_subscribes = authorized_user.current_url#; print(f'URL до клика таба "Подписки": {url_before_click_tab_subscribes}')
    account.click_tab_subscribes()
    url_after_click_tab_subscribes = authorized_user.current_url#; print(f'URL после клика таба "Подписки": {url_after_click_tab_subscribes}')
    get_title_in_tab_subscribes = account.get_title()#; print(f'Заголовок в личном кабинете: {get_title_in_tab_subscribes}')
    assert url_before_click_tab_subscribes != url_after_click_tab_subscribes, 'URL не изменился при переходе в таб "Подписки"'
    assert get_title_in_tab_subscribes != '', 'Заголовок в разделе таба пустой'

    #    6. Переключение на таб "Избранные товары":
    url_before_click_tab_favorite_cards = authorized_user.current_url# ; print(f'URL до клика таба "Избранные товары": {url_before_click_tab_favorite_cards}')
    account.click_tab_favorite_cards()
    url_after_click_tab_favorite_cards = authorized_user.current_url# ; print(f'URL после клика таба "Избранные товары": {url_after_click_tab_favorite_cards}')
    get_title_in_tab_favorite_cards = account.get_title()# ; print(f'Заголовок в личном кабинете: {get_title_in_tab_favorite_cards}')
    assert url_before_click_tab_favorite_cards != url_after_click_tab_favorite_cards, 'URL не изменился при переходе в таб "Избранные товары"'
    assert get_title_in_tab_favorite_cards != '', 'Заголовок в разделе таба пустой'

    #    7. Переключение на таб "Помощь":
    url_before_click_tab_help = authorized_user.current_url# ; print(f'URL до клика таба "Помощь": {url_before_click_tab_help}')
    account.click_tab_help()
    url_after_click_tab_help = authorized_user.current_url# ; print(f'URL после клика таба "Помощь": {url_after_click_tab_help}')
    get_title_in_tab_help = account.get_title()# ; print(f'Заголовок в личном кабинете: {get_title_in_tab_help}')
    assert url_before_click_tab_help != url_after_click_tab_help, 'URL не изменился при переходе в таб "Помощь"'
    assert get_title_in_tab_help != '', 'Заголовок в разделе таба пустой'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_account_logout(authorized_user):
    """
    Проверить, что: по клику "Выйти" происходит разлогин
    """
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию
    account.open_account_page()

    url_before_click_btn_exit = authorized_user.current_url#; print(f'URL до клика таба "Избранные товары": {url_before_click_btn_exit}')
    account.click_btn_exit()
    url_after_click_btn_exit = authorized_user.current_url#; print(f'URL после клика таба "Избранные товары": {url_after_click_btn_exit}')
    assert url_before_click_btn_exit != url_after_click_btn_exit, 'URL не изменился после выхода из учётной записи'