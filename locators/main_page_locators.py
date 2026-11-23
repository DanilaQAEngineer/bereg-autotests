from selenium.webdriver.common.by import By


class LocatorsForMainPage:
    """ Локаторы главной страницы сайта """

    # ==================================================================================================================
    # БАННЕРНАЯ КАРУСЕЛЬ
    # ==================================================================================================================
    BTN_PREV_SLIDE = (By.CSS_SELECTOR, 'div.slider-nav-wrap div.swiper-button-prev')
    BTN_NEXT_SLIDE = (By.CSS_SELECTOR, 'div.slider-nav-wrap div.swiper-button-next')
    CURRENT_BANNER_ON_PAGE = (By.CSS_SELECTOR, 'div.maxwidth-banner a.target')  # Текущий баннер в карусели

    # ==================================================================================================================
    # БЛОК "БЕСТСЕЛЛЕРЫ"
    # ==================================================================================================================
    TITLE_BESTSELLEAR = (By.CSS_SELECTOR, 'div.CATALOG_TAB a.stroke-theme-hover')  # Бестселлеры > Заголовок блока
    TAG_IN_CARD_LISTING_BESTSEALER = (By.CSS_SELECTOR, 'div.CATALOG_TAB div.catalog-block div.sticker__item-content')  # Бестселлеры > Тэг в карточек товара на странице
    TAB_HIT = (By.XPATH, '//div[contains(@class, CATALOG_TAB)]//span[contains(text(), "Хит")]')  # Бестселлеры > Таб "Хит"
    TAB_RECOMMEND = (By.XPATH, '//div[contains(@class, CATALOG_TAB)]//span[contains(text(), "Советуем")]')  # Таб "Бестселлеры > Советуем"
    TAB_NEW = (By.XPATH, '//div[contains(@class, CATALOG_TAB)]//span[contains(text(), "Новинка")]')  # Бестселлеры > Таб "Новинка"
    TAB_STOCK = (By.XPATH, '//div[contains(@class, CATALOG_TAB)]//span[contains(text(), "Акция")]')  # Бестселлеры > Таб "Акция"

    # ==================================================================================================================
    # БЛОК "ПОХОДНЫЕ ПАЛАТКИ И ПЕЧИ"
    # ==================================================================================================================
    TITLE_PECHI = (By.CSS_SELECTOR, 'div.CUSTOM_CATALOG a.stroke-theme-hover')  # Походные палатки и печи > Заголовок блока
    TAG_IN_CARD_LISTING_PECHI = (By.CSS_SELECTOR,'div.CUSTOM_CATALOG div.catalog-block div.sticker__item-content')  # Походные палатки и печи > Тэг в карточек товара на странице
    TAB_PALATKI = (By.XPATH, '(//span[text()="Палатки"])[4]')  # Походные палатки и печи > Таб "Палатки"
    TAB_ARM_PALATKI = (By.XPATH, '(//span[text()="Армейские палатки"])[4]')  # Походные палатки и печи > Таб "Армейские палатки"