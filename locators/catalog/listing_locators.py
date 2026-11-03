from selenium.webdriver.common.by import By


class LocatorsForListing:
    """Локаторы для страниц листинга (Каталог, Поиск)"""

    URL_PAGE_WITH_SORT = 'https://pfbereg.ru/catalog/aksessuary1/'

    # Сортировка на странице каталога
    SORT_DROPDOWN = (By.CSS_SELECTOR, 'div.filter-panel__sort')    # Кнопка выбора сортировки на странице
    ASC_SORT_PRICE = (By.XPATH, '(//*[text() = "Сначала дешевые"])[2]')  # Выбор в выпадающем списке сортировки "Сначала дешевые"
    DESC_SORT_PRICE = (By.XPATH, '(//*[text() = "Сначала дорогие"])[2]')    # Выбор в выпадающем списке сортировки "Сначала дорогие"

    # Сортировка на странице с результатами поиска
    SORT_DROPDOWN_ON_RESULT_SEARCH_PAGE = (By.XPATH, '(//*[text()="По релевантности"])[3]')  # Кнопка выбора сортировки на странице

    # Карточки товаров
    PRODUCT_CARDS = (By.CSS_SELECTOR, 'div.catalog-item')  # Общий класс карточки
    PRICE_ELEMENTS = (By.CSS_SELECTOR, 'span.price__new-val')  # Класс цены
