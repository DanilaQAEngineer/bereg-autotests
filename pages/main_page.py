import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time # Добавляем для микро-паузы анимации карусели

from pages.base_page import BasePage
from locators.main_page_locators import LocatorsForMainPage


class MainPage(BasePage):
    """ Методы для главной страницы сайта """

    # ==================================================================================================================
    # === ДЕЙСТВИЯ ===
    # ==================================================================================================================
    @allure.step('Метод клика по элементу {locator}')
    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.find(locator).click()
        return self

    @allure.step('Метод переключения баннера на следующий слайд')
    def click_next_banner(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsForMainPage.BTN_NEXT_SLIDE))
        self.click_element(LocatorsForMainPage.BTN_NEXT_SLIDE)
        # Карусель Swiper имеет анимацию ~0.3-0.5 сек. Даем ей время завершиться перед проверкой
        time.sleep(0.5)
        return self

    @allure.step('Метод переключения баннера на предыдущий слайд')
    def click_prev_banner(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsForMainPage.BTN_PREV_SLIDE))
        self.click_element(LocatorsForMainPage.BTN_PREV_SLIDE)
        # Карусель Swiper имеет анимацию ~0.3-0.5 сек. Даем ей время завершиться перед проверкой
        #time.sleep(0.5)
        return self

    # ==================================================================================================================
    # === ПРОВЕРКИ ===
    # ==================================================================================================================
    @allure.step('Метод получения ссылки (href) текущего активного баннера')
    def get_current_banner_href(self) -> str:
        """ Возвращает URL, куда ведет текущий баннер """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForMainPage.CURRENT_BANNER_ON_PAGE))
        element = self.find(LocatorsForMainPage.CURRENT_BANNER_ON_PAGE)
        return element.get_attribute('href')

    @allure.step('Метод получения списка тегов в карточках блока {block_name}')
    def get_tags_in_block(self, locator) -> list[str]:
        """ Собирает тексты всех видимых тегов (стикеров) в указанном блоке """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        elements = self.find_all(locator)
        # Фильтруем пустые строки и убираем пробелы
        return [el.text.strip() for el in elements if el.text.strip()]

    @allure.step('Проверка, что URL содержит ожидаемую подстроку {expected_part}')
    def is_url_contains(self, expected_part: str) -> bool:
        return expected_part in self.driver.current_url