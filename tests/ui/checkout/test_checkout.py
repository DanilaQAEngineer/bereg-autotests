import pytest
import allure


from pages.cart.cart_page import Basket
from pages.checkout.checkout_page import CheckoutPage
from pages.catalog.listing_page import ListingPage
from locators.cart.cart_locators import LocatorsForCart
from locators.checkout.checkout_locators import LocatorsForCheckout


### Кейсы:
### 1_Проверить, что на странице отображаются все элементы:
# Проверить, что на странице есть все элементы (заголовок, блоки)
#   Блок "Физ.лицо": Есть поля и кнопка
#   Блок "Юр.лицо": Есть поля и кнопка
#   Блок "Способ доставки": Есть кнопка "Изменить" > По клику "Изменить" появляются 2 радиокнопки: Доставка + Самовывоз
#   Блок_радиокнопка "Доставка": Есть поля и кнопка
#   Блок_радиокнопка "Самовывоз": Есть карта, поля и кнопка
#   Блок "Итого": Есть карта, поля и кнопка

### 2_Проверить возможность заполнения полей блоков "Физ.лицо, Юр.Лицо, Доставка, Самовывоз, Итого" (+то, что в полях/чекбоксах действительно появляются значения)

### 3_Проверить отображения ошибок под пустыми обязательными полями (+если вообще нижего не ввожу и кликаю "Оформить заказ" появляются уведомления, а не просто ошибки под полями)
###     можно так чекнуть: Раскрываю Покупатель > Физ.лицо + Способ доставки > Изменить > Доставка (очищаю предзаполненное поле Индекс) = Кликаю кнопко Итого > Оформить заказ
### + проверить ошибки при вводе невалидных данных в поля (телефон, почта)


@allure.feature('Корзина > Оформление заказа')
@allure.story('Общая проверка всего интерфейса страницы')
@pytest.mark.smoke
def test_check_main_interface(browser):
    """
        Проверить полноту раздела "Оформление заказа": есть блоки, табы, поля, кнопки
    """
    listing = ListingPage(browser)
    cart = Basket(browser)
    checkout = CheckoutPage(browser)

    (
        listing.open_page_category_with_sorting_filters()  # Предварительный шаг: Переходим на страницу с товарами
        .product_card.click_button_add_cart_in_basket()  # Предварительный шаг: Добавляем товар в корзину
    )
    (
        cart.open_basket_page()  # Предварительный шаг: Переходим в корзину
        .click_element(LocatorsForCart.BUTTON_OFORMLENIE)  # Предварительный шаг: Прожимаем кнопку "Перейти к оформлению"
    )

    #   1. Поверки страницы "Оформление заказа":
    assert "/order/" in browser.current_url, \
        'Переход на страницу "Оформление заказа" не произошел'
    assert "оформление" in checkout.check_text(LocatorsForCheckout.TITLE_ON_PAGE).lower(), \
        f'Ожидали заголовок про оформление, получили: "{checkout.check_text(LocatorsForCheckout.TITLE_ON_PAGE).lower()}"'
    assert checkout.is_visible_element(LocatorsForCheckout.BLOCK_POKUPATEL), \
        'Блока "Покупатель" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.BLOCK_DOSTAVKA), \
        'Блока "Способ доставки" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.BLOCK_ITOGO), \
        'Блока "Итого" на странице нет'

    #   2. Поверки таба "Физическое лицо":
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_FIO_1), \
        'Поля "ФИО" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_EMAIL_1), \
        'Поля "E-mail" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_PHONE_1), \
        'Поля "Телефон" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.BTN_PRODOL_1), \
        'Кнопки "Продолжить" на странице нет'

    (
        checkout.wait_visible_element(LocatorsForCheckout.TAB_LEGAL)  # Жду перед кликом, когда таб "Юридическое лицо" станет видимым на странице оформления
        .click_element(LocatorsForCheckout.TAB_LEGAL)  # Кликаю по табу "Юридическое лицо"
        .wait_visible_element(LocatorsForCheckout.BTN_PRODOL_2)  # Жду полной прогрузке таба (когда в нём появится кнопка "Продолжить")
    )
    #   3. Поверки таба "Юридическое лицо":
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_COMPANY_NAME), \
        'Поля "Название компании" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_ADRESS_COMPANY), \
        'Поля "Юридический адрес" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_INN), \
        'Поля "ИНН" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_KPP), \
        'Поля "КПП" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_CONTACT_NAME), \
        'Поля "Контактное лицо" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_EMAIL_2), \
        'Поля "E-mail" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_PHONE_2), \
        'Поля "Телефон" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_OPERATOR_EDO), \
        'Поля "Оператор ЭДО" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.BTN_PRODOL_2), \
        'Кнопки "Продолжить" на странице нет'

    (
        checkout.wait_visible_element(LocatorsForCheckout.BTN_IZMENIT_1)  # Жду перед кликом, когда кнопка "Изменить" в блоке "Способ доставки" станет видимой
        .click_element(LocatorsForCheckout.BTN_IZMENIT_1)  # Кликаю по кнопке "Изменить"
        .wait_visible_element(LocatorsForCheckout.BTN_PRODOL_3)  # Жду полной прогрузки блока (когда в нём появится кнопка "Продолжить")
    )
    #   4. Поверки блока "Способ доставки > Доставка компанией"":
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_ADRESS), \
        'Поля "Адрес доставки" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_INDEX), \
        'Поля "Индекс" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_COMMENT_1), \
        'Поля "Комментарий к заказу" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.BTN_PRODOL_3), \
        'Кнопки "Продолжить" на странице нет'

    (
        checkout.wait_visible_element(LocatorsForCheckout.RADIO_SAMOVYVOZ)  # Жду перед кликом, когда радиокнопка "Самовывоз" отрисуется на странице
        .click_element(LocatorsForCheckout.RADIO_SAMOVYVOZ)  # Кликаю по радиокнопке "Самовывоз"
        .wait_visible_element(LocatorsForCheckout.BTN_PRODOL_4)  # Жду полной прогрузки блока (когда в нём появится кнопка "Продолжить")
    )
    #   5. Поверки блока "Способ доставки > Самовывоз"":
    assert checkout.is_visible_element(LocatorsForCheckout.KARTA), \
        'Яндекс-карты на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_COMMENT_2), \
        'Поля "Комментарий к заказу" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.BTN_PRODOL_3), \
        'Кнопки "Продолжить" на странице нет'

    checkout.wait_visible_element(LocatorsForCheckout.BTN_OFORM_ZAKAZ)  # Жду, когда блок "Итого" отрисуется на странице (когда в нём появится кнопка "Оформить заказ")
    #   6. Поверки блока "Итого"":
    assert checkout.is_visible_element(LocatorsForCheckout.INPUT_ENTER_PROMOCODE), \
        'Поля "Введите промокод или сертификат" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.BTN_OFORM_ZAKAZ), \
        'Кнопки "Оформить заказ" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.CHECKBOX_1), \
        'Поля-чекбокса "Продолжая, вы соглашаетесь с политикой конфиденциальности" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.CHECKBOX_2), \
        'Поля-чекбокса "Продолжая, вы соглашаетесь с публичной офертой" на странице нет'
    assert checkout.is_visible_element(LocatorsForCheckout.CHECKBOX_3), \
        'Поля-чекбокса "Продолжая, вы соглашаетесь на маркетинговые рассылки" на странице нет'


@allure.feature('Корзина > Оформление заказа')
@allure.story('Проверка ошибок на табах "Покупатель: Физическое лицо + Способ доставки: Доставка транспортной компанией или Озон Доставкой + Ошибки блока "Итого""')
@pytest.mark.smoke
def test_check_error_messages(browser):
    """
        Проверка отображения ошибок на странице таба: "Покупатель: Физическое лицо + Способ доставки: Доставка транспортной компанией или Озон Доставкой"
    """
    listing = ListingPage(browser)
    cart = Basket(browser)
    checkout = CheckoutPage(browser)

    (
        listing.open_page_category_with_sorting_filters()  # Предварительный шаг: Переходим на страницу с товарами
        .product_card.click_button_add_cart_in_basket()  # Предварительный шаг: Добавляем товар в корзину
    )

    (
        cart.open_basket_page()  # Предварительный шаг: Переходим в корзину
        .click_element(LocatorsForCart.BUTTON_OFORMLENIE)  # Предварительный шаг: Прожимаем кнопку "Перейти к оформлению"
    )

    (
        checkout.wait_visible_element(LocatorsForCheckout.BTN_IZMENIT_1)  # Жду перед кликом, когда в блоке "Способ доставки" появится кнопка "Изменить"
        .click_element(LocatorsForCheckout.BTN_IZMENIT_1)  # Кликаю по кнопке "Изменить"
        .wait_visible_element(LocatorsForCheckout.BTN_PRODOL_3)  # Жду полной прогрузки блока (должна появиться кнопка "Продолжить")
        .clear_field(LocatorsForCheckout.INPUT_ENTER_INDEX)  # Очищаю поле "Индекс" (т.к. оно по умолчанию предзаполнено и под ним 100% должна отобразиться ошибка)
        .wait_visible_element(LocatorsForCheckout.BTN_OFORM_ZAKAZ) # Жду полной прогрузки страницы (в "Итого" должна появиться кнопка "Продолжить")
        .click_element(LocatorsForCheckout.BTN_OFORM_ZAKAZ)  # Кликаю по кнопке "Оформить заказ"
    )

    #    Ошибки в блоке "Покупатель": (алерт: один алерт с 3 ошибками на разных строках (в HTML так: ошибка_1 <br> ошибка_2 <br> ошибка_3))
    assert 'оле "ф.и.о." обязатель' in checkout.check_text(LocatorsForCheckout.ERROR_ALERT_1).lower(), \
        f'Ожидали ошибку про ...оле "ф.и.о." обязатель..., получили: "{checkout.check_text(LocatorsForCheckout.ERROR_ALERT_1).lower()}"'
    assert 'оле "e-mail" обязатель' in checkout.check_text(LocatorsForCheckout.ERROR_ALERT_1).lower(), \
        f'Ожидали ошибку про ...оле "e-mail" обязатель..., получили: "{checkout.check_text(LocatorsForCheckout.ERROR_ALERT_1).lower()}"'
    assert 'оле "телефон" обязатель' in checkout.check_text(LocatorsForCheckout.ERROR_ALERT_1).lower(), \
        f'Ожидали ошибку про ...оле "телефон" обязатель..., получили: "{checkout.check_text(LocatorsForCheckout.ERROR_ALERT_1).lower()}"'
    #    Ошибки в блоке "Покупатель": (ошибки под инпутами)
    assert 'оле "ф.и.о." обязатель' in checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_FIO_INPUT).lower(), \
        f'Ожидали ошибку про ...оле "ф.и.о." обязатель..., получили: "{checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_FIO_INPUT).lower()}"'
    assert 'оле "e-mail" обязатель' in checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_EMAIL_INPUT).lower(), \
        f'Ожидали ошибку про ...оле "e-mail" обязатель..., получили: "{checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_EMAIL_INPUT).lower()}"'
    assert 'оле "телефон" обязатель' in checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_PHONE_INPUT).lower(), \
        f'Ожидали ошибку про ...оле "телефон" обязатель..., получили: "{checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_PHONE_INPUT).lower()}"'

    #    Ошибки в блоке "Способ доставки": (ошибки под инпутами)
    assert 'оле "индекс" обязатель' in checkout.check_text(LocatorsForCheckout.ERROR_ALERT_2).lower(), \
        f'Ожидали ошибку про ...оле "индекс" обязатель..., получили: "{checkout.check_text(LocatorsForCheckout.ERROR_ALERT_2).lower()}"'
    assert 'оле "индекс" обязатель' in checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_INPUT_INDEX).lower(), \
        f'Ожидали ошибку про ...оле "индекс" обязатель..., получили: "{checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_INPUT_INDEX).lower()}"'

    #    Ошибки в блоке "Итого": (алерт)
    assert 'огласитесь с услов' in checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_CHECKBOX_1).lower(), \
        f'Ожидали ошибку про ...огласитесь с услов..., получили: "{checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_CHECKBOX_1).lower()}"'
    assert 'огласитесь с услов' in checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_CHECKBOX_2).lower(), \
        f'Ожидали ошибку про ...огласитесь с услов..., получили: "{checkout.check_text(LocatorsForCheckout.ERROR_MSG_UNDER_CHECKBOX_2).lower()}"'
