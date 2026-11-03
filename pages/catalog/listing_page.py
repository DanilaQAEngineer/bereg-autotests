import allure


from config.settings import settings
from pages.base_page import BasePage
from pages.components.sort_panel import SortPanelComponent
from pages.components.product_card import ProductCardComponent
from pages.components.filter_panel import FilterPanelComponent
from locators.catalog.listing_locators import LocatorsForListing


class ListingPage(BasePage):
    """ Универсальная страница листинга (страница раздела "Аксессуары, Палатки" и т.д.) """

    def __init__(self, driver):
        super().__init__(driver)
        #     Внедряю повторяющиеся компоненты:
        self.sort_panel = SortPanelComponent(driver)
        self.product_card = ProductCardComponent(driver)
        self.filter_panel = FilterPanelComponent(driver)

    @allure.step('Метод открытия какой-нибудь дефолтной страницы раздела, на которой есть сортировка, фильтры и карточки товара: {category_url}')
    def open_page_category_with_sorting_filters(self, category_url: str = '/catalog/aksessuary1/dlya-palatok/'):
        self.driver.get(f'{settings.base_url}{category_url}')
        return self

    @allure.step('Метод получения количества карточек на странице раздела')
    def get_product_count(self) -> int:
        return len(self.find_all(LocatorsForListing.PRODUCT_CARDS))

    @allure.step('Метод перехода на страницу поиска с нужным запросом_результатами (имитирую переход по ссылке: ввёл запрос в поиск + нажал "Найти/Все результаты")')
    def open_search_results_page(self, query: str = "Палатка"):
        self.driver.get(f'{settings.base_url}/catalog/?q={query}')
        return self
