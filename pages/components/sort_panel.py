import re
import allure


from pages.base_page import BasePage
from locators.catalog.listing_locators import LocatorsForListing


class SortPanelComponent(BasePage):
    """Компонент сортировки (универсальный, для всех страниц, где она есть)"""


    #    1) Методы для тестирования сортировки на странице каталога:

    # @allure.step('Метод перехода на любую страницу с сортировкой')
    # def open_main_page(self):
    #     self.open(LocatorsForListing.URL_PAGE_WITH_SORT)
    #     return self

    @allure.step('Метод клика по кнопке_дропдауну "Сортировка" на странице каталога')
    def click_sort_button_on_catalog_page(self):
        self.click(LocatorsForListing.SORT_DROPDOWN)
        return self


    @allure.step('Метод клика по параметру "Сначала дешёвые" в выпадающем списке_дропдауне сортировки')
    def select_asc_sort_price(self):
        self.click(LocatorsForListing.ASC_SORT_PRICE)
        return self


    @allure.step('Метод клика по параметру "Сначала дорогие" в выпадающем списке_дропдауне сортировки на странице каталога')
    def select_desc_sort_price(self):
        self.click(LocatorsForListing.DESC_SORT_PRICE)
        return self

    @allure.step('Метод сбора цен на странице раздела каталога')
    def get_all_prices_as_floats(self) -> list[float]:
        elements = self.find_all(LocatorsForListing.PRICE_ELEMENTS)
        prices = []
        for el in elements:
            text = el.text.replace(',', '.')
            clean_text = re.sub(r'[^\d.]', '', text)
            if clean_text:
                prices.append(float(clean_text))
        return prices

    #   2) Методы для тестирования сортировки на странице с результатами поиска по сайту:
    @allure.step('Метод клика по кнопке_дропдауну "Сортировка" на странице с результатами поиска по сайту')
    def click_sort_button_on_result_search_page(self):
        self.click(LocatorsForListing.SORT_DROPDOWN_ON_RESULT_SEARCH_PAGE)
        return self
