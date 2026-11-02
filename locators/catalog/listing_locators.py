from selenium.webdriver.common.by import By


class LocatorsForListing:
    """Локаторы для страниц листинга (Каталог, Поиск)"""

    URL_PAGE_WITH_SORT = 'https://pfbereg.ru/catalog/aksessuary1/'

    # Сортировка
    SORT_DROPDOWN = (By.CSS_SELECTOR, 'div.filter-panel__sort')    # Кнопка выбора сортировки на странице
    DESC_SORT_PRICE = (By.XPATH, '(//*[text() = "Сначала дорогие"])')    # Выбор в выпадающем списке сортировки "Сначала дорогие"

    # Карточки товаров
    PRODUCT_CARDS = (By.CSS_SELECTOR, 'div.catalog-item')  # Общий класс карточки
    PRICE_ELEMENTS = (By.CSS_SELECTOR, 'span.price__new-val')  # Класс цены
