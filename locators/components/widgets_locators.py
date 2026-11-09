from selenium.webdriver.common.by import By


class LocatorsForWidgets:
    """ Локаторы для выпадающих виджетов в шапке (Корзина, Избранное, Сравнение) """

    # --- Мини-Сравнение (виджет) ---
    ICON_WIDGET_COMPARE = (By.XPATH, '(//i[contains(@class, "compare") and contains(@class, "header__icon")])[1]')  # Иконка "Сравнение" в хедере
    COUNT_ICON_IN_COMPARE = (By.XPATH, '(//*[@class="icon-count icon-count--compare bg-more-theme count"])[1]')  # Иконка с количеством товаров в разделе
    DROPDOWN_MINICOMPARE = (By.XPATH, '(//*[@class="compare-dropdown product-dropdown-hover-block loaded"])[1]')  # Выпадающее меню при наведении курсора на иконку "Сравнение"
    FIRST_CARD_IN_DROPDOWN_COMPARE = (By.XPATH, '(//*[@class="dropdown-product__item js-popup-block"])[1]')  # Первый товар в выпадашке
    TITLE_FIRST_CARD_IN_COMPARE = (By.XPATH, '(//*[@class="dark_link"])[3]')  # Заголовок/название первого товара в разделе (по клику редиректит на его страницу)
    BTN_REMOVE_FIRST_CARD_IN_COMPARE = (By.XPATH, '(//*[@class="svg inline remove  inline "])[1]')  # Кнопка удаления первого товара из сравнения/выпадашки
    DROPDOWN_WITH_BTN_IN_COMPARE = (By.XPATH, '(//*[@class="foot dropdown dropdown--relative dropdown-product-foot dropdown-product-foot--one-btn"])[1]')  # Блок_див выпадашки с кнопкой "В сравнение"
    BTN_IN_COMPARE = (By.XPATH, '(//*[@href="/catalog/compare.php"])[2]')  # Кнопка "В сравнение" (переход в раздел сравнения товаров)

    # --- Мини-Избранное (виджет) ---
    ICON_WIDGET_FAVORITE = (By.CSS_SELECTOR, 'div[data-ajax-load-block="HEADER_TOGGLE_FAVORITE"]')  # Иконка "Избранное" в хедере
    ICON_COUNT_IN_FAVORITE = (By.XPATH, '(//*[@class="icon-count icon-count--favorite bg-more-theme count"])[1]')  # Иконка с количеством товаров в разделе
    DROPDOWN_MINIFAVORITE = (By.XPATH, '(//*[@class="favorite-dropdown product-dropdown-hover-block loaded"])[1]')  # Выпадающее меню при наведении курсора на иконку "Избранное"
    FIRST_CARD_IN_DROPDOWN_FAVORITE = (By.XPATH, '(//*[@class="dropdown-product__item js-popup-block"])[1]')  # Первый товар в выпадашке
    TITLE_FIRST_CARD_IN_FAVORITE = (By.XPATH, '(//*[@class="dark_link"])[1]')  # аголовок/название первого товара в разделе (по клику редиректит на его страницу)
    BTN_REMOVE_FIRST_CARD_IN_FAVORITE = (By.XPATH, '(//*[@data-action="favorite"])[1]')  # Кнопка удаления первого товара из избранного/выпадашки
    DROPDOWN_WITH_BTN_IN_FAVORITE = (By.XPATH, '(//*[@class="foot dropdown dropdown--relative dropdown-product-foot dropdown-product-foot--one-btn"])[1]')  # Блок_див выпадашки с кнопкой "В избранное"
    BTN_IN_FAVORITE = (By.XPATH, '(//*[@class="btn btn-default btn-wide has-ripple"])[1]')  # Кнопка "В избранное" (переход в раздел избранных товаров)

    # --- Мини-Корзина (виджет) ---
    ICON_WIDGET_BASKET = (By.CSS_SELECTOR, 'div[data-ajax-load-block="HEADER_TOGGLE_BASKET"]')  # Иконка "Корзина" в хедере
    ICON_COUNT_IN_BASKET = (By.XPATH, '(//*[@class="header-cart__count bg-more-theme count"])[1]')  # Иконка с количеством товаров в разделе
    DROPDOWN_MINIBASKET = (By.XPATH, '(//*[@class="wrap_cont dropdown-product-wrap"])[1]')  # Выпадающее меню при наведении курсора на иконку "Корзина"
    FIRST_CARD_IN_DROPDOWN_BASKET = (By.XPATH, '(//*[@class="foot dropdown dropdown--relative dropdown-product-foot"])[1]')  # Первый товар в выпадашке
    TITLE_FIRST_CARD_IN_BASKET = (By.XPATH, '(//*[@class="dark_link"])[1]')  # аголовок/название первого товара в разделе (по клику редиректит на его страницу)
    BTN_REMOVE_FIRST_CARD_IN_BASKET = (By.XPATH, '(//*[@class="dropdown-product__item-remove remove fill-dark-light-block fill-theme-use-svg-hover"])[1]')  # Кнопка удаления первого товара из корзины/выпадашки
    DROPDOWN_WITH_SUM_AND_BTN = (By.XPATH, '(//*[@class="foot dropdown dropdown--relative dropdown-product-foot"])[1]')  # Блок_див выпадашки со стоимостью и кнопкой "В корзину"
    FINAL_SUM_CARDS_IN_BASKET = (By.XPATH, '(//*[@class="line-block__item cart-total__value"])[1]')  # Значение поля "Итого" (стоимость всех товаров в корзине)
    BTN_IN_BASKET = (By.XPATH, '(//*[@class="btn btn-default btn-wide has-ripple"])[1]')  # Кнопка "В избранное" (переход в раздел избранных товаров)
