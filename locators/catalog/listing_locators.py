from selenium.webdriver.common.by import By


class LocatorsForListing:
    """Локаторы для страниц листинга (Каталог, Поиск)"""

    URL_PAGE_WITH_SORT = 'https://pfbereg.ru/catalog/aksessuary1/'

    # Сортировка на странице каталога
    SORT_DROPDOWN = (By.CSS_SELECTOR, 'div.filter-panel__sort')    # Кнопка выбора сортировки на странице
    ASC_SORT_PRICE = (By.XPATH, '(//*[text()="Сначала дешевые"])[2]')  # Выбор в выпадающем списке сортировки "Сначала дешевые"
    DESC_SORT_PRICE = (By.CSS_SELECTOR, 'a[data-url="/catalog/aksessuary1/dlya-palatok/?sort=CATALOG_PRICE_1&order=desc"]')    # Выбор в выпадающем списке сортировки "Сначала дорогие"

    # Сортировка на странице с результатами поиска
    SORT_DROPDOWN_ON_RESULT_SEARCH_PAGE = (By.XPATH, '(//*[text()="По релевантности"])[3]')  # Кнопка выбора сортировки на странице

    # Карточки товаров
    PRODUCT_CARDS = (By.CSS_SELECTOR, 'div.catalog-item')  # Общий класс карточки товара на странице каталога
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.catalog-item a.dark_link')  # Локатор названия карточки (для дальнейшего перехода карточку товара)
    BTN_FAST_WATCH = (By.CSS_SELECTOR, 'div.btn-default[data-name="fast_view"]')  # Кнопка "Быстрый просмотр"
    PRICE_NEW = (By.CSS_SELECTOR, 'span.price__new-val')  # Актуальная цена в карточке товара
    PRICE_OLD = (By.CSS_SELECTOR, 'span.price__old-val')  # Старая цена в карточке товара (зачёркнутая)
