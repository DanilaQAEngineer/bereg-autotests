import re
import allure
from selenium.webdriver.support.ui import WebDriverWait


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
        # #    Запоминаем цену первой карточки ДО сортировки
        # first_price_before = self.find_all(LocatorsForListing.PRICE_NEW)[0].text

        self.click(LocatorsForListing.ASC_SORT_PRICE)
        # #    ЖДЕМ, пока первая цена не изменится (значит, сайт перестроил список)\
        # WebDriverWait(self.driver, 10).until(
        #     lambda d: self.find_all(LocatorsForListing.PRICE_NEW)[0].text != first_price_before
        # )
        return self


    @allure.step('Метод клика по параметру "Сначала дорогие" в выпадающем списке_дропдауне сортировки на странице каталога')
    def select_desc_sort_price(self):
        # #    Запоминаем цену первой карточки ДО сортировки
        # first_price_before = self.find_all(LocatorsForListing.PRICE_NEW)[0].text

        self.click(LocatorsForListing.DESC_SORT_PRICE)
        # #    ЖДЕМ, пока первая цена не изменится (значит, сайт перестроил список)\
        # WebDriverWait(self.driver, 10).until(
        #     lambda d: self.find_all(LocatorsForListing.PRICE_NEW)[0].text != first_price_before
        # )
        return self

    @allure.step('Метод сбора цен на странице')    # Старый метод, который будет падать, если на странице есть зачёркнутые цены
    def get_all_prices_as_floats(self) -> list[float]:
        elements = self.find_all(LocatorsForListing.PRICE_NEW)
        prices = []
        for el in elements:
            text = el.text.replace(',', '.')
            clean_text = re.sub(r'[^\d.]', '', text)
            if clean_text:
                prices.append(float(clean_text))
        return prices

    # @allure.step('Метод сбора цен на странице раздела каталога')  # Новый метод, который будет падать, если на странице есть зачёркнутые цены
    # def get_all_prices_as_floats(self) -> list[float]:
    #     #    1. Сперва ищем на странице сами карточки товаров (Получаем список ВСЕХ карточек на странице (это список)):
    #     all_cards = self.find_all(LocatorsForListing.PRODUCT_CARDS)
    #     prices = []
    #
    #     #    2. Проходимся циклом по каждой карточке
    #     for card in all_cards:
    #         #    3. Внутри КАЖДОЙ карточки ищем старую цену
    #         old_prices = card.find_elements(*LocatorsForListing.PRICE_OLD)
    #
    #         if old_prices:    # Если старая цена (зачеркнутая) есть
    #             price_text = old_prices[0].text    # то, берем её текст
    #         else:    # Если же скидки нет
    #             new_prices = card.find_elements(*LocatorsForListing.PRICE_NEW)    # то, берем обычную_новую цену
    #             if new_prices:
    #                 price_text = new_prices[0].text
    #             else:
    #                 continue    # Если цен вообще нет - пропускаем
    #
    #         #     4. Очищаем от мусора (пробелы, знаки рубля) и переводим в тип "float"
    #         text = price_text.replace(',', '.')
    #         clean_text = re.sub(r'[^\d.]', '', text)
    #         if clean_text:
    #             prices.append(float(clean_text))
    #
    #     return prices

    #   2) Методы для тестирования сортировки на странице с результатами поиска по сайту:
    @allure.step('Метод клика по кнопке_дропдауну "Сортировка" на странице с результатами поиска по сайту')
    def click_sort_button_on_result_search_page(self):
        self.click(LocatorsForListing.SORT_DROPDOWN_ON_RESULT_SEARCH_PAGE)
        return self

    #   2) Методы для тестирования сортировки на странице с результатами поиска по сайту:
    @allure.step('Метод клика по кнопке_дропдауну "Сортировка" на странице с результатами поиска по сайту')
    def click_sort_button_on_result_search_page(self):
        self.click(LocatorsForListing.SORT_DROPDOWN_ON_RESULT_SEARCH_PAGE)
        return self