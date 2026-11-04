from selenium.webdriver.common.by import By


class LocatorsForHeader:
    """Локаторы элементов хедера"""

    BASE_PAGE = 'https://pfbereg.ru/'
    CLOSE_MODAL_VERIFID_CITY = (By.XPATH, '(//*[@title="Закрыть"])[2]')

    # Логотип
    LOGO = (By.CSS_SELECTOR, 'a.menu-light-icon-fill.banner-light-icon-fill')

    # Город (слева сверху + его модалка)
    CITY_BUTTON = (By.XPATH, '(//*[@data-name="city_chooser"])[1]')
    CITY_MODAL = (By.CSS_SELECTOR, 'div.city_chooser_frame')    # Модалка выбора города

    # Контакты в шапке сайта:
    PHONE_ICON = (By.CSS_SELECTOR, '.header__top-item[data-ajax-load-block="HEADER_TOGGLE_PHONE"]')    # Иконка/блок наведения на телефон
    CALL_REQUEST_BUTTON = (By.XPATH, '(//*[@class="phones__dropdown-item callback-item"])[1]')    # Кнопка в выпадашке

    # Виджеты (иконки в шапке)
    LK_WIDGET_ICON = (By.CSS_SELECTOR, '.line-block__item[data-ajax-load-block="HEADER_TOGGLE_CABINET"]')    # Кнопка_иконка "Войти"
    COMPARE_WIDGET_ICON = (By.CSS_SELECTOR, '.line-block__item[data-ajax-load-block="HEADER_TOGGLE_COMPARE"]')    # Кнопка_иконка "Список сравниваемых элементов"
    COMPARE_COUNTER = (By.CSS_SELECTOR, 'span.icon-count--compare')  # Иконка с количеством товаров в сравнении
    FAVORITES_WIDGET_ICON = (By.CSS_SELECTOR, '.line-block__item[data-ajax-load-block="HEADER_TOGGLE_FAVORITE"]')    # Кнопка_иконка "Избранные товары"
    FAVORITE_COUNTER = (By.CSS_SELECTOR, 'span.icon-count--favorite')  # Иконка с количеством товаров в избранном
    BASKET_WIDGET_ICON = (By.CSS_SELECTOR, '.line-block__item[data-ajax-load-block="HEADER_TOGGLE_BASKET"]')    # Кнопка_иконка "Корзина"
    BASKET_COUNTER = (By.CSS_SELECTOR, 'span.header-cart__count')    # Иконка с количеством товаров в корзине

    # Глобальный поиск
    SEARCH_INPUT = (By.ID, 'title-search-input')    # Поле ввода поиска
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.search-button-div')    # Кнопка поиска (лупа)
    SEARCH_CLEAR_BTN = (By.CSS_SELECTOR, 'button.btn-clear-search')    # Кнопка удаления запроса из поля (х)
    SEARCH_DROPDOWN = (By.CSS_SELECTOR, 'div.searche-result.scrollbar')    # Выпадающий список с результатами поиска
    SEARCH_RESULT_ITEMS = (By.CSS_SELECTOR, 'a.bx_item_block')    # Карточка товара в результирующем списке (в выпадашке)
