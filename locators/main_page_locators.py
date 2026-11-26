from selenium.webdriver.common.by import By


class LocatorsForMainPage:
    """ Локаторы главной страницы сайта """

    # ==================================================================================================================
    # БАННЕРНАЯ КАРУСЕЛЬ
    # ==================================================================================================================
    CURRENT_BANNER_ON_PAGE = (By.CSS_SELECTOR, 'div.swiper-slide-active a.target')  # Ссылка текущего баннера в карусели
    BTN_NEXT_SLIDE = (By.CSS_SELECTOR, 'div.slider-nav-wrap div.swiper-button-next')
    BTN_PREV_SLIDE = (By.CSS_SELECTOR, 'div.slider-nav-wrap div.swiper-button-prev')

    # ==================================================================================================================
    # БЛОК "БЕСТСЕЛЛЕРЫ"
    # ==================================================================================================================
    TITLE_BESTSELLER = (By.CSS_SELECTOR, 'div.CATALOG_TAB a.stroke-theme-hover')  # Бестселлеры > Заголовок блока
    TAG_IN_CARD_LISTING_BESTSELLER = (By.XPATH, '//div[contains(@class, "CATALOG_TAB")]//div[contains(@class, "sticker--upper")]')  # Бестселлеры > Тэг в карточек товара на странице

    ### ФИЛЬТРЫ БЛОКА "БЕСТСЕЛЛЕРЫ"
    FILTER_HIT = (By.XPATH, '//div[contains(@class, "CATALOG_TAB")]//span[text()="Хит"]')  # Бестселлеры > Таб "Хит"
    FILTER_RECOMMEND = (By.XPATH, '//div[contains(@class, "CATALOG_TAB")]//span[text()="Советуем"]')  # Таб "Бестселлеры > "Советуем"
    FILTER_NEW = (By.XPATH, '//div[contains(@class, "CATALOG_TAB")]//span[text()="Новинка"]')  # Бестселлеры > Таб "Новинка"
    FILTER_STOCK = (By.XPATH, '//div[contains(@class, "CATALOG_TAB")]//span[text()="Акция"]')  # Бестселлеры > Таб "Акция"

    # ==================================================================================================================
    # БЛОК "ПОХОДНЫЕ ПАЛАТКИ И ПЕЧИ"
    # ==================================================================================================================
    TITLE_PECHI = (By.CSS_SELECTOR, 'div.CUSTOM_CATALOG a.stroke-theme-hover')  # Походные палатки и печи > Заголовок блока
    TITLE_IN_CARD_LISTING_PECHI = (By.CSS_SELECTOR, 'div.CUSTOM_CATALOG div.catalog-block a.switcher-title')  # Походные палатки и печи > Названия карточек товаров на странице

    ### ФИЛЬТРЫ БЛОКА "БЕСТСЕЛЛЕРЫ"
    FILTER_PALATKI = (By.XPATH, '//div[contains(@class, "CUSTOM_CATALOG")]//span[text()="Палатки"]')  # Походные палатки и печи > Таб "Палатки"
    FILTER_ARM_PALATKI = (By.XPATH, '//div[contains(@class, "CUSTOM_CATALOG")]//span[text()="Армейские палатки"]')  # Походные палатки и печи > Таб "Армейские палатки"
    FILTER_BANI = (By.XPATH, '//div[contains(@class, "CUSTOM_CATALOG")]//span[text()="Походные бани"]')  # Походные палатки и печи > Таб "Походные бани"
    FILTER_PECHI = (By.XPATH, '//div[contains(@class, "CUSTOM_CATALOG")]//span[text()="Походные печи"]')  # Походные палатки и печи > Таб "Походные печи"
    FILTER_MEBEL = (By.XPATH, '//div[contains(@class, "CUSTOM_CATALOG")]//span[text()="Мебель"]')  # Походные палатки и печи > Таб "Мебель"