from selenium.webdriver.common.by import By


class LocatorsForCart:
    """" Локаторы элементов корзины """

    # ==================================================================================================================
    # ПУСТАЯ КОРЗИНА
    # ==================================================================================================================
    TITLE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, 'div.bx-sbb-empty-cart-text')    # Заголовок на странице, когда она полностью путсая

    # ==================================================================================================================
    # Локаторы элементов карточки внутри корзины:
    # ==================================================================================================================
    CARD_IN_BASKET = (By.ID, 'basket-items-list-container')
    TITLE_ADDED_CARD = (By.CSS_SELECTOR, 'span[data-entity="basket-item-name"]')
    PRICE_IN_CARD = (By.CSS_SELECTOR, 'div.basket-item-price-current-value')
    COUNT_TOVAROV = (By.CSS_SELECTOR, 'input.basket-item-amount-filed')

    # ==================================================================================================================
    #    Управление количеством (внутри карточки)
    # ==================================================================================================================
    BUTTON_PLUS = (By.CSS_SELECTOR, 'span[data-entity="basket-item-quantity-plus"]')
    BUTTON_MINUS = (By.CSS_SELECTOR, 'span[data-entity="basket-item-quantity-minus"]')
    BUTTON_DELETE_CARD = (By.CSS_SELECTOR, '.basket-items-list-item-removes')
    BUTTON_REPEAT_DELETE_CARD = (By.CSS_SELECTOR, 'span[data-entity="basket-item-close-restore-button"]')

    # ==================================================================================================================
    #    Блок "Итого":
    # ==================================================================================================================
    PRICE_IN_ITOGO_BLOCK = (By.CSS_SELECTOR, 'div.basket-total-outer div.basket-coupon-block-total-price-current')
    INPUT_PROMOCODE = (By.CSS_SELECTOR, 'div.basket-total-outer input.form-control')
    BTN_PROMOCODE = (By.CSS_SELECTOR, 'div.basket-total-outer i.svg-inline-coupon')  # Кнопка -> справа в поле ввода промокода
    MSG_AFTER_ENTER_PROMOCODE = (By.CSS_SELECTOR, 'div.basket-total-outer span.basket-coupon-info__text')  # Сообщение "Не найден" после ввода промика
    BUTTON_OFORMLENIE = (By.CSS_SELECTOR, 'div.basket-total-outer button.basket-btn-checkout')
    BUTTON_BUY_IN_ONE_CLICK = (By.CSS_SELECTOR, 'button[data-entity="basket-checkout-button"]')
    BUTTON_CLEAN_BASKET = (By.CSS_SELECTOR, 'div.delete_all')
    MINIMAL_SUM_ZAKAZA = (By.CSS_SELECTOR, 'div.icon_error_wrapper')    # Напоминалка под полем "Промокод" (просто её див)
    VALUE_MINIMAL_SUM_ZAKAZA = (By.CSS_SELECTOR, 'div.icon_error_block_basket')    # Текст напоминалки: "Минимальная сумма заказа 1 000 ₽ Пожалуйста, добавьте еще товаров в корзину"
