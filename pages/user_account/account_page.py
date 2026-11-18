import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


from config.settings import settings
from pages.base_page import BasePage
from locators.user_account.account_locators import LocatorsForAccount


class AccountPage(BasePage):
    """ Методы для работы в личном кабинете """

    @allure.step('Метод перехода в личный кабинет')
    def open_account_page(self):
        self.driver.get(f'{settings.base_url}/personal/')
        return self


    # === Проверки ===
    @allure.step('Метод получения заголовка табов')  # Один универсальный локатор для всех
    def get_title(self):
        return self.get_text(LocatorsForAccount.TITLE_IN_TAB)

    @allure.step('Метод проверки наличия значения в инпут-полях')
    def is_field_filled(self, locator) -> bool:
        """Универсальная проверка любого input-поля на наличие значения."""
        element = self.find(locator)
        value = element.get_attribute('value')
        return bool(value and value.strip())

    @allure.step('Проверка состояния чекбокса')
    def is_checkbox_checked(self, locator) -> bool:
        """ Универсальная проверка любого чекбокса, что он отмечен """
        # Ищем элемент напрямую, без ожидания видимости (чекбоксы часто скрыты)
        element = self.driver.find_element(*locator)
        return element.is_selected()

    # ==================================================================================================================
    # ТАБ "ЗАКАЗЫ"
    # ==================================================================================================================

    # === Навигация ===
    @allure.step('Метод клика по табу "Заказы"')
    def click_tab_orders(self):
        self.click(LocatorsForAccount.TAB_ORDERS)
        return self

    @allure.step('Метод клика по дропдауну "Статус заказа"')
    def click_dropdown_order_status(self):
        self.click(LocatorsForAccount.DROPDOWN_STATUS_ORDER)
        return self

    @allure.step('Метод выбора параметра "Отменен" в дропдауне "Статус заказа"')
    def select_otmena_in_dropdown_status_order(self):
        self.click(LocatorsForAccount.SELECT_STATUS_BY_OTMENA)
        return self

    @allure.step('Метод выбора параметра "Выполнен" в дропдауне "Статус заказа"')
    def select_vypolnen_in_dropdown_status_order(self):
        self.click(LocatorsForAccount.SELECT_STATUS_BY_VYPOLNEN)
        return self

    @allure.step('Метод клика по дропдауну "Статус оплаты"')
    def click_dropdown_payment_status(self):
        self.click(LocatorsForAccount.DROPDOWN_STATUS_PAYMENT)
        return self

    @allure.step('Метод выбора параметра "Не оплачен" в дропдауне "Статус оплаты"')
    def select_dont_payment_in_dropdown_status_payment(self):
        self.click(LocatorsForAccount.SELECT_STATUS_BY_DONT_PAYMENT)
        return self

    @allure.step('Метод клика по дропдауну "Период"')
    def click_dropdown_period(self):
        self.click(LocatorsForAccount.DROPDOWN_PERIOD)
        return self

    @allure.step('Метод выбора параметра "2026" в дропдауне "Период"')
    def select_2026_in_dropdown_period(self):
        self.click(LocatorsForAccount.SELECT_2026_PERIOD)
        return self

    @allure.step('Метод клика по карточке заказа')
    def click_card_order(self):
        self.click(LocatorsForAccount.ORDER_CARD)
        return self

    @allure.step('Метод клика по кнопке "Повторить заказ" в карточке заказа')
    def click_repeat_order_in_order_card(self):
        self.click(LocatorsForAccount.BTN_REPEAT_IN_ORDER)
        return self

    @allure.step('Метод клика по кнопке "Задать вопрос" в карточке заказа')
    def click_ask_question_in_order_card(self):
        self.click(LocatorsForAccount.BTN_ASK_QUESTION)
        return self

    # === Проверки ===
    @allure.step('Метод получения статусов заказов в табе "Заказы" после фильтрации')
    def get_all_order_statuses(self) -> list[str]:
        elements = self.find_all(LocatorsForAccount.CHECK_ORDER_STATUS)  # Используем find_all из BasePage, чтобы найти все элементы
        return [el.text.strip() for el in elements]  # Собираем текст из каждого элемента в список

    @allure.step('Метод поиска текстовки о пустоте раздела "Заказы"')
    def is_orders_empty(self) -> bool:
        return self.is_visible(LocatorsForAccount.CHECK_MESSAGE_IN_EMPTY_PAGE)

    # ==================================================================================================================
    # ТАБ "МОЙ КАБИНЕТ"
    # ==================================================================================================================

    # === Навигация ===
    @allure.step('Метод клика по табу "Мой кабинет"')
    def click_tab_my_cabinet(self):
        self.click(LocatorsForAccount.TAB_PERSONAL_CABINET)
        return self

    # ==================================================================================================================
    # ТАБ "ЛИЧНЫЕ ДАННЫЕ"
    # ==================================================================================================================

    # === Навигация ===
    @allure.step('Метод клика по табу "Личные данные"')
    def click_tab_personal_data(self):
        self.click(LocatorsForAccount.TAB_PERSONAL_DATA)
        return self

    @allure.step('Метод очистки поля "ФИО" на странице таба "Личные данные"')
    def clear_name_field_in_tab_personal_data(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LocatorsForAccount.INPUT_NAME_IN_TAB_PERSONAL_DATA))
        element = self.find(LocatorsForAccount.INPUT_NAME_IN_TAB_PERSONAL_DATA)  # Твой локатор поля имени
        element.clear()
        return self

    @allure.step('Метод очистки поля "E-mail" на странице таба "Личные данные"')
    def clear_email_field_in_tab_personal_data(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LocatorsForAccount.INPUT_EMAIL_IN_TAB_PERSONAL_DATA))
        element = self.find(LocatorsForAccount.INPUT_EMAIL_IN_TAB_PERSONAL_DATA)  # Твой локатор поля имени
        element.clear()
        return self

    @allure.step('Метод очистки поля "Телефон" на странице таба "Личные данные"')
    def clear_phone_field_in_tab_personal_data(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LocatorsForAccount.INPUT_PHONE_IN_TAB_PERSONAL_DATA))
        element = self.find(LocatorsForAccount.INPUT_PHONE_IN_TAB_PERSONAL_DATA)  # Твой локатор поля имени
        element.clear()
        return self

    @allure.step('Метод ввода данных в поле "ФИО" (таб "Личные данные")')
    def enter_fio_in_personal_data(self, fio: str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.INPUT_NAME_IN_TAB_PERSONAL_DATA))
        self.type(LocatorsForAccount.INPUT_NAME_IN_TAB_PERSONAL_DATA, fio)
        return self

    @allure.step('Метод ввода данных в поле "E-mail" (таб "Личные данные")')
    def enter_email_in_personal_data(self, email: str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.INPUT_EMAIL_IN_TAB_PERSONAL_DATA))
        self.type(LocatorsForAccount.INPUT_EMAIL_IN_TAB_PERSONAL_DATA, email)
        return self

    @allure.step('Метод ввода данных в поле "Телефон" (таб "Личные данные")')
    def enter_phone_in_personal_data(self, phone: str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.INPUT_PHONE_IN_TAB_PERSONAL_DATA))
        self.type(LocatorsForAccount.INPUT_PHONE_IN_TAB_PERSONAL_DATA, phone)
        return self

    @allure.step('Метод клика по кнопке "Сохранить изменения" в табе "Личные данные"')
    def click_btn_save_in_tab_personal_data(self):
        self.click(LocatorsForAccount.BTN_SAVE_IN_TAB_PERSONAL_DATA)
        return self

    # === Проверки ===
    @allure.step('Метод поиска текстовки  сохранении новых данных в разделе "Личные данные"')
    def is_success_message_after_saving_data(self) -> bool:
        return self.is_visible(LocatorsForAccount.MSG_AFTER_SAVING_NEW_DATA)

    @allure.step('Метод проверки наличия сообщений об обязательности заполнения пустых полей: "ФИО"')
    def is_error_message_fio_in_tab_personal_data(self) -> bool:
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LocatorsForAccount.ERROR_INPUT_NAME_IN_TAB_PERSONAL_DATA))
        return self.is_visible(LocatorsForAccount.ERROR_INPUT_NAME_IN_TAB_PERSONAL_DATA)

    @allure.step('Метод проверки наличия сообщений об обязательности заполнения пустых полей: "E-mail"')
    def is_error_message_email_in_tab_personal_data(self) -> bool:
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LocatorsForAccount.ERROR_INPUT_EMAIL_IN_TAB_PERSONAL_DATA))
        return self.is_visible(LocatorsForAccount.ERROR_INPUT_EMAIL_IN_TAB_PERSONAL_DATA)

    @allure.step('Метод проверки наличия сообщений об обязательности заполнения пустых полей: "Телефон"')
    def is_error_message_phone_in_tab_personal_data(self) -> bool:
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LocatorsForAccount.ERROR_INPUT_PHONE_IN_TAB_PERSONAL_DATA))
        return self.is_visible(LocatorsForAccount.ERROR_INPUT_PHONE_IN_TAB_PERSONAL_DATA)

    # ==================================================================================================================
    # ТАБ "ЛИЧНЫЙ СЧЁТ"
    # ==================================================================================================================

    @allure.step('Метод клика по табу "Личный счёт"')
    def click_tab_personal_check(self):
        self.click(LocatorsForAccount.TAB_PERSONAL_CHECK)
        return self


    # ==================================================================================================================
    # ТАБ "ПРОФИЛИ ЗАКАЗОВ"
    # ==================================================================================================================

    @allure.step('Метод клика по табу "Профили заказов"')
    def click_tab_profile_orders(self):
        self.click(LocatorsForAccount.TAB_PROFILE_ORDERS)
        return self

    # ==================================================================================================================
    # ТАБ "ПОДПИСКИ"
    # ==================================================================================================================

    # === Навигация ===
    @allure.step('Метод клика по табу "Подписки"')
    def click_tab_subscribes(self):
        self.click(LocatorsForAccount.TAB_SUBSCRIBES)
        return self

    @allure.step('Метод очистки поля "Ваш e-mail" (таб "Подписки")')
    def clear_email_field_in_subscribes_tab(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.INPUT_EMAIL_IN_TAB_SUBSCRIBES))
        element = self.find(LocatorsForAccount.INPUT_EMAIL_IN_TAB_SUBSCRIBES)  # Твой локатор поля имени
        element.clear()
        return self

    @allure.step('Метод ввода данных в поле "Ваш e-mail" (таб "Подписки")')
    def enter_email_in_subscribes_tab(self, email: str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.INPUT_EMAIL_IN_TAB_SUBSCRIBES))
        self.type(LocatorsForAccount.INPUT_EMAIL_IN_TAB_SUBSCRIBES, email)
        return self

    @allure.step('Метод клика по чекбоксу "Первая рассылка" в табе "Подписки"')
    def click_checkbox_rub_1_in_subscribes_tab(self):
        self.click(LocatorsForAccount.CHECKBOX_RUB_1_IN_TAB_SUBSCRIBES)
        return self

    @allure.step('Метод клика по чекбоксу "Новости магазина" в табе "Подписки"')
    def click_checkbox_rub_2_in_subscribes_tab(self):
        self.click(LocatorsForAccount.CHECKBOX_RUB_2_IN_TAB_SUBSCRIBES)
        return self

    @allure.step('Метод клика по радиокнопке "Текст" в табе "Подписки"')
    def click_radio_button_1_in_subscribes_tab(self):
        self.click(LocatorsForAccount.RADIOBUTTON_1_IN_TAB_SUBSCRIBES)
        return self

    @allure.step('Метод клика по радиокнопке "HTML" в табе "Подписки"')
    def click_radio_button_2_in_subscribes_tab(self):
        self.click(LocatorsForAccount.RADIOBUTTON_2_IN_TAB_SUBSCRIBES)
        return self

    @allure.step('Метод клика по кнопке "Добавить" в табе "Подписки"')
    def click_btn_add_in_subscribes_tab(self):
        self.click(LocatorsForAccount.BTN_ADD_IN_TAB_SUBSCRIBES)
        return self

    @allure.step('Метод клика по кнопке "Изменить" в табе "Подписки"')
    def click_btn_save_in_subscribes_tab(self):
        self.click(LocatorsForAccount.BTN_SAVE_IN_TAB_SUBSCRIBES)
        return self

    @allure.step('Метод клика по кнопке "Сброс" в табе "Подписки"')
    def click_btn_reset_in_subscribes_tab(self):
        self.click(LocatorsForAccount.BTN_RESET_IN_TAB_SUBSCRIBES)
        return self

    # === Проверки ===
    @allure.step('Метод проверки_получения заголовка "Настройки подписки" в разделе "Подписки"')
    def get_title_in_subscribes_tab(self):
        return self.get_text(LocatorsForAccount.TITLE_IN_TAB_SUBSCRIBES)

    @allure.step('Метод проверки_получения ошибок в разделе "Подписки" (все ошибки в одном локаторе)')
    def get_errors_in_subscribes_tab(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.ERROR_MSG_IN_TAB_SUBSCRIBES))
        return self.get_text(LocatorsForAccount.ERROR_MSG_IN_TAB_SUBSCRIBES)

    @allure.step('Метод проверки_получения сообщения об успехе подписки в разделе "Подписки"')
    def get_success_msg_after_sub_in_subscribes_tab(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.MSG_AFTER_CLICK_BTN_ADD))
        return self.get_text(LocatorsForAccount.MSG_AFTER_CLICK_BTN_ADD)

    @allure.step('Метод проверки появления блока "Подтверждение подписки" после успешной подписки')
    def is_block_verify_subscribe(self) -> bool:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.BLOCK_1_AFTER_SUCCESS_SUBSCRIBE))
        return self.is_visible(LocatorsForAccount.BLOCK_1_AFTER_SUCCESS_SUBSCRIBE)

    @allure.step('Метод проверки_получения заголовка блока "Подтверждение подписки"')
    def get_title_1_success_msg_after_sub_in_subscribes_tab(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.TITLE_BLOCK_1_AFTER_SUCCESS_SUBSCRIBE))
        return self.get_text(LocatorsForAccount.TITLE_BLOCK_1_AFTER_SUCCESS_SUBSCRIBE)

    @allure.step('Метод проверки появления блока "Состояние подписки" после успешной подписки')
    def is_block_status_subscribe(self) -> bool:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.BLOCK_2_AFTER_SUCCESS_SUBSCRIBE))
        return self.is_visible(LocatorsForAccount.BLOCK_2_AFTER_SUCCESS_SUBSCRIBE)

    @allure.step('Метод проверки_получения заголовка блока "Состояние подписки"')
    def get_title_2_success_msg_after_sub_in_subscribes_tab(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.TITLE_BLOCK_2_AFTER_SUCCESS_SUBSCRIBE))
        return self.get_text(LocatorsForAccount.TITLE_BLOCK_2_AFTER_SUCCESS_SUBSCRIBE)

    # ==================================================================================================================
    # ТАБ "ИЗБРАННЫЕ ТОВАРЫ"
    # ==================================================================================================================

    # === Навигация ===
    @allure.step('Метод клика по табу "Избранные товары"')
    def click_tab_favorite_cards(self):
        self.click(LocatorsForAccount.TAB_FAVORITE_CARDS)
        return self

    @allure.step('Метод клика кнопки "Очистить" (в разделе Избранные товары)')
    def click_btn_clear(self):
        self.click(LocatorsForAccount.BTN_CLEAR)
        return self

    @allure.step('Метод клика по табу "Помощь"')
    def click_tab_help(self):
        self.click(LocatorsForAccount.TAB_HELP)
        return self

    @allure.step('Метод клика по кнопке "Написать сообщение"')
    def click_btn_write_message(self):
        self.click(LocatorsForAccount.BTN_WRITE_MESSAGE)
        return self

    @allure.step('Метод клика кнопки "Выйти"')
    def click_btn_exit(self):
        self.click(LocatorsForAccount.BTN_EXIT)
        return self

    @allure.step('Метод клика раздела "Личный кабинет" в хлебных крошках')
    # нужен для возврата в ЛК, т.к. в некоторых табах непонятно куда редиректит (не в пределах ЛК)
    def click_personal_cabinet_in_breadcrumbs(self):
        self.click(LocatorsForAccount.BREADCRUMBS_PERSONAL_CABINET)
        return self

    # === Проверки ===
    @allure.step('Метод поиска текстовки о пустоте раздела "Избранные товары"')
    def is_favorites_empty(self) -> bool:
        return self.is_visible(LocatorsForAccount.TEXT_EMPTY_PAGE_FAVORITE)