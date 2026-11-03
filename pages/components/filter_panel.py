import allure


from pages.base_page import BasePage
from config.settings import settings
from locators.catalog.filter_locators import LocatorsForFilters

class FilterPanelComponent(BasePage):
    """Компонент работы с фильтрами в листинге"""

    @allure.step('Метод открытия какой-нибудь дефолтной страницы раздела, на которой есть фильтры и карточки товара: {category_url}')
    def open_page_category_with_filters(self, category_url: str = '/catalog/aksessuary1/dlya-palatok/'):
        self.driver.get(f'{settings.base_url}{category_url}')
        return self

    @allure.step('Метод ввода минимальной цены в поле "Цена"')
    def enter_minimal_price(self, price: str):
        self.type(LocatorsForFilters.INPUT_MIN_PRICE, price)
        return self

    @allure.step('Метод ввода максимальной цены в поле "Цена"')
    def enter_maximal_price(self, price: str):
        self.type(LocatorsForFilters.INPUT_MAX_PRICE, price)
        return self

    @allure.step('Метод клика по чекбоксу "Наши предложения: Советуем"')
    def click_checkbox_recomendate(self):
        self.click(LocatorsForFilters.CHECKBOX_RECOMENDATE)
        return self

    @allure.step('Метод клика по чекбоксу "Наши предложения: Новинка"')
    def click_checkbox_new(self):
        self.click(LocatorsForFilters.CHECKBOX_NEW)
        return self

    @allure.step('Метод клика по кнопке "Сбросить" (очистка фильтров)')
    def click_reset_button(self):
        self.click(LocatorsForFilters.RESET_BUTTON)
        return self
