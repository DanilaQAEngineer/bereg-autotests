import re
import allure
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from config.settings import settings
from pages.base_page import BasePage
from locators.locators_for_catalog_page_section_accessories import LocatorsForCatalogPageSectionAccessories


@allure.description("добавить описание страницы")
class SectionAccessoriesInCatalogPage(BasePage):
    """ Методы раздела "Аксессуары" в меню каталога """


    #    Методы ДО перехода в раздел "Аксессуары":
    @allure.step('Перехожу на главную страницу + Клик по кнопке "Каталог"')
    def open_catalog_menu(self):    # 1. Метод раскрытия каталога с категориями товаров
        self.driver.get(settings.base_url)
        self.click(LocatorsForCatalogPageSectionAccessories.CATALOG_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForCatalogPageSectionAccessories.CATEGORY_ACCESSORIES))
        return self

    @allure.step('В каталоге кликаю по разделу "Аксессуары"')
    def go_to_sale_category(self):    # 2. Метод клика по разделу "Распродажа" в каталоге
        self.find(LocatorsForCatalogPageSectionAccessories.CATEGORY_ACCESSORIES).click()
        WebDriverWait(self.driver, 10).until(EC.url_changes(settings.base_url))
        return self


    #    Методы страницы "Аксессуары":
    @allure.step('Ищу на странице раздела заголовок "Аксессуары"')
    def get_title(self) -> str:  # 3) Метод получения заголовка на странице
        return self.get_text(LocatorsForCatalogPageSectionAccessories.TITLE_PAGE)

    @allure.step('Ищу на странице раздела блок с количеством товаров')
    def get_product_count(self) -> bool:  # 4) Метод получения количества товаров на странице  // тут походу стрингу надо, т.к. там "N товаров" UPD: этот метод вообще не нужно усложнять считанием, т.к. в ХТМЛе строка обычная, а не просто кол-во
        return self.is_visible(LocatorsForCatalogPageSectionAccessories.COUNT_TOVAROV)

    @allure.step('Ищу на странице раздела хлебные крошки')
    def is_breadcrumbs_visible(self) -> bool:  # 5) Метод проверки того, что на странице есть элемент "Хлебные крошки"
        return self.is_visible(LocatorsForCatalogPageSectionAccessories.KROSHKI)  # Использую метод is_visible из BasePage, который возвращает True/False без падения

    #    Методы сортировки на странице "Аксессуары":
    @allure.step('Ищу на странице раздела сортировку по: алфавиту, цене, популярности')
    def is_sort_1_visible(self) -> bool:  # 6) Метод проверки того, что на странице есть элемент "Сортировка" ()
        return self.is_visible(LocatorsForCatalogPageSectionAccessories.SORT_DROPDOWN)  # Использую метод is_visible из BasePage, который возвращает True/False без падения

    @allure.step("Кликаю на кнопку_дропдаун сортировки")
    def click_on_sort_button(self):
        self.find(LocatorsForCatalogPageSectionAccessories.SORT_DROPDOWN).click()
        return self

    @allure.step("Выбор новой сортировки: по убыванию цены (DESC-сортировка)")
    def click_desc_sort_by_price(self):
        self.find(LocatorsForCatalogPageSectionAccessories.DESC_SORT_BY_PRICE).click()
        return self

    @allure.step("Проверяю, действительно ли карточки на странице отображаются от самой дорогой, к самой дешёвой")
    def get_all_prices_as_floats(self) -> list[float]:
        """ Собираем актуальные цены со страницы и возвращает список чисел """
        # Ждем, пока цены отрисуются после сортировки (можно добавить явное ожидание, если нужно)
        elements = self.find_all(LocatorsForCatalogPageSectionAccessories.ACTUAL_PRICE_IN_CARD)
        prices = []
        for el in elements:
            # Убираем всё, кроме цифр (пробелы, знаки валют, запятые)
            text = el.text.replace(',', '.')
            clean_text = re.sub(r'[^\d.]', '', text)
            if clean_text:
                prices.append(float(clean_text))
        return prices

    @allure.step('Ищу на странице сортировку по: алфавиту, цене, популярности + Проверяю её новое значение')
    def is_new_sort_value(self) -> str:  # 6) Метод проверки того, что после применения сортировки отображается "По алфавиту"
        return self.get_text(LocatorsForCatalogPageSectionAccessories.SORT_DROPDOWN)

    @allure.step('Ищу на странице меню фильтров')
    def is_filtres_visible(self) -> bool:  # 8) Метод проверки того, что на странице есть элемент/блок "Фильтры"
        return self.is_visible(LocatorsForCatalogPageSectionAccessories.FILTERS_MENU)  # Использую метод is_visible из BasePage, который возвращает True/False без падения

    @allure.step('Ищу поле с минимальной ценой + Ввожу в неё минимальную стоимость')
    def search_and_input_min_price(self):
        self.find(LocatorsForCatalogPageSectionAccessories.FILTERS_MIN_PRICE).send_keys("7000")  # УБРАТЬ ХАРДКОД (возможно, фэйкером данные генерить)
        return self

    @allure.step('Ищу поле с максимальной ценой + Ввожу в неё максимальную стоимость')
    def search_and_input_max_price(self):
        self.find(LocatorsForCatalogPageSectionAccessories.FILTERS_MAX_PRICE).send_keys("1000")  # УБРАТЬ ХАРДКОД (возможно, фэйкером данные генерить)
        return self

    @allure.step('Ищу на странице сообщение об отсутствии результатов')
    def get_message_bez_resultatov(self) -> str:
        return self.get_text(LocatorsForCatalogPageSectionAccessories.MESSAGE_BEZ_RESULTATOV)

    @allure.step('Ищу на странице сортировку по: количеству карточек на странице')
    def is_sort_2_visible(self) -> bool:  # 7) Метод проверки того, что на странице есть элемент "Сортировка" ()
        return self.is_visible(LocatorsForCatalogPageSectionAccessories.SORT_2)  # Использую метод is_visible из BasePage, который возвращает True/False без падения

    @allure.step('Клик по названию карточки (переход внутрь)')
    def click_first_product(self):
        self.find(LocatorsForCatalogPageSectionAccessories.PEREHOD_V_KARTOCHKU_TOVARA).click()
        return self

    #    Методы страницы карточки товара:
    @allure.step('Ищу на странице карточки её название')
    def get_title_card(self) -> str:
        return self.get_text(LocatorsForCatalogPageSectionAccessories.NAME_CARD)
