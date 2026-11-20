from selenium.webdriver.common.by import By


class LocatorsForFooterMenu:
    """ Локаторы футера """

    # ==================================================================================================================
    # ФУТЕР
    # ==================================================================================================================
    TITLE_SUBSCRIBES_IN_FOOTER = (By.CSS_SELECTOR, 'footer#footer div.subscribe-block__text')  # Футер > Заголовок "Подписаться на новости и акции"
    INPUT_EMAIL_IN_FOOTER = (By.CSS_SELECTOR, 'footer#footer input[name="EMAIL"]')  # Футер > Поле ввода почты
    BTN_SUBSCRIBES_IN_FOOTER = (By.CSS_SELECTOR, 'footer#footer div.subscribe-trigger')  # Футер > Кнопка "Подписаться"

    # ==================================================================================================================
    # МОДАЛКА "ПОДПИСКА НА РАССЫЛКУ"
    # ==================================================================================================================
    MODAL_SUBSCRIBES = (By.CSS_SELECTOR, 'div.flexbox.scrollbar div#popup_subscribe_container')  # Модалка "Подписка на рассылку"
    TITLE_IN_MODAL_SUBSCRIBES = (By.CSS_SELECTOR, 'div.flexbox.scrollbar div.title')  # Модалка "Подписка на рассылку" > Заголовок
    INPUT_EMAIL_IN_MODAL_SUBSCRIBES = (By.CSS_SELECTOR, 'div.flexbox.scrollbar input[name="EMAIL"]')  # Модалка "Подписка на рассылку" > Поле ввода почты
    #CAPTCHA_IN_MODAL_SUBSCRIBES = (By.CSS_SELECTOR, '')
    CHECKBOX_IN_MODAL_SUBSCRIBES = (By.XPATH, '(//span[text()="Продолжая, вы соглашаетесь с "])')  # Модалка "Подписка на рассылку" > Строка с согласием (для клика по чекбоксу)
    CHECKED_CHECKBOX_IN_MODAL_SUBSCRIBES = (By.CSS_SELECTOR, 'div.flexbox.scrollbar input#licenses_subscribe_popup')  # Модалка "Подписка на рассылку" > "Квадратик" чекбокса (для проверки флажка в нём)
    BTN_SUBSCRIBES_IN_MODAL_SUBSCRIBES = (By.CSS_SELECTOR, 'div.flexbox.scrollbar button[type="submit"]')  # Модалка "Подписка на рассылку" > Кнопка "Подписаться"
    BTN_CLOSE_MODAL_SUBSCRIBES = (By.CSS_SELECTOR, 'div#popup_iframe_wrapper i.svg')  # Модалка "Подписка на рассылку" > Кнопка "Закрыть модалку"

    ERROR_UNDER_INPUT_EMAIL_IN_MODAL_SUBSCRIBES = (By.CSS_SELECTOR, 'div.flexbox.scrollbar label#EMAIL-error')  # Модалка "Подписка на рассылку" > Сообщение под полем "Почта": +Заполните это поле!; +Неверный формат!
    ERROR_UNDER_CAPTCHA_IN_MODAL_SUBSCRIBES = (By.CSS_SELECTOR, 'div.flexbox.scrollbar label#-error')  # Модалка "Подписка на рассылку" > Сообщение под полем "Капча": +Пройдите проверку
    ERROR_UNDER_CHECKBOX_IN_MODAL_SUBSCRIBES = (By.CSS_SELECTOR, 'div.flexbox.scrollbar label#licenses_subscribe-error')  # Модалка "Подписка на рассылку" > Сообщение под полем-чекбоксом: +Согласитесь с условиями
