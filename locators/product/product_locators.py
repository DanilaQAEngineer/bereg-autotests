from selenium.webdriver.common.by import By


class ProductLocators:
    """ Локаторы страницы карточки товара """

    #    Локаторы элементов карточки страницы:
    BREADCRUMBS = (By.CSS_SELECTOR, 'div.breadcrumbs')
    TITLE_CARD = (By.CSS_SELECTOR, 'h1.switcher-title')

    #    Локаторы табов на странице карточки:
    TAB_DESCRIPTION = (By.XPATH, '(//*[@data-toggle="tab"])[1]')
    CONTENT_TAB_DESCRIPTION = (By.CSS_SELECTOR, 'div.js-detail-description')
    TAB_OTZ = (By.XPATH, '(//*[@data-toggle="tab"])[5]')
    CONTENT_TAB_OTZ = (By.CSS_SELECTOR, 'div.blog-comment__container')
    TAB_DOST = (By.XPATH, '(//*[@data-toggle="tab"])[7]')
    CONTENT_TAB_DOST = (By.CSS_SELECTOR, 'div.tab-pane#delivery')

    #    Кнопки действий на странице карточки товара
    BTN_IN_BASKET = (By.XPATH, '(//*[@data-action="basket"])[1]')
    NOTIFICATION_AFTER_ADD_BASKET = (By.CSS_SELECTOR, 'div.line-block--align-flex-start')
    TITLE_NOTIFICATION_AFTER_ADD_BASKET = (By.CSS_SELECTOR, 'div.notice__title')    # Название уведомления: "В корзине"
    TEXT_NOTIFICATION_AFTER_ADD_BASKET = (By.CSS_SELECTOR, 'div.notice__detail')    # Название карточки товара в уведомлении
