import pytest
import allure
from time import sleep


from pages.cart.cart_page import Basket
from pages.checkout.checkout_page import CheckoutPage
from pages.catalog.listing_page import ListingPage
from locators.cart.cart_locators import LocatorsForCart
from locators.checkout.checkout_locators import LocatorsForCheckout


@allure.feature('Корзина > Оформление заказа')
@allure.story('Проверка базового функционала: ввод значений в поля, клик по чекбоксам')
@pytest.mark.smoke
def test_enter_data(browser):
    """
        Проверить полноту страницы "Оформление заказа" (есть табы, поля, кнопки)

    """
    listing = ListingPage(browser)
    cart = Basket(browser)
    checkout = CheckoutPage(browser)

    #    Предусловие_1: Добавляем товар в корзину
    (
        listing.open_page_category_with_sorting_filters()
        .product_card.click_button_add_cart_in_basket()
    )
    #    Предусловие_2: Переходим в корзину + Кликаем кнопку "Перейти к оформлению"
    (
        cart.open_basket_page()
        .click_element(LocatorsForCart.BUTTON_OFORMLENIE)
    )

    #   1. Поверки страницы "Оформление заказа":
    assert "/order/" in browser.current_url, 'Переход на страницу "Оформление заказа" не произошел'
    assert "оформление" in checkout.check_text(LocatorsForCheckout.TITLE_ON_PAGE).lower(), f'Ожидали заголовок про оформление, получили: "{checkout.check_text(LocatorsForCheckout.TITLE_ON_PAGE).lower()}"'
    assert checkout.is_visible_element(LocatorsForCheckout.BLOCK_POKUPATEL), 'Блока "Покупатель" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.BLOCK_DOSTAVKA), 'Блока "Способ доставки" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.BLOCK_ITOGO), 'Блока "Итого" на странице нет'

    #   2. Поверки таба "Физическое лицо":
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_FIO_1), 'Поля "ФИО" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_EMAIL_1), 'Поля "E-mail" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_PHONE_1), 'Поля "Телефон" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.BTN_PRODOL_1), 'Кнопки "Продолжить" на странице нет'

    #   3. Поверки таба "Юридическое лицо":
    (
        checkout.wait_visible_element(LocatorsForCheckout.TAB_LEGAL)  # Жду перед кликом, когда таб "Юридическое лицо" станет видимым на странице оформления
        .click_element(LocatorsForCheckout.TAB_LEGAL)
        .wait_visible_element(LocatorsForCheckout.BTN_PRODOL_2)  # Жду полной прогрузке таба (когда в нём появится кнопка "Продолжить")

    )
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_COMPANY_NAME), 'Поля "Название компании" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_ADRESS_COMPANY), 'Поля "Юридический адрес" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_INN), 'Поля "ИНН" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_KPP), 'Поля "КПП" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_CONTACT_NAME), 'Поля "Контактное лицо" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_EMAIL_2), 'Поля "E-mail" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_PHONE_2), 'Поля "Телефон" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_OPERATOR_EDO), 'Поля "Оператор ЭДО" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.BTN_PRODOL_2), 'Кнопки "Продолжить" на странице нет'

    #checkout.click_element(LocatorsForCheckout.TAB_LEGAL)
    # checkout.click_tab_and_wait(LocatorsForCheckout.TAB_PHYSICAL)
    # checkout.click_element(LocatorsForCheckout.TAB_PHYSICAL)
    # checkout.click_tab_and_wait(LocatorsForCheckout.TAB_LEGAL)
    #
    # #    Переключение радиокнопок блока "Способ доставки":
    # checkout.click_element(LocatorsForCheckout.BTN_IZMENIT_1)
    # checkout.click_element(LocatorsForCheckout.RADIO_DOSTAVKA)
    # checkout.click_radio_and_wait(LocatorsForCheckout.RADIO_DOSTAVKA)
    # checkout.click_element(LocatorsForCheckout.RADIO_SAMOVYVOZ)
    # checkout.click_radio_and_wait(LocatorsForCheckout.RADIO_SAMOVYVOZ)
