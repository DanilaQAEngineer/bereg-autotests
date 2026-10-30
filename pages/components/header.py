import allure
from selenium.webdriver.common.action_chains import ActionChains



from pages.base_page import BasePage
from locators.components.header_locators import LocatorsForHeader


class HeaderComponents(BasePage):
    """Компонент шапки сайта. Доступен на любой странице."""

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

    @allure.step('Метод ввода данных в поисковую строку в хедере: {query}')
    def search_for(self, query: str):
        self.type(LocatorsForHeader.SEARCH_INPUT, query)
        self.click(LocatorsForHeader.SEARCH_BUTTON)
        return self
