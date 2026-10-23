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

    # МЕТОД ПРОВЕРКИ СОРТИРОВКИ ПО ЦЕНЕ (ОТ БОЛЬШЕЙ К МЕНЬШЕЙ)
    @allure.step("Проверяю, действительно ли карточки на странице отображаются от самой дорогой, к самой дешёвой")
    def get_all_prices_as_floats(self) -> list[float]:    # Метод-парсер для сбора цен на странице, который переводит данные из строк в числа с плавающей точкой: -> list[float] говорит, что функция вернёт список чисел с плавающей точкой (например, [15000.0, 12000.5, 8000.0])
        """ Собираем актуальные цены со страницы и возвращает список чисел """
        # Ждем, пока цены отрисуются после сортировки (можно добавить явное ожидание, если нужно)
        elements = self.find_all(LocatorsForCatalogPageSectionAccessories.ACTUAL_PRICE_IN_CARD)    # Собираю ВСЕ элементы с ценами на странице раздела (в HTML`е это локатор ACTUAL_PRICE_IN_CARD, который смотрит на цену в карточке)
        prices = []    # Создал пустой список, куда буду складываться результаты для дальнейшего их сравнения (что меньше, что больше)
        for el in elements:    # Создал цикл "for" (перебора эементов переменной "elements"): запускаю цикл, где el — это каждая отдельная «коробочка/элемент» с ценой по очереди
            text = el.text.replace(',', '.')    # Меняю запятые на точку: el.text вытаскивает видимый текст (например, "15 999,50") + Метод .replace(',', '.') меняет запятую на точку,
                                                # т.к. в Python дробные числа пишутся через точку и если попытаться превратить строку "15,5" в число через float(), Python упадёт с ошибкой. На сайтах в РФ цены часто пишут через запятую
            clean_text = re.sub(r'[^\d.]', '', text)    # Очистка регулярным выражением (Regex): функция re.sub (из модуля re) берет строку и удаляет из неё всё, что не является цифрой или точкой (пустота/пробел, буквы):
                                                                     # [^\d.] — это правило, говорящее: «Найди любой символ, который НЕ (^) является цифрой (\d) и НЕ является точкой (. )», а '' — на что заменить найденное (на пустоту)
                                                                     # Зачем: Сайт отдаёт цену в ужасном виде: "15 999.50 ₽" (с пробелами и знаком рубля). Если мы попытаемся сделать float("15 999.50 ₽"), Python упадёт.
                                                                     # После работы re.sub от строки останется только "15999.50" — чистое число, готовое к конвертации
            if clean_text:    # Создаю условие "Защита от пустых строк": проверяю, что строка не пустая
                              # К примеру, на карточке вместо цены написано "Цена по запросу". В таком случае регулярка удалит все буквы, и останется лишь пустая строка "". И если мы попытаемся сделать float(""), код упадёт
                              # Эта проверка как раз защищает от таких ситуаций
                prices.append(float(clean_text))    # Конвертация и добавление в список: тут мы преобразуем строку "15999.50" в число 15999.5 и добавляем его в переменную/список "prices"
                                                    # Теперь у нас есть список чисел, с которыми умеет работать математика
        return prices    # Возврат результата: итог метода -- отдаём готовый список полученных со страницы чисел/ценников в карточках, например: [15999.5, 12500.0, 8000.0]

    @allure.step('Ищу на странице кнопку_дропдаун сортировки по: алфавиту, цене, популярности + Проверяю её значение')
    def get_sort_value(self) -> str:  # 6) Метод проверки того, что после применения сортировки отображается "По алфавиту"
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

    @allure.step("Кликаю на раскладку странице 'Строчный вывод'")
    def click_on_view_by_line(self):
        self.find(LocatorsForCatalogPageSectionAccessories.VIEW_MODE_LINE).click()
        return self

    @allure.step('Клик по названию карточки (переход внутрь)')
    def click_first_product(self):
        self.find(LocatorsForCatalogPageSectionAccessories.PEREHOD_V_KARTOCHKU_TOVARA).click()
        return self

    #    Методы страницы карточки товара:
    @allure.step('Ищу на странице карточки её название')
    def get_title_card(self) -> str:
        return self.get_text(LocatorsForCatalogPageSectionAccessories.NAME_CARD)
