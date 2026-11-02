import allure
from selenium.webdriver.common.action_chains import ActionChains


from pages.base_page import BasePage
from locators.components.header_locators import LocatorsForHeader


class HeaderComponents(BasePage):
    """Компонент шапки сайта. Доступен на любой странице."""

    @allure.step('Метод перехода на главную страницу')
    def open_main_page(self):
        self.open(LocatorsForHeader.BASE_PAGE)
        return self

    @allure.step('Метод клика по лого в хедере')
    def click_logo(self):
        self.click(LocatorsForHeader.LOGO)
        return self

    @allure.step('Метод клика по кнопке выбора города + Открытия модалки выбора города')
    def open_city_modal(self):
        self.click(LocatorsForHeader.CITY_BUTTON)
        # Жду появления модалки выбора города
        self.find(LocatorsForHeader.CITY_MODAL)
        return self

    @allure.step('Метод открытия выпадающего меню "Номер телефона" в хедере')
    def hover_phone(self):
        # Selenium не имеет встроенного hover, поэтому используем ActionChains
        element = self.find(LocatorsForHeader.PHONE_ICON)
        ActionChains(self.driver).move_to_element(element).perform()
        return self

    @allure.step('Метод проверки наличия кнопки в выпадающем меню "Номер телефона"')
    def is_call_request_visible(self) -> bool:
        return self.is_visible(LocatorsForHeader.CALL_REQUEST_BUTTON)

    #    Методы работы с поиском в хедере:
    @allure.step('Метод ввода запроса в поисковую строку в хедере: {query}')
    def search_input(self, query: str):
        self.type(LocatorsForHeader.SEARCH_INPUT, query)
        # Жду пока JS сайта отрисует выпадашку с результатами поиска
        self.find(LocatorsForHeader.SEARCH_DROPDOWN)
        return self

    @allure.step('Метод проверки появления выпадающего списка с результатами поиска')
    def is_search_dropdown_result_visible(self) -> bool:
        return self.is_visible(LocatorsForHeader.SEARCH_DROPDOWN)

    @allure.step('Метод проверки наличия карточек в результирующем списке (в выпадашке)')
    def get_search_results_count(self) -> int:
        """Возвращает количество найденных элементов в выпадашке"""
        # 1) Ждем, когда хотя бы один элемент появится в списке (на случай долгой загрузки)
        self.find(LocatorsForHeader.SEARCH_RESULT_ITEMS)
        # 2) Возвращаем длину списка
        return len(self.find_all(LocatorsForHeader.SEARCH_RESULT_ITEMS))

    @allure.step('Метод проверки значения в поисковой строке (что она не пустая)')
    def get_search_input_value(self) -> str:
        return self.find(LocatorsForHeader.SEARCH_INPUT).get_attribute("value")

    @allure.step('Метод клика по кнопке поиска (лупа)')
    def click_button_search(self):
        self.click(LocatorsForHeader.SEARCH_BUTTON)
        return self

    @allure.step('Метод клика по кнопке "х" в поисковой строке (удаление запроса из поля поиска)')
    def click_clear_button(self):
        self.click(LocatorsForHeader.SEARCH_CLEAR_BTN)
        return self
