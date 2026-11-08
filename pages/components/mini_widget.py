import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage
from locators.components.widgets_locators import LocatorsForWidgets


class MiniWidgetComponent(BasePage):
    """ Универсальный компонент для выпадающих виджетов в шапке: принимает локаторы (иконка, дропдаун, карточка, кнопка удаления). """

    def __init__(self, driver, count, widget, dropdown, first_card, title_card, remove_btn, btn_in_widget):
        super().__init__(driver)
        self.count = count  # Локатор иконки с количеством добавленных товаров
        self.widget = widget    # Локатор виджета раздела "В сравнение/избранное/корзину"
        self.dropdown = dropdown    # Локатор выпадающего списка добавленных товаров
        self.first_card = first_card     # Локатор карточки товара внутри выпадающего списка
        self.title = title_card    # Локатор названия карточки добавленного товара (по клику мы переходим на страницу карточки этого товара)
        self.remove_btn = remove_btn     # Локатор кнопки "Удалить товар из выпадающего списка"
        self.btn_in_widget = btn_in_widget     # Локатор кнопки "В сравнение/избранное/корзину" (переход в раздел)

    ### Добавить метод, который бы чекал количество добавленных товаров (в иконке в правом верхнем углу)
    @allure.step('Метод проверки_получения количества товаров в иконке над виджетом')
    def check_count_in_widget(self) -> str:    # возможно, понадобится int, а не строка
        return self.get_text(self.count)

    @allure.step('Метод наведения курсора на иконку виджета')
    def hover_icon(self):
        #    Selenium не имеет встроенного hover, поэтому для наведения курсора на иконку виджета (чтоб появилась выпадашка) используем ActionChains
        element = self.find(self.widget)    # можно на "count" заменить
        ActionChains(self.driver).move_to_element(element).perform()
        #    Жду, когда выпадающий список реально появится в DOM
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dropdown))    # раскомментить
        return self

    @allure.step('Метод проверки наличия выпадающего меню после наведения курсора на виджет')
    def check_dropdown(self) -> bool:
        return self.is_visible(self.dropdown)

    @allure.step('Метод проверки наличия товаров в выпадающем меню')
    def check_card_in_widget(self) -> bool:
        return self.is_visible(self.first_card )

    @allure.step('Метод клика по названию товара в выпадающем списке (переход на страницу карточки товара)')
    def click_title_card_in_dropdown(self):
        self.click(self.title)
        return self

    @allure.step('Метод удаления первого товара в выпадающем меню')
    def click_remove_button_in_dropdown(self):
        self.click(self.remove_btn)
        return self

    @allure.step('Метод клика кнопки "В сравнение/избранное/корзину"')
    def click_inside_button_in_dropdown(self):
        self.click(self.btn_in_widget)
        return self
