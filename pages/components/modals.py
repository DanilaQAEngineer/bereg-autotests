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

    #    --- 1) Методы для модалки "Заказать звонок" ---
    @allure.step('Метод проверки открытия_отображения модалки "Заказать звонок"')
    def is_callback_modal_visible(self) -> bool:
        return self.is_visible(LocatorsForModals.MODAL_CALLBACK)

    @allure.step('Метод клика по кнопке "Отправить"')  # КЛИКАЕМ ПО НЕЙ ОТДЕЛЬНЫМ КЕЙСОМ: ТОЛЬКО КОГДА МОДАЛКА ПУСТАЯ (чтоб ошибки глянуть)
    def click_submit_button(self):
        #    Жду, когда на странице полностью подгрузится капча:
        #        иначе Селениум кликает "Отправить" сразу и там какие-то левые ошибки появляются
        #            UPD: пока без ожидания работает, но если будет падать -- раскомментить строку ниже
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsForModals.CAPTCHA_IFRAME))
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
        self.type(LocatorsForModals.INPUT_CALLBACK_NAME, name)
        return self

    @allure.step('Метод ввода данных в поле "Телефон"')
    def enter_phone(self, phone: str):
        self.type(LocatorsForModals.INPUT_CALLBACK_PHONE, phone)
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


    #    --- 2) Методы для модалки "Быстрый просмотр" ---

    ### ВАЖНО: Метод наведения курсора на фото карточки товара и клик по кнопке "Быстрый просмотор" берём/описан в ProductCardComponent

    ###    2.1) Методы проверки отображения элементов на странице

    @allure.step('Метод проверки открытия_отображения модалки "Быстрый просмотр"')
    def is_quick_view_modal_visible(self) -> bool:
        return self.is_visible(LocatorsForModals.MODAL_QUICK_VIEW)

    @allure.step('Метод получения названия/заголовка товара в модалке "Быстрый просмотр"')
    def check_title_in_modal_quick_view(self) -> str:
        return self.get_text(LocatorsForModals.TITLE_QUICK_VIEW)

    @allure.step('Метод получения кнопки "В избранное"')
    def check_button_in_favorite_in_modal_quick_view(self) -> bool:
        return self.is_visible(LocatorsForModals.BTN_QUICK_VIEW_IN_FAVORITE)

    @allure.step('Метод получения кнопки "В сравнение"')
    def check_button_in_compare_in_modal_quick_view(self) -> bool:
        return self.is_visible(LocatorsForModals.BTN_QUICK_VIEW_IN_COMPARE)

    @allure.step('Метод получения кнопки "В корзину"')
    def check_button_in_basket_in_modal_quick_view(self) -> bool:
        return self.is_visible(LocatorsForModals.BTN_QUICK_VIEW_IN_BASKET)

    @allure.step('Метод получения кнопки "х"')
    def check_button_close_modal_quick_view(self) -> bool:
        return self.is_visible(LocatorsForModals.BTN_QUICK_VIEW_CLOSE)

    @allure.step('Метод получения кнопки "Купить в 1 клик"')
    def check_button_bye_in_one_click_in_modal_quick_view(self) -> bool:
        return self.is_visible(LocatorsForModals.BTN_QUICK_VIEW_BYE_IN_ONE_CLICK)

    @allure.step('Метод проверки наличия кнопки "Подробнее о товаре"')
    def is_button_detailed_visible(self) -> bool:
        return self.is_visible(LocatorsForModals.BTN_DETAILED_QUICK_VIEW)

    @allure.step('Метод проверки наличия кнопки "Предыдущий товар"')
    def is_button_prev_btn_visible(self) -> bool:
        return self.is_visible(LocatorsForModals.BTN_PREV_CARD)

    @allure.step('Метод проверки наличия кнопки "Следующий товар"')
    def is_button_next_btn_visible(self) -> bool:
        return self.is_visible(LocatorsForModals.BTN_NEXT_CARD)

    @allure.step('Метод проверки открытия_отображения модалки "Купить в 1 клик"')
    def is_bye_in_one_click_modal_visible(self) -> bool:
        return self.is_visible(LocatorsForModals.MODAL_BYE_IN_ONE_CLICK)

    @allure.step('Метод получения названия товара/заголовка в модалке "Купить в 1 клик"')
    def check_title_in_modal(self) -> str:
        return self.get_text(LocatorsForModals.TITLE_MODAL_BYE_IN_ONE_CLICK)

    ###    2.2) Методы действий с элементами

    @allure.step('Метод клика по названию/заголовку товара в модалке "Быстрый просмотр"')
    def click_title_in_modal_quick_view(self):
        self.click(LocatorsForModals.TITLE_QUICK_VIEW)
        return self

    ###    2.2) Методы действий с элементами

    @allure.step('Метод клика по кнопке "В корзину"')
    def click_btn_in_basket_in_modal_quick_view(self):
        self.click(LocatorsForModals.BTN_QUICK_VIEW_IN_BASKET)
        return self

    @allure.step('Метод клика по кнопке "Купить в 1 клик"')
    def click_btn_bye_in_one_click_in_modal_quick_view(self):
        self.click(LocatorsForModals.BTN_QUICK_VIEW_BYE_IN_ONE_CLICK)
        return self

    @allure.step('Метод клика по кнопке "Подробнее о товаре"')
    def click_btn_detailed_in_modal_quick_view(self):
        self.click(LocatorsForModals.BTN_DETAILED_QUICK_VIEW)
        return self

    ### добавить методы для переключения фото в карточке, добавление/удаление в сравнение/избранное, клик по кнопке "Купить в 1 клик", переход в карточку ###