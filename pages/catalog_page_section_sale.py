from selenium.webdriver.common.by import By


from config.settings import settings
from pages.base_page import BasePage


class SectionSaleInCatalogPage(BasePage):
    """Раздел "Распродажа" в меню каталога"""


    # Локаторы
    CATALOG_BUTTON = (By.XPATH, '(//*[@class="header-menu__link--only-catalog fill-use-fff btn btn-default btn--no-rippple btn-lg"])[1]')
    CATEGORY_SALE = (By.XPATH, '(//*[@class="font_16 font_weight--500 dark_link switcher-title header-menu__wide-child-link fill-theme-hover"])[12]')
    TITLE_PAGE = (By.CSS_SELECTOR, '.topic .switcher-title')
    COUNT_TOVAROV = (By.CSS_SELECTOR, '.topic .element-count-wrapper')


    def open_catalog_menu(self):    # 1) Метод раскрытия каталога с категориями товаров
        self.driver.get(settings.base_url)    # Открываю главную страницу
        self.click(self.CATALOG_BUTTON)    # Кликаю по кнопке "Каталог"
        return self

    def go_to_sale_category(self):    # 2) Метод клика по разделу "Распродажа" в каталоге
        self.click(self.CATEGORY_SALE)    # Кликаю по разделу "Распродажа"
        return self

    def get_title(self) -> str:    # 3) Метод получения заголовка на странице
        return self.get_text(self.TITLE_PAGE)

    def get_product_count(self) -> int:    # 4) Метод получения количества товаров на странице  // тут походу стрингу надо, т.к. там "N товаров" UPD: этот метод вообще не нужно усложнять считанием, т.к. в ХТМЛе строка обычная, а не просто кол-во
        return len(self.find_all(self.COUNT_TOVAROV))
