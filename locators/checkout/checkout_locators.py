from selenium.webdriver.common.by import By


class LocatorsForCheckout:
    """ Локаторы страницы оформления заказа """

    # ==================================================================================================================
    # СТРАНИЦА "ОФОРМЛЕНИЕ ЗАКАЗА"
    # ==================================================================================================================
    TITLE_ON_PAGE = (By.CSS_SELECTOR, 'h1#pagetitle')  # Заголовок на странице "Оформление заказа"
    BLOCK_POKUPATEL = (By.CSS_SELECTOR, 'div#bx-soa-properties')  # Див блока "Покупатель"
    BLOCK_DOSTAVKA = (By.CSS_SELECTOR, 'div.pandd')  # Див блока "Способ доставки"
    BLOCK_ITOGO = (By.CSS_SELECTOR, 'div#bx-soa-total')  # Див блока "Итого"

    # ==================================================================================================================
    # ОФОРМЛЕНИЕ ЗАКАЗА > БЛОК "ПОКУПАТЕЛЬ" > ТАБ "ФИЗИЧЕСКОЕ ЛИЦО"
    # ==================================================================================================================
    TAB_PHYSICAL = (By.XPATH, '//div[contains(@class, "bx-soa")]//label[text()="Физическое лицо"]')  # Блок "Покупатель" > Таб "Физическое лицо"
    INPUT_ENTER_FIO_1 = (By.CSS_SELECTOR, 'div#bx-soa-properties input#soa-property-1')  # Блок "Покупатель" > Таб "Физическое лицо" > Поле "ФИО"
    INPUT_ENTER_EMAIL_1 = (By.CSS_SELECTOR, 'div#bx-soa-properties input#soa-property-2')  # Блок "Покупатель" > Таб "Физическое лицо" > Поле "E-mail"
    INPUT_ENTER_PHONE_1 = (By.CSS_SELECTOR, 'div#bx-soa-properties input#soa-property-3')  # Блок "Покупатель" > Таб "Физическое лицо" > Поле "Телефон"
    BTN_PRODOL_1 = (By.XPATH, '(//div[contains(@class, "bx-soa-more")]//div[text()="Продолжить"])[1]')  # Блок "Покупатель" > Таб "Физическое лицо" > Кнопка "Продолжить"

    ERROR_MSG_UNDER_FIO_INPUT = (By.CSS_SELECTOR, 'div.container-fluid div#tooltip-soa-property-1 div.tooltip-inner')  # Блок "Покупатель" > Таб "Физическое лицо" > Поле "ФИО" > Ошибка под полем
    ERROR_MSG_UNDER_FIO_EMAIL = (By.CSS_SELECTOR, 'div.container-fluid div#tooltip-soa-property-2 div.tooltip-inner')  # Блок "Покупатель" > Таб "Физическое лицо" > Поле "E-mail" > Ошибка под полем
    ERROR_MSG_UNDER_FIO_PHONE = (By.CSS_SELECTOR, 'div.container-fluid div#tooltip-soa-property-3 div.tooltip-inner')  # Блок "Покупатель" > Таб "Физическое лицо" > Поле "Телефон" > Ошибка под полем

    # ==================================================================================================================
    # ОФОРМЛЕНИЕ ЗАКАЗА > БЛОК "ПОКУПАТЕЛЬ" > ТАБ "ЮРИДИЧЕСКОЕ ЛИЦО"
    # ==================================================================================================================
    TAB_LEGAL = (By.XPATH, '//div[contains(@class, "bx-soa")]//label[text()="Юридическое лицо"]')  # Блок "Покупатель" > Таб "Юридическое лицо"
    INPUT_ENTER_COMPANY_NAME = (By.CSS_SELECTOR, 'div.container-fluid input#soa-property-8')  # Блок "Покупатель" > Таб "Юридическое лицо" > Поле "Название компании"
    INPUT_ENTER_ADRESS_COMPANY = (By.CSS_SELECTOR, 'div.container-fluid textarea#soa-property-9')  # Блок "Покупатель" > Таб "Юридическое лицо" > Поле "Юридический адрес"
    INPUT_ENTER_INN = (By.CSS_SELECTOR, 'div.container-fluid input#soa-property-10')  # Блок "Покупатель" > Таб "Юридическое лицо" > Поле "ИНН"
    INPUT_ENTER_KPP = (By.CSS_SELECTOR, 'div.container-fluid input#soa-property-11')  # Блок "Покупатель" > Таб "Юридическое лицо" > Поле "КПП"
    INPUT_ENTER_CONTACT_NAME = (By.CSS_SELECTOR, 'div.container-fluid input#soa-property-12')  # Блок "Покупатель" > Таб "Юридическое лицо" > Поле "Контактное лицо"
    INPUT_ENTER_EMAIL_2 = (By.CSS_SELECTOR, 'div.container-fluid input#soa-property-13')  # Блок "Покупатель" > Таб "Юридическое лицо" > Поле "E-mail"
    INPUT_ENTER_PHONE_2 = (By.CSS_SELECTOR, 'div.container-fluid input#soa-property-14')  # Таб "Юридическое лицо" > Поле "Телефон"
    INPUT_ENTER_OPERATOR_EDO = (By.CSS_SELECTOR, 'div.container-fluid input#soa-property-15')  # Блок "Покупатель" > Таб "Юридическое лицо" > Поле "Оператор ЭДО"
    BTN_PRODOL_2 = (By.XPATH, '(//div[contains(@class, "bx-soa-more")]//div[text()="Продолжить"])[1]')  # Блок "Покупатель" > Таб "Физическое лицо" > Кнопка "Продолжить"

    # ==================================================================================================================
    # ОФОРМЛЕНИЕ ЗАКАЗА > БЛОК "СПОСОБ ДОСТАВКИ" > Доставка транспортной компанией или Озон Доставкой
    # ==================================================================================================================
    BTN_IZMENIT_1 = (By.XPATH, '(//div[contains(@class, "pandd")]//div[text()="Изменить"])[1]')  # Блок "Способ доставки" (Выберите адрес доставки) > Доставка транспортной компанией > Кнопка "Изменить"
    RADIO_DOSTAVKA = (By.XPATH, '//div[contains(@class, "bx-soa-pp-item-container")]//span[text()="Доставка транспортной компанией или Озон Доставкой"]')  # Блок "Способ доставки" (Выберите адрес доставки) > Доставка транспортной компанией > Радиокнопка "Доставка транспортной компанией"
    INPUT_ENTER_ADRESS = (By.CSS_SELECTOR, 'div.pandd div.grid-list__item textarea#soa-property-7')  # Блок "Способ доставки" (Выберите адрес доставки) > Доставка транспортной компанией > Поле "Адрес доставки"
    INPUT_ENTER_INDEX = (By.CSS_SELECTOR, 'div.pandd div.grid-list__item input#zipProperty')  # Блок "Способ доставки" (Выберите адрес доставки) > Доставка транспортной компанией >  Поле "Индекс"
    INPUT_ENTER_COMMENT_1 = (By.CSS_SELECTOR, 'div.pandd div.grid-list__item textarea#orderDescription')  # Блок "Способ доставки" (Выберите адрес доставки) > Доставка транспортной компанией >  Поле "Комментарий к заказу"
    BTN_PRODOL_3 = (By.XPATH, '(//div[contains(@class, "bx-soa-more")]//div[text()="Продолжить"])[2]')  # Блок "Способ доставки" (Выберите адрес доставки) > Доставка транспортной компанией >  Кнопка "Продолжить"

    ERROR_MSG_UNDER_INPUT_INDEX = (By.CSS_SELECTOR, 'div.pandd div#tooltip-zipProperty div.tooltip-inner')  # Блок "Способ доставки" (Выберите адрес доставки) > Доставка транспортной компанией >  Поле "Индекс" > Ошибка под полем

    # ==================================================================================================================
    # ОФОРМЛЕНИЕ ЗАКАЗА > БЛОК "СПОСОБ ДОСТАВКИ" > Самовывоз
    # ==================================================================================================================
    BTN_IZMENIT_2 = (By.XPATH, '(//div[contains(@class, "pandd")]//div[text()="Изменить"])[1]')  # Блок "Способ доставки" (Выберите адрес доставки) > Самовывоз > Кнопка "Изменить"
    RADIO_SAMOVYVOZ = (By.XPATH, '//div[contains(@class, "bx-soa-pp-item-container")]//span[text()="Самовывоз"]')  # Блок "Способ доставки" (Выберите адрес доставки) > Доставка транспортной компанией > Радиокнопка "Доставка транспортной компанией"
    INPUT_ENTER_COMMENT_2 = (By.CSS_SELECTOR, 'div.pandd div.grid-list__item textarea#orderDescription')  # Блок "Способ доставки" (Выберите адрес доставки) > Самовывоз >  Поле "Комментарий к заказу"
    BTN_PRODOL_4 = (By.XPATH,  '(//div[contains(@class, "bx-soa-more")]//div[text()="Продолжить"])[2]')  # Блок "Способ доставки" (Выберите адрес доставки) > Самовывоз >  Кнопка "Продолжить"
    # ==================================================================================================================
    # ОФОРМЛЕНИЕ ЗАКАЗА > БЛОК "ИТОГО"
    # ==================================================================================================================
    INPUT_ENTER_PROMOCODE = (By.CSS_SELECTOR, 'div#bx-soa-total div.bx-soa-coupon input.form-control')  # Блок "Итого" > Поле "Введите промокод или сертификат"
    ### ПРИМЕНЕНИЕ ПРОМОКОДА МОЖНО ПРОВЕРИТЬ МИСКЛИКОМ ПОСЛЕ ВВОДА ###
    MSG_AFTER_ENTER_PROMOCODE = (By.XPATH, '(//span[contains(@class, "bx-soa-tooltip")]//span[text()="Не найден"])[2]')  # Блок "Итого" > Сообщение "Не найден" после ввода промика в поле "Введите промокод или сертификат"
    BTN_OFORM_ZAKAZ = (By.CSS_SELECTOR, 'div#bx-soa-total div.bx-soa-cart-total-button-container a.btn')  # Блок "Итого" > Кнопка "оформить заказ"
    CHECKBOX_1 = (By.XPATH, '//div[contains(@class, "bx-soa-cart-conditions-text")]//span[text()="Продолжая, вы соглашаетесь с "]//a[text()="политикой конфиденциальности"]')  # Блок "Итого" > 1 чекбокс
    CHECKED_CHECKBOX_1 = (By.CSS_SELECTOR, 'div.bx-soa-cart-conditions input#licenses_order')  # Блок "Итого" > "Квадратик" 1 чекбокса (для проверки флажка в нём)
    CHECKBOX_2 = (By.XPATH, '(//div[contains(@class, "bx-soa-cart-conditions-text")]//span[text()="Продолжая, вы соглашаетесь с "]//a[text()="публичной офертой"])')  # Блок "Итого" > 2 чекбокс
    CHECKED_CHECKBOX_2 = (By.CSS_SELECTOR, 'div.bx-soa-cart-conditions input#offer_order')  # Блок "Итого" > "Квадратик" 2 чекбокса (для проверки флажка в нём)
    CHECKBOX_3 = (By.XPATH, '(//div[contains(@class, "bx-soa-cart-conditions-text")]//span[text()="Продолжая, вы соглашаетесь на "])')  # Блок "Итого" > 3 чекбокс
    CHECKED_CHECKBOX_3 = (By.CSS_SELECTOR, 'div.bx-soa-cart-conditions input#marketing_consent')  # Блок "Итого" > "Квадратик" 3 чекбокса (для проверки флажка в нём)