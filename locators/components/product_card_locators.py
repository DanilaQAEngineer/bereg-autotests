from selenium.webdriver.common.by import By


class LocatorsForProductCard:
    """ Локаторы элементов внутри карточки товара в листинге (на странице каталога) """

    IN_FAVORITE_BUTTON = (By.CSS_SELECTOR, 'div.item-action--favorite')  # Локатор кнопки добавления товара в избранное
    IN_COMPARE_BUTTON = (By.CSS_SELECTOR, 'div.item-action--compare')  # Локатор кнопки добавления товара в сравнение
    IN_BASKET_BUTTON = (By.CSS_SELECTOR, 'span.item-action--basket')  # Локатор кнопки добавления товара в корзину

    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.catalog-item a.dark_link')  # Локатор названия карточки (для дальнейшего перехода карточку товара)
    IMG_CARD = (By.CSS_SELECTOR, 'div.sticker--upper')  # Фото карточки товара на странице (чтобы попасть на кнопку - надо навести курсор на фото)
    BTN_FAST_WATCH = (By.CSS_SELECTOR, 'div.btn-default[data-name="fast_view"]')  # Кнопка "Быстрый просмотр"

    NOTIFICATION_AFTER_ADDED_IN_COMPARE = (
    By.CSS_SELECTOR, 'div.notice--link')  # Уведомление после успешного добавления товара в сравнение (сам его див)
    NOTIFICATION_AFTER_ADDED_IN_FAVORITE = (
    By.CSS_SELECTOR, 'div.notice__inner')  # Уведомление после успешного добавления товара в избранное (сам его див)
    NOTIFICATION_AFTER_ADDED_IN_BASKET = (
    By.CSS_SELECTOR, 'div.notice__inner')  # Уведомление после успешного добавления товара в корзину (сам его див)

