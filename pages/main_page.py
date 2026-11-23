import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class MainrPage(BasePage):
    """ Методы для главной страницы сайта """

    # ==================================================================================================================
    # === НАВИГАЦИЯ ===
    # ==================================================================================================================
    @allure.step('Универсальный метод очистки поля')
    def clear_field(self, locator):
        """ Универсальный метод удаления значений из полей """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.find(locator).clear()
        return self

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
    def enter_text(self, locator, value: str) -> "RegisterPage":
        """ Универсальный метод ввода данных в любое текстовое поле """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.type(locator, value)
        return self

    # ==================================================================================================================
    # === ПРОВЕРКИ ===
    # ==================================================================================================================
    @allure.step('Универсальный метод получения текста')
    def check_text(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.get_text(locator)

