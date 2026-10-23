from selenium.webdriver.common.by import By    # импортировали «способ поиска»: говорим Selenium, как искать элемент: == By.CSS_SELECTOR.XPATH.ID



class LocatorsForCatalogPageSectionAccessories:
    CATALOG_BUTTON = (By.XPATH, '(//*[@class="header-menu__link--only-catalog fill-use-fff btn btn-default btn--no-rippple btn-lg"])[1]')

    #    1. Локаторы основной страницы каталога:
    CATEGORY_ACCESSORIES = (By.XPATH, '(//*[@class="font_16 font_weight--500 dark_link switcher-title header-menu__wide-child-link fill-theme-hover"])[8]')

    #    2. Локаторы страницы раздела "Аксессуары":
    TITLE_PAGE = (By.CSS_SELECTOR, '.topic #pagetitle')
    COUNT_TOVAROV = (By.CSS_SELECTOR, '.topic .element-count.color_999.rounded-4')
    KROSHKI = (By.CSS_SELECTOR, '.cowl .breadcrumbs.swipeignore')
    BLOKI_CATEGORY = (By.CSS_SELECTOR, '.sections-block.main-template [class="grid-list  grid-list--fill-bg normal grid-list--items-5-1200  grid-list--items-4-992  grid-list--items-3-768 grid-list--items-2-601"]')
    SUBCATEGORY_DLYA_PALATOK = (By.CSS_SELECTOR, '.top-content-block [href="/catalog/aksessuary1/dlya-palatok/"]')
    SUBCATEGORY_DLYA_BAN = (By.CSS_SELECTOR, '.top-content-block [href="/catalog/aksessuary1/dlya-ban/"]')
    SUBCATEGORY_DLYA_PECHEY = (By.CSS_SELECTOR, '.top-content-block [href="/catalog/aksessuary1/dlya-pechey/"]')
    SUBCATEGORY_DLYA_MEBELI = (By.CSS_SELECTOR, '.top-content-block [href="/catalog/aksessuary1/dlya-mebeli/"]')
    SUBCATEGORY_DLYA_AEROLODOK = (By.CSS_SELECTOR, '.top-content-block [href="/catalog/aksessuary1/dlya-aerolodok/""]')
    BUTTON_NAVERH = (By.CSS_SELECTOR, '.scroll-to-top.ROUND_COLOR.PADDING.animated.visible.rotateIn#scrollToTop')
    ACTUAL_PRICE_IN_CARD = (By.CSS_SELECTOR, '.js-popup-price .price__new')

    #    3. Локаторы сортировки и фильтров:
    SORT_DROPDOWN = (By.CSS_SELECTOR, '.line-block__item .dropdown-select__title.font_14.font_large.fill-dark-light.bordered.rounded-x.shadow-hovered.shadow-no-border-hovered')    # Кнопка выбора сортировки по: алфавиту, цене, популярности
    ASC_SORT_BY_ALPHABET = (By.XPATH, '(//*[text()="С начала алфавита"])')
    DESC_SORT_BY_ALPHABET = (By.XPATH, '(//*[text()="С конца алфавита"])')
    ASC_SORT_BY_PRICE = (By.XPATH, '(//*[text()="Сначала дешевые"])')    # Эта сортировка на странице по умолчанию !!!
    DESC_SORT_BY_PRICE = (By.XPATH, '(//*[text()="Сначала дорогие"])')
    SORT_2 = (By.CSS_SELECTOR, '.filter-panel__part-right .toggle-panel.hide-600')    # Кнопка выбора сортировки по: количеству карточек на странице

    FILTERS_MENU = (By.CSS_SELECTOR, '.left_block.visible-by-block-presence .sticky-block.sticky-block--show-N')
    FILTERS_MIN_PRICE = (By.CSS_SELECTOR, '.bx_filter_block #MAX_SMART_FILTER_P1_MIN')
    FILTERS_MAX_PRICE = (By.CSS_SELECTOR, '.bx_filter_block #MAX_SMART_FILTER_P1_MAX')
    MESSAGE_BEZ_RESULTATOV = (By.CSS_SELECTOR, '.no_products .big_text.font_24')

    #    3.1. Локаторы пагинации:
    PAGINATION = (By.CSS_SELECTOR, '.bottom_nav_wrapper.nav-compact .module-pagination')
    NEXT_OR_TWO_PAGE_IN_PAGINATION = (By.CSS_SELECTOR, '.bottom_nav_wrapper.nav-compact .module-pagination [href="/catalog/aksessuary1/?PAGEN_1=2"]')    # тут можно обращаться к любой странице в пагинации, заменив последнюю цсфру
    BUTTON_ZAGRUZIT_ESHE = (By.CSS_SELECTOR, '.bottom_nav_wrapper.nav-compact .more_text_ajax.btn.btn-transparent.has-ripple')


    #    4. Переход в карточку товара:
    BUTTON_ADD_FAVORITIES = {By.CSS_SELECTOR, '.image-list .item-action.item-action--vertical.item-action--favorite [data-id="3693"]'}    # Локатор кнопки добавления в избранное
    BUTTON_SRAVNIT = (By.CSS_SELECTOR, '.item-action.item-action--vertical.item-action--compare [data-id="3693"]')
    BUTTON_BYSTR_PROSMOTR = (By.CSS_SELECTOR, '.btn-fast-view.rounded-x.hide-600 .btn.btn-xs.btn-default.has-ripple')
    BUTTON_ADD_IN_BASKET = (By.CSS_SELECTOR, '.buy_block.btn-actions__inner [data-id="3693"]')
    PEREHOD_V_KARTOCHKU_TOVARA = (By.CSS_SELECTOR, '.catalog-block__info-inner [href="/catalog/aksessuary1/dlya-palatok/vvertyshi-dlya-palatki/?oid=4032"]')

    #    5. Локаторы карточки товара:
    NAME_CARD = (By.CSS_SELECTOR, '.catalog-detail__main .font_32.switcher-title.js-popup-title.font_20--to-600')