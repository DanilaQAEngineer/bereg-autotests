import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


from config.settings import settings
from pages.base_page import BasePage
from locators.components.modals_locators import LocatorsForGlobalModals


class GlobalModalsComponent(BasePage):
    """ Компонент для работы с модальными окнами: Заказать звонок, Быстрый просмотр, Задать вопрос """

    #    --- Методы для "Заказать звонок" ---
    @allure.step('Метод клика по кнопке "Отправить"')  # КЛИКАЕМ ПО НЕЙ ОТДЕЛЬНЫМ КЕЙСОМ: ТОЛЬКО КОГДА МОДАЛКА ПУСТАЯ (чтоб ошибки глянуть)
    def click_submit_button(self):
        self.click(LocatorsForGlobalModals.BTN_CALLBACK_SUBMIT)
        return self

    @allure.step('Метод проверки наличия сообщений об обязательнсти заполнения пустых полей: "Ваше имя"')
    def check_error_message_name(self) -> bool:
        return self.is_visible(LocatorsForGlobalModals.ERROR_MSG_NAME)

    @allure.step('Метод проверки наличия сообщений об обязательнсти заполнения пустых полей: "Телефон"')
    def check_error_message_name(self) -> bool:
        return self.is_visible(LocatorsForGlobalModals.ERROR_MSG_PHONE)

    # @allure.step('Метод проверки наличия сообщений об обязательнсти заполнения пустых полей: "Капча')
    # def check_error_message_capcha(self) -> bool:
    #     return self.is_visible(LocatorsForGlobalModals.)
    #
    # @allure.step('Метод проверки наличия сообщений об обязательнсти заполнения пустых полей: "Согласие с политикой сайта')
    # def check_error_message_confidencial(self) -> bool:
    #     return self.is_visible(LocatorsForGlobalModals.)

    @allure.step('Метод проверки открытия_отображения модалки "Заказать звонок"')
    def is_callback_modal_visible(self) -> bool:
        return self.is_visible(LocatorsForGlobalModals.CALLBACK_MODAL)

    @allure.step('Метод ввода данных в поле "Ваше имя"')
    def enter_name(self, name: str):
        self.type(LocatorsForGlobalModals.CALLBACK_NAME_INPUT, name)
        return self

    @allure.step('Метод ввода данных в поле "Телефон"')
    def enter_phone(self, phone: str):
        self.type(LocatorsForGlobalModals.CALLBACK_PHONE_INPUT, phone)
        return self

    @allure.step('Метод ввода капчи')
    def click_capcha(self):
        self.click(LocatorsForGlobalModals.CAPCHA)
        return self

    @allure.step('Метод клика чекбокса согласия с политикой сайта')
    def click_capcha(self):
        self.click(LocatorsForGlobalModals.CHECKBOX_COFIDENTIONAL)
        return self

    ### добавить методы для ввода капчи и согласия с политикой сайта (они инпуты, но я не помню как их заполнять) ###