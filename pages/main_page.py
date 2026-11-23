import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from locators.main_page_locators import LocatorsForMainPage


class MainPage(BasePage):
    """ Методы для главной страницы сайта """

    # ==================================================================================================================
    # === НАВИГАЦИЯ ===
    # ==================================================================================================================
    @allure.step('Универсальный метод клика')
    def click_element(self, locator):
        """ Универсальный метод лика по чему-либо на странице """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.find(locator).click()
        return self
    # @allure.step('Универсальный метод клика (JS)')
    # def click_element(self, locator):
    #     """Универсальный метод клика. Используем JS-клик, чтобы обойти перекрытия (оверлеи)"""
    #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
    #     element = self.find(locator)
    #     self.driver.execute_script("arguments[0].click();", element)
    #     return self

    # ==================================================================================================================
    # === ПРОВЕРКИ ===
    # ==================================================================================================================
    @allure.step("Метод получения ссылки (href) активного баннера")
    def get_active_banner_link(self, locator) -> str:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        #    Находим активный слайд
        active_slide = self.find(locator)
        #    Ищем внутри него ссылку <a> и берем атрибут href
        link_element = active_slide.find_element(By.TAG_NAME, 'a')
        return link_element.get_attribute('href')

    @allure.step("Метод получения тэгов карточек в блоке Бестселлеры")
    def get_bestseller_tags(self, locator) -> list[str]:
        # Находим все тэги
        cards = self.find_all(locator)
        # Собираем из них текст названий (или ссылок)
        return [card.text for card in cards]

    @allure.step('Универсальный метод получения текста')
    def check_text(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.get_text(locator)

