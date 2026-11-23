import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from pages.base_page import BasePage


class FooterPage(BasePage):
    """ Методы для футер-меню """

    # ==================================================================================================================
    # === НАВИГАЦИЯ ===
    # ==================================================================================================================
    # @allure.step('Универсальный метод клика')
    # def click_element(self, locator):
    #     """ Универсальный метод лика по чему-либо на странице """
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #     self.find(locator).click()
    #     return self
    @allure.step('Универсальный метод клика (JS)')
    def click_element(self, locator):
        """Универсальный метод клика. Используем JS-клик, чтобы обойти перекрытия (оверлеи)"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)
        return self

    @allure.step('Ввод текста "{value}" в поле {locator}')
    def enter_text(self, locator, value: str) -> "FooterPage":
        """ Универсальный метод ввода данных в любое текстовое поле """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.type(locator, value)
        return self

    # ==================================================================================================================
    # === ПРОВЕРКИ ===
    # ==================================================================================================================
    @allure.step('Универсальный метод проверки_наличия_отображения элемента на странице')
    def is_visible_element(self, locator) -> bool:
        """ Универсальная проверка появления элемента на странице """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.is_visible(locator)

    @allure.step('Ожидание исчезновения элемента {locator}')
    def wait_until_invisible(self, locator, timeout=10) -> bool:
        """ Универсальная проверка исчезновения элемента со страницы """
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return True

    @allure.step('Универсальный метод получения текста')
    def check_text(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.get_text(locator)

    @allure.step('Универсальный метод проверки наличия значения в инпут-полях (в полях есть данные?)')
    def is_field_filled(self, locator) -> bool:
        """ Универсальная проверка любого input-поля на наличие значения """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))  # Закомментить, если всё равно по таймауту валиться будут
        element = self.find(locator)
        value = element.get_attribute('value')
        return bool(value and value.strip())

    @allure.step('Универсальная проверка состояния Универсальная проверка чекбокса (флажок в чекбоксе выставлен?)')
    def is_checkbox_checked(self, locator) -> bool:
        """ Универсальная проверка любого чекбокса, что он отмечен """
        # Ищем элемент напрямую, без ожидания видимости (чекбоксы часто скрыты)
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))  # Закомментить, если всё равно по таймауту валиться будут
        element = self.driver.find_element(*locator)
        return element.is_selected()

    @allure.step('Метод проверки_получения_отображения ошибки под полями')
    def check_errors(self, locator) -> str:
        """ Универсальная проверка ошибок под полями """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.get_text(locator)
