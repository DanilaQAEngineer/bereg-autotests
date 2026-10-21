import allure
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from config.settings import settings
from pages.base_page import BasePage


@allure.description("добавить описание страницы")
class SectionAccessoriesInCatalogPage(BasePage):
    """Раздел "Аксессуары" в меню каталога"""

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

    #    3. Локаторы сортировки и фильтров:
    SORT_1 = (By.CSS_SELECTOR, '.line-block__item .dropdown-select__title.font_14.font_large.fill-dark-light.bordered.rounded-x.shadow-hovered.shadow-no-border-hovered')    # Сортировка по: алфавиту, цене, популярности
    SORT_ALPHABET = (By.XPATH, '(//*[text()="С начала алфавита"])')
    SORT_2 = (By.CSS_SELECTOR, '.filter-panel__part-right .toggle-panel.hide-600')    # Сортировка по: количеству карточек на странице

    FILTERS_MENU = (By.CSS_SELECTOR, '.left_block.visible-by-block-presence .sticky-block.sticky-block--show-N')
    FILTERS_MIN_PRICE = (By.CSS_SELECTOR, '.bx_filter_block #MAX_SMART_FILTER_P1_MIN')
    FILTERS_MAX_PRICE = (By.CSS_SELECTOR, '.bx_filter_block #MAX_SMART_FILTER_P1_MAX')
    MESSAGE_BEZ_RESULTATOV = (By.CSS_SELECTOR, '.no_products .big_text.font_24')

    #    3.1. Локаторы пагинации:
    PAGINATION = (By.CSS_SELECTOR, '.bottom_nav_wrapper.nav-compact .module-pagination')
    NEXT_OR_TWO_PAGE_IN_PAGINATION = (By.CSS_SELECTOR, '.bottom_nav_wrapper.nav-compact .module-pagination [href="/catalog/aksessuary1/?PAGEN_1=2"]')    # тут можно обращаться к любой странице в пагинации, заменив последнюю цсфру
    BUTTON_ZAGRUZIT_ESHE = (By.CSS_SELECTOR, '.bottom_nav_wrapper.nav-compact .more_text_ajax.btn.btn-transparent.has-ripple')


    #    4. Переход в карточку товара:
    BUTTON_ADD_IZBRANNOE = {By.CSS_SELECTOR, '.image-list .item-action.item-action--vertical.item-action--favorite [data-id="3693"]'}
    BUTTON_SRAVNIT = (By.CSS_SELECTOR, '.item-action.item-action--vertical.item-action--compare [data-id="3693"]')
    BUTTON_BYSTR_PROSMOTR = (By.CSS_SELECTOR, '.btn-fast-view.rounded-x.hide-600 .btn.btn-xs.btn-default.has-ripple')
    BUTTON_ADD_IN_BASKET = (By.CSS_SELECTOR, '.buy_block.btn-actions__inner [data-id="3693"]')
    PEREHOD_V_KARTOCHKU_TOVARA = (By.CSS_SELECTOR, '.catalog-block__info-inner [href="/catalog/aksessuary1/dlya-palatok/vvertyshi-dlya-palatki/?oid=4032"]')

    #    5. Локаторы карточки товара:
    NAME_KARTOCHKI = (By.CSS_SELECTOR, '.catalog-detail__main .font_32.switcher-title.js-popup-title.font_20--to-600')


    #    Методы ДО перехода в раздел "Аксессуары":
    @allure.step('Открываю главную страницу + Клик по кнопке "Каталог"')
    def open_catalog_menu(self):    # 1. Метод раскрытия каталога с категориями товаров
        self.driver.get(settings.base_url)
        self.click(self.CATALOG_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CATEGORY_ACCESSORIES))
        return self

    @allure.step('Кликаю по разделу "Аксессуары"')
    def go_to_sale_category(self):    # 2. Метод клика по разделу "Распродажа" в каталоге
        self.find(self.CATEGORY_ACCESSORIES).click()
        WebDriverWait(self.driver, 10).until(EC.url_changes(settings.base_url))
        return self


    #    Методы страницы "Аксессуары":
    @allure.step('Ищу на странице заголовок "Аксессуары"')
    def get_title(self) -> str:  # 3) Метод получения заголовка на странице
        return self.get_text(self.TITLE_PAGE)

    @allure.step('Ищу на странице блок с количеством товаров')
    def get_product_count(self) -> bool:  # 4) Метод получения количества товаров на странице  // тут походу стрингу надо, т.к. там "N товаров" UPD: этот метод вообще не нужно усложнять считанием, т.к. в ХТМЛе строка обычная, а не просто кол-во
        return self.is_visible(self.COUNT_TOVAROV)

    @allure.step('Ищу на странице хлебные крошки')
    def is_breadcrumbs_visible(self) -> bool:  # 5) Метод проверки того, что на странице есть элемент "Хлебные крошки"
        return self.is_visible(self.KROSHKI)  # Использую метод is_visible из BasePage, который возвращает True/False без падения

    @allure.step('Ищу на странице сортировку по: алфавиту, цене, популярности')
    def is_sort_1_visible(self) -> bool:  # 6) Метод проверки того, что на странице есть элемент "Сортировка" ()
        return self.is_visible(self.SORT_1)  # Использую метод is_visible из BasePage, который возвращает True/False без падения

    @allure.step("Кликаю на сортировку")
    def click_on_sort_button(self):
        self.find(self.SORT_1).click()
        return self

    @allure.step("Выбор новой сортировки по алфавиту")
    def click_sort_alphabet(self):
        self.find(self.SORT_ALPHABET).click()
        return self

    @allure.step('Ищу на странице сортировку по: алфавиту, цене, популярности')
    def is_new_sort(self) -> str:  # 6) Метод проверки того, что после применения сортировки отображается "По алфавиту"
        return self.get_text(self.SORT_1)

    @allure.step('Ищу на странице меню фильтров')
    def is_filtres_visible(self) -> bool:  # 8) Метод проверки того, что на странице есть элемент/блок "Фильтры"
        return self.is_visible(self.FILTERS_MENU)  # Использую метод is_visible из BasePage, который возвращает True/False без падения

    @allure.step('Ищу поле с минимальной ценой + Ввожу в неё минимальную стоимость')
    def search_and_input_min_price(self):
        self.find(self.FILTERS_MIN_PRICE).send_keys("7000")  # УБРАТЬ ХАРДКОД (возможно, фэйкером данные генерить)
        return self

    @allure.step('Ищу поле с максимальной ценой + Ввожу в неё максимальную стоимость')
    def search_and_input_max_price(self):
        self.find(self.FILTERS_MAX_PRICE).send_keys("1000")  # УБРАТЬ ХАРДКОД (возможно, фэйкером данные генерить)
        return self

    @allure.step('Ищу на странице сообщение об отсутствии результатов')
    def get_message_bez_resultatov(self) -> str:
        return self.get_text(self.MESSAGE_BEZ_RESULTATOV)

    @allure.step('Ищу на странице сортировку по: количеству карточек на странице')
    def is_sort_2_visible(self) -> bool:  # 7) Метод проверки того, что на странице есть элемент "Сортировка" ()
        return self.is_visible(self.SORT_2)  # Использую метод is_visible из BasePage, который возвращает True/False без падения

    @allure.step('Клик по названию карточки (переход внутрь)')
    def click_first_product(self):
        self.find(self.PEREHOD_V_KARTOCHKU_TOVARA).click()
        return self

    #    Методы страницы карточки товара:
    @allure.step('Ищу на странице карточки её название')
    def get_title_card(self) -> str:
        return self.get_text(self.NAME_KARTOCHKI)
