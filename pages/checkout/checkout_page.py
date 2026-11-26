import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time # Добавляем для микро-паузы анимации карусели

from pages.base_page import BasePage
from locators.main_page_locators import LocatorsForMainPage


class CheckoutPage(BasePage):
    """ Методы для страницы оформления заказа (после корзины) """

    # ==================================================================================================================
    # === ДЕЙСТВИЯ ===
    # ==================================================================================================================
    @allure.step('Метод клика по элементу {locator} (через JS)')
    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element = self.find(locator)
        # Клик через JS, чтобы игнорировать перекрытия (попапы, баннеры)
        self.driver.execute_script("arguments[0].click();", element)
        return self

    @allure.step('Клик по табу и ожидание его активации')
    def click_tab_and_wait(self, tab_locator):
        """Кликает по табу и ждёт, пока у него появится класс 'active'."""
        self.click_element(tab_locator)
        WebDriverWait(self.driver, 5).until(
            lambda d: 'active' in d.find_element(*tab_locator).get_attribute('class')
        )
        return self

    @allure.step('Клик по радиокнопке и ожидание её активации')
    def click_radio_and_wait(self, radio_locator):
        """Кликает по радиокнопке и ждёт, пока она станет выбранной."""
        self.click_element(radio_locator)
        WebDriverWait(self.driver, 5).until(
            lambda d: d.find_element(*radio_locator).is_selected()
        )
        return self

    @allure.step('Ввод текста "{value}" в поле {locator}')
    def enter_text(self, locator, value: str) -> "CheckoutPage":
        """ Универсальный метод ввода данных в любое текстовое поле """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.type(locator, value)
        return self

    @allure.step('Универсальный метод очистки поля')
    def clear_field(self, locator):
        """ Универсальный метод удаления значений из полей """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.find(locator).clear()
        return self

    # ==================================================================================================================
    # === ПРОВЕРКИ ===
    # ==================================================================================================================
    @allure.step('Метод ожидания видимости элемента {locator}')
    def wait_visible_element(self, locator, timeout=10):
        """
        Ждет, пока элемент станет видимым на странице
        (метод нужен для того, чтобы искать какой-то элемент перед действием (замена таймслипов))
        """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self

    @allure.step('Универсальный метод проверки_наличия_отображения элемента на странице')
    def is_visible_element(self, locator) -> bool:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.is_visible(locator)

    @allure.step('Универсальный метод получения текста')
    def check_text(self, locator) -> str:
        """ Для проверки заголовков или ошибок под полями """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.get_text(locator)

    @allure.step('Универсальный метод проверки наличия значения в инпут-полях (в полях есть данные?)')
    def is_field_filled(self, locator) -> bool:
        """ Универсальная проверка любого input-поля на наличие значения """
        element = self.find(locator)
        value = element.get_attribute('value')
        return bool(value and value.strip())

    @allure.step('Универсальная проверка состояния Универсальная проверка чекбокса (флажок в чекбоксе выставлен?)')
    def is_checkbox_checked(self, locator) -> bool:
        """ Универсальная проверка любого чекбокса, что он отмечен """
        # Ищем элемент напрямую, без ожидания видимости (чекбоксы часто скрыты)
        element = self.driver.find_element(*locator)
        return element.is_selected()
