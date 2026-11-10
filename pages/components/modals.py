import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


from config.settings import settings
from pages.base_page import BasePage
from locators.components.modals_locators import LocatorsForModals


class ModalsComponent(BasePage):
    """ Компонент для работы с модальными окнами: Заказать звонок, Быстрый просмотр, Задать вопрос """

    #    --- Методы для "Заказать звонок" ---
    @allure.step('Метод проверки открытия_отображения модалки "Заказать звонок"')
    def is_callback_modal_visible(self) -> bool:
        return self.is_visible(LocatorsForModals.CALLBACK_MODAL)

    @allure.step('Метод клика по кнопке "Отправить"')  # КЛИКАЕМ ПО НЕЙ ОТДЕЛЬНЫМ КЕЙСОМ: ТОЛЬКО КОГДА МОДАЛКА ПУСТАЯ (чтоб ошибки глянуть)
    def click_submit_button(self):
        self.click(LocatorsForModals.BTN_CALLBACK_SUBMIT)
        return self

    @allure.step('Метод проверки наличия сообщений об обязательнсти заполнения пустых полей: "Ваше имя"')
    def check_error_message_name(self) -> bool:
        return self.is_visible(LocatorsForModals.ERROR_MSG_NAME)

    @allure.step('Метод проверки наличия сообщений об обязательнсти заполнения пустых полей: "Телефон"')
    def check_error_message_phone(self) -> bool:
        return self.is_visible(LocatorsForModals.ERROR_MSG_PHONE)

    @allure.step('Метод проверки наличия сообщений об обязательнсти заполнения пустых полей: "Капча')
    def check_error_message_capcha(self) -> bool:
        return self.is_visible(LocatorsForModals.ERROR_MSG_CAPCHA)

    @allure.step('Метод проверки наличия сообщений об обязательнсти заполнения пустых полей: "Согласие с политикой сайта')
    def check_error_message_confidencial(self) -> bool:
        return self.is_visible(LocatorsForModals.ERROR_MSG_COFIDENTIONAL)

    @allure.step('Метод ввода данных в поле "Ваше имя"')
    def enter_name(self, name: str):
        self.type(LocatorsForModals.CALLBACK_NAME_INPUT, name)
        return self

    @allure.step('Метод ввода данных в поле "Телефон"')
    def enter_phone(self, phone: str):
        self.type(LocatorsForModals.CALLBACK_PHONE_INPUT, phone)
        return self

    @allure.step('Метод ввода капчи')
    def click_captcha(self):
        #    1. Жду, когда на странице появится хотя бы один iframe капчи:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsForModals.CAPTCHA_IFRAME))
        #    2. Ищу ВСЕ iframe
        iframes = self.driver.find_elements(*LocatorsForModals.CAPTCHA_IFRAME)
        #    3. Ищу среди них видимый и переключаюсь на него
        switched = False
        for iframe in iframes:
            if iframe.is_displayed():
                self.driver.switch_to.frame(iframe)
                switched = True
                break
        if not switched:
            raise AssertionError("Не удалось найти видимый iframe капчи!")
        #    4. Я внутри iframe, жду появления чекбокса
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(LocatorsForModals.CAPTCHA_CHECKBOX))
        #    5. Ищем ВСЕ чекбоксы (отсекаем скрытые дубликаты)
        checkboxes = self.driver.find_elements(*LocatorsForModals.CAPTCHA_CHECKBOX)
        clicked = False
        for cb in checkboxes:
            if cb.is_displayed():
                #    6. Кликаю через JS (обычный клик в Яндексе часто перехватывается невидимым слоем)
                self.driver.execute_script("arguments[0].click();", cb)
                clicked = True
                break
        if not clicked:
            raise AssertionError("Не найден видимый чекбокс капчи!")
        #    7. ОБЯЗАТЕЛЬНО возвращаюсь на основную страницу
        self.driver.switch_to.default_content()
        #    8. Жду, когда Яндекс обработает клик и появится  галочка вместо "Я не робот" (обычно это занимает 1-2 секунды)
        sleep(3)
        return self

    ### добавить методы для ввода капчи и согласия с политикой сайта (они инпуты, но я не помню как их заполнять) ###