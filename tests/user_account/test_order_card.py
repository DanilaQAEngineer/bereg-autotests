import pytest
import allure


from pages.catalog.listing_page import ListingPage
from pages.user_account.account_page import AccountPage
from pages.components.modals import ModalsComponent


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_repeat_order(authorized_user):
    """ Проверить, что по клику кнопки "Повторить заказ" в карточке товара открывается корзина """
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию

    #    Переходим в ЛК (таб "Заказы")
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_orders()  # Кликаем по табу "Заказы"
        .click_card_order()  # Кликаю первую карточку заказа
    )

    url_before_click_repeat_order_btn = authorized_user.current_url#; print(f"\nURL до применения фильтров: {url_before_click_repeat_order_btn}")

    (
        account.click_repeat_order_in_order_card()  # Кликаю кнопку "Повторить заказ"
    )

    url_after_click_repeat_order_btn = authorized_user.current_url  # ; print(f"\nURL до применения фильтров: {url_after_click_repeat_order_btn}")

    #assert url_before_click_repeat_order_btn != url_after_click_repeat_order_btn, 'URL не изменился после клика кнопки "Повторить заказ": корзина не открылась'
    assert "/basket/" in authorized_user.current_url, 'Переход в корзину по кнопке "Повторить заказ" не произошел'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_ask_question_in_order_card(authorized_user):
    """ Проверить, что по клику кнопки "Задать вопрос" открывается модалка "Задать вопрос по заказу" """
    account = AccountPage(authorized_user)  # Прокидываю фикстуру, в которой уже прописали корректную авторизацию
    modals = ModalsComponent(authorized_user)

    #    Переходим в ЛК (таб "Заказы")
    (
        account.open_account_page()  # Открываем ЛК
        .click_tab_orders()  # Кликаем по табу "Заказы"
        .click_card_order()  # Кликаю первую карточку заказа
        .click_ask_question_in_order_card()  # Кликаю на кнопку "Задать вопрос"
    )

    title_modal = modals.check_title_in_ask_question_modal_in_order_card()#; print(f'Заголовок в модалке:{title_modal}')

    assert modals.is_ask_question_modal_in_order_card_visible(), 'Модалка "Задать вопрос по заказу" не открылась'
    assert title_modal != '', 'Заголовок в модалке "Задать вопрос по заказу" пустой'
