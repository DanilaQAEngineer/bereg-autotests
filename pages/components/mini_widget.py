import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage
from locators.components.widgets_locators import LocatorsForWidgets


class MiniWidgetComponent(BasePage):
    """ Универсальный компонент для выпадающих виджетов в шапке: принимает локаторы (иконка, дропдаун, карточка, кнопка удаления). """

    def __init__(self, driver, icon_locator, dropdown_locator, item_locator, remove_locator):
        super().__init__(driver)
        self.icon = icon_locator
        self.dropdown = dropdown_locator
        self.item = item_locator
        self.remove = remove_locator

    @allure.step('Метод наведения курсора на иконку виджета')
    def hover_icon(self):
        #    Selenium не имеет встроенного hover, поэтому для наведения курсора на иконку виджета (чтоб появилась выпадашка) используем ActionChains
        element = self.find(self.icon)
        ActionChains(self.driver).move_to_element(element).perform()
        #    Жду, когда выпадающий список реально появится в DOM
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dropdown))
        return self

    ### Добавить метод, который бы чекал количество добавленных товаров (в иконке в правом верхнем углу)

