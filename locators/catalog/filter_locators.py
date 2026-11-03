from selenium.webdriver.common.by import By


class LocatorsForFilters:
    """Локаторы панели фильтров (сайдбар)"""

    #BASE_PAGE = 'https://pfbereg.ru/'

    #    Меню фильтров: (ВАЖНО: нужно будет так же добавить локаторы ползунков и кнопок "вверх-вниз" внутри самих фильтров)
    INPUT_MIN_PRICE = (By.CSS_SELECTOR, 'input.min-price')
    INPUT_MAX_PRICE = (By.CSS_SELECTOR, 'input.max-price')

    CHECKBOX_HIT = (By.CSS_SELECTOR, 'label[data-role="label_MAX_SMART_FILTER_89_2103780943"]')
    CHECKBOX_RECOMENDATE = (By.CSS_SELECTOR, 'label[data-role="label_MAX_SMART_FILTER_89_174200537"]')
    CHECKBOX_NEW = (By.CSS_SELECTOR, 'label[data-role="label_MAX_SMART_FILTER_89_2483454842"]')
    CHECKBOX_BEREG = (By.CSS_SELECTOR, 'label[data-role="label_MAX_SMART_FILTER_90_3895070348"]')
    CHECKBOX_V_NALICHII = (By.CSS_SELECTOR, 'label[data-role="label_MAX_SMART_FILTER_91_2003519797"]')
    COLOR_1 = (By.CSS_SELECTOR, 'label[data-role="label_MAX_SMART_FILTER_272_3197246697"]')
    COLOR_2 = (By.CSS_SELECTOR, 'label[data-role="label_MAX_SMART_FILTER_272_757113898"]')    # Остальные локаторы тоже лучше забирать по data-role
    COLOR_3 = (By.CSS_SELECTOR, 'label[for="MAX_SMART_FILTER_272_2205888181"]')
    COLOR_4 = (By.CSS_SELECTOR, 'label[for="MAX_SMART_FILTER_272_1423390776"]')
    COLOR_5 = (By.CSS_SELECTOR, 'label[for="MAX_SMART_FILTER_272_2142381090"]')
    MODEL_1 = (By.CSS_SELECTOR, 'label[data-role="label_MAX_SMART_FILTER_592_3878939785"]')
    MODEL_2 = (By.CSS_SELECTOR, 'label[data-role="label_MAX_SMART_FILTER_592_2261890934"]')
    MODEL_3 = (By.CSS_SELECTOR, 'label[data-role="label_MAX_SMART_FILTER_592_2419383327"]')

    RESET_BUTTON = (By.ID, 'del_filter')
