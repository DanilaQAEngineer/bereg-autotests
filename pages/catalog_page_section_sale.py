from selenium.webdriver.common.by import By
import allure


from config.settings import settings
from pages.base_page import BasePage


@allure.description("добавить описание страницы")
class SectionSaleInCatalogPage(BasePage):
    """Раздел "Распродажа" в меню каталога"""


    #    Локаторы
    CATALOG_BUTTON = (By.XPATH, '(//*[@class="header-menu__link--only-catalog fill-use-fff btn btn-default btn--no-rippple btn-lg"])[1]')
    CATEGORY_SALE = (By.XPATH, '(//*[@class="font_16 font_weight--500 dark_link switcher-title header-menu__wide-child-link fill-theme-hover"])[12]')
    TITLE_PAGE = (By.CSS_SELECTOR, '.topic .switcher-title')
    COUNT_TOVAROV = (By.CSS_SELECTOR, '.topic .element-count-wrapper')
    KROSHKI = (By.CSS_SELECTOR, '.cowl .breadcrumbs.swipeignore')
    SORT_1 = (By.CSS_SELECTOR, '.line-block__item .dropdown-select__title.font_14.font_large.fill-dark-light.bordered.rounded-x.shadow-hovered.shadow-no-border-hovered')
    SORT_2 = (By.CSS_SELECTOR, '.filter-panel__part-right .toggle-panel.hide-600')
    FILTRES = (By.CSS_SELECTOR, '.left_block.visible-by-block-presence .sticky-block.sticky-block--show-N')

    #    Методы
    @allure.step('Открываю главную страницу + Клик по кнопке "Каталог"')
    def open_catalog_menu(self):    # 1. Метод раскрытия каталога с категориями товаров
        self.driver.get(settings.base_url)
        self.click(self.CATALOG_BUTTON)
        return self

    @allure.step('Кликаю по разделу "Распродажа"')
    def go_to_sale_category(self):    # 2. Метод клика по разделу "Распродажа" в каталоге
        self.click(self.CATEGORY_SALE)
        return self

    @allure.step('Ищу на странице заголовок "Распродажа"')
    def get_title(self) -> str:    # 3) Метод получения заголовка на странице
        return self.get_text(self.TITLE_PAGE)

    @allure.step('Ищу на странице блок с количеством товаров')
    def get_product_count(self) -> bool:    # 4) Метод получения количества товаров на странице  // тут походу стрингу надо, т.к. там "N товаров" UPD: этот метод вообще не нужно усложнять считанием, т.к. в ХТМЛе строка обычная, а не просто кол-во
        return self.is_visible(self.COUNT_TOVAROV)

    @allure.step('Ищу на странице хлебные крошки')
    def is_breadcrumbs_visible(self) -> bool:    # 5) Метод проверки того, что на странице есть элемент "Хлебные крошки"
        return self.is_visible(self.KROSHKI)    # Использую метод is_visible из BasePage, который возвращает True/False без падения

    @allure.step('Ищу на странице сортировку по: алфавиту, цене, популярности')
    def is_sort_1_visible(self) -> bool:    # 6) Метод проверки того, что на странице есть элемент "Сортировка" ()
        return self.is_visible(self.SORT_1)    # Использую метод is_visible из BasePage, который возвращает True/False без падения

    @allure.step('Ищу на странице сортировку по: количеству карточек на странице')
    def is_sort_2_visible(self) -> bool:    # 7) Метод проверки того, что на странице есть элемент "Сортировка" ()
        return self.is_visible(self.SORT_2)    # Использую метод is_visible из BasePage, который возвращает True/False без падения

    @allure.step('Ищу на странице меню фильтров')
    def is_filtres_visible(self) -> bool:    # 8) Метод проверки того, что на странице есть элемент "Хлебные крошки"
        return self.is_visible(self.FILTRES)    # Использую метод is_visible из BasePage, который возвращает True/False без падения
