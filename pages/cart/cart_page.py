import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from config.settings import settings
from pages.base_page import BasePage
from locators.cart.cart_locators import LocatorsForCart


class Basket(BasePage):
    """ Методы для тестирования корзины товаров """

    # ==================================================================================================================
    # === ДЕЙСТВИЯ ===
    # ==================================================================================================================
    @allure.step('Метод открытия страницы корзины')
    def open_basket_page(self):
        self.driver.get(f'{settings.base_url}/basket/')
        return self

    @allure.step('Ввод текста "{value}" в поле {locator}')
    def enter_text(self, locator, value: str) -> "Basket":
        """ Универсальный метод ввода данных в любое текстовое поле """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.type(locator, value)
        return self

    @allure.step('Универсальный метод клика (JS)')
    def click_element(self, locator):
        """Универсальный метод клика. Используем JS-клик, чтобы обойти перекрытия (оверлеи)"""
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)
        return self

    # ==================================================================================================================
    # === ПРОВЕРКИ ===
    # ==================================================================================================================
    @allure.step('Метод ожидания видимости элемента {locator}')
    def wait_until_visible(self, locator, timeout=10):
        """
        Ждет, пока элемент станет видимым на странице
        (метод нужен для того, чтобы искать какой-то элемент перед действием (замена таймслипов))
        """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self

    @allure.step("Универсальный метод проверки элемента на странице")
    def is_element_visible(self, locator) -> bool:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.is_visible(locator)

    @allure.step('Метод ожидания пересчёта тоговой суммы корзины')
    def wait_for_cart_total_change(self, timeout=5):
        """Ждёт, пока в корзине появится/обновится элемент с суммой."""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(LocatorsForCart.PRICE_IN_ITOGO_BLOCK)
        )
        return self

    @allure.step('Метод проверки наличия товаров в корзине')
    def get_cart_in_basket(self) -> bool:
        return self.is_visible(LocatorsForCart.CARD_IN_BASKET)

    @allure.step('Метод получения названия товара')
    def get_title_first_card(self) -> str:
        return self.get_text(LocatorsForCart.TITLE_ADDED_CARD)

    @allure.step('Метод получения количества единиц в карточке товара')
    def get_count_cart_in_card(self) -> str:
        element = self.find(LocatorsForCart.COUNT_TOVAROV)
        return element.get_attribute('value')

    @allure.step('Метод получения цены товара (в самой карточке)')
    def get_price_cart_in_card(self) -> str:
        return self.get_text(LocatorsForCart.PRICE_IN_CARD)

    @allure.step('Метод получения цены товара (в блоке "Итого")')
    def get_final_price_cart(self) -> str:
        return self.get_text(LocatorsForCart.PRICE_IN_ITOGO_BLOCK)

    # @allure.step('Метод клика кнопки "+" в карточке первого товара')
    # def click_button_plus(self):
    #     self.find_all(LocatorsForCart.BUTTON_PLUS)[0].click()
    #     return self

    @allure.step('Метод клика кнопки "+" в карточке товара')
    def click_button_plus(self):
        self.click(LocatorsForCart.BUTTON_PLUS)
        return self

    @allure.step('Метод клика кнопки "-" в карточке первого товара')
    def click_button_minus(self):
        self.find_all(LocatorsForCart.BUTTON_MINUS)[0].click()
        return self

    @allure.step('Метод клика кнопки "Удалить_Корзина" в карточке первого товара')
    def click_button_delete(self):
        self.find_all(LocatorsForCart.BUTTON_DELETE_CARD)[0].click()
        return self

    @allure.step('Метод клика кнопки "Удалить" (подтверждение удаления карточки из корзины) в карточке первого товара')
    def click_button_repeat_delete(self):
        self.find_all(LocatorsForCart.BUTTON_REPEAT_DELETE_CARD)[0].click()
        return self

    @allure.step('Метод проверки, что после первого удаления товара из корзины появляется напоминалка под "Итого > Промокод"')
    def check_message_pod_promokod(self) -> bool:
        return self.is_visible(LocatorsForCart.MINIMAL_SUM_ZAKAZA)

    @allure.step('Метод получения содержимого сообщения после удаления товара')
    def get_text_message_pod_promokod(self) -> str:
        return self.get_text(LocatorsForCart.VALUE_MINIMAL_SUM_ZAKAZA)