from selenium.webdriver.common.by import By


class ProductLocators:
    """ Локаторы страницы карточки товара """

    #    Локаторы элементов карточки страницы:
    BREADCRUMBS = (By.CSS_SELECTOR, 'div.breadcrumbs')
    TITLE_CARD = (By.CSS_SELECTOR, 'h1.switcher-title')

    #    Локаторы табов на странице карточки:
    TAB_DESCRIPTION = (By.XPATH, '(//*[contains(text(), "Описание")])[1]')
    CONTENT_TAB_DESCRIPTION = (By.CSS_SELECTOR, 'div.js-detail-description')
    TAB_OTZ = (By.XPATH, '(//*[contains(text(), "Отзывы")])[2]')
    CONTENT_TAB_OTZ = (By.CSS_SELECTOR, 'div.blog-comment__container')
    TAB_OPL = (By.XPATH, '(//*[contains(text(), "Оплата")])[1]')
    CONTENT_TAB_OPL = (By.CSS_SELECTOR, 'div.tab-pane#payment')
    TAB_DOST = (By.XPATH, '(//*[contains(text(), "Доставка")])[1]')
    CONTENT_TAB_DOST = (By.CSS_SELECTOR, 'div.tab-pane#delivery')
    TAB_VOPR = (By.XPATH, '(//*[contains(text(), "Вопросы о товаре")])[1]')
    CONTENT_TAB_VOPR = (By.CSS_SELECTOR, 'div.red-comments-module')

    #    Кнопки действий на странице карточки товара
    BTN_IN_BASKET = (By.XPATH, '(//*[@data-action="basket"])[1]')
    NOTIFICATION_AFTER_ADD_BASKET = (By.CSS_SELECTOR, 'div.line-block--align-flex-start')
    TITLE_NOTIFICATION_AFTER_ADD_BASKET = (By.CSS_SELECTOR, 'div.notice__title')    # Название уведомления: "В корзине"
    TEXT_NOTIFICATION_AFTER_ADD_BASKET = (By.CSS_SELECTOR, 'div.notice__detail')    # Название карточки товара в уведомлении
