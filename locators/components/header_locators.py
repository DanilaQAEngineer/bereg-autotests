from selenium.webdriver.common.by import By


class LocatorsForHeader:
    """Локаторы элементов хедера"""

    # Логотип
    LOGO = (By.CSS_SELECTOR, '.header__main-part.header__main-part--long.part-with-search .header__main-item .logo.line-block__item.no-shrinked')

    # Город (слева сверху + его модалка)
    CITY_BUTTON = (By.XPATH, '(//*[@data-name="city_chooser"])[1]')
    CITY_MODAL = (By.CSS_SELECTOR, '.city_chooser_frame.jqmWindow.popup.jqm-init.show')    # Модалка выбора города

    # Контакты
    PHONE_ICON = (By.XPATH, '(//*[@class="phones__inner phones__inner--big fill-theme-parent"])[1]')    # Иконка/блок наведения на телефон
    CALL_REQUEST_BUTTON = (By.CSS_SELECTOR, '.animate-load.btn.btn-default.btn-wide.btn-sm.has-ripple')    # Кнопка в выпадашке

    # Глобальный поиск (строка и иконка)
    SEARCH_INPUT = (By.CSS_SELECTOR, '.search-input-div .search-input.font_16.banner-light-text.form-control[id="title-search-input"]')    # Поле ввода поиска
    SEARCH_BUTTON = (By.CSS_SELECTOR, '')    # Кнопка лупы