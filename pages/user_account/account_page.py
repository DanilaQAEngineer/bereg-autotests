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


    ###    1) Методы нахождения_проверки_получения элементов на странице:
    @allure.step('Метод получения заголовка табов')  # Один универсальный локатор для всех
    def get_title(self):
        return self.get_text(LocatorsForAccount.TITLE_IN_TAB)

    @allure.step('Метод получения статусов заказов в табе "Заказы" после фильтрации')
    def get_all_order_statuses(self) -> list[str]:
        # Используем find_all из BasePage, чтобы найти все элементы
        elements = self.find_all(LocatorsForAccount.CHECK_ORDER_STATUS)
        # Собираем текст из каждого элемента в список
        return [el.text.strip() for el in elements]

    @allure.step('Метод поиска текстовки о пустоте раздела "Избранные товары"')
    def is_favorites_empty(self) -> bool:
        return self.is_visible(LocatorsForAccount.TEXT_EMPTY_PAGE_FAVORITE)

    @allure.step('Метод поиска текстовки о пустоте раздела "Заказы"')
    def is_orders_empty(self) -> bool:
        return self.is_visible(LocatorsForAccount.CHECK_MESSAGE_IN_EMPTY_PAGE)

    @allure.step('Метод поиска текстовки  сохранении новых данных в разделе "Личные данные"')
    def is_success_message_after_saving_data(self) -> bool:
        return self.is_visible(LocatorsForAccount.MSG_AFTER_SAVING_NEW_DATA)

    @allure.step('Метод проверки наличия сообщений об обязательности заполнения пустых полей: "ФИО"')
    def is_error_message_fio_in_tab_personal_data(self) -> bool:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.ERROR_INPUT_NAME_IN_TAB_PERSONAL_DATA))
        return self.is_visible(LocatorsForAccount.ERROR_INPUT_NAME_IN_TAB_PERSONAL_DATA)

    @allure.step('Метод проверки наличия сообщений об обязательности заполнения пустых полей: "E-mail"')
    def is_error_message_email_in_tab_personal_data(self) -> bool:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.ERROR_INPUT_EMAIL_IN_TAB_PERSONAL_DATA))
        return self.is_visible(LocatorsForAccount.ERROR_INPUT_EMAIL_IN_TAB_PERSONAL_DATA)

    @allure.step('Метод проверки наличия сообщений об обязательности заполнения пустых полей: "Телефон"')
    def is_error_message_phone_in_tab_personal_data(self) -> bool:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAccount.ERROR_INPUT_PHONE_IN_TAB_PERSONAL_DATA))
        return self.is_visible(LocatorsForAccount.ERROR_INPUT_PHONE_IN_TAB_PERSONAL_DATA)

    @allure.step('Метод проверки наличия значения в полях модалки "Задать вопрос"')
    def is_field_filled_in_personal_data(self, locator) -> bool:
        """Универсальная проверка любого input-поля на наличие значения."""
        element = self.find(locator)
        value = element.get_attribute('value')
        return bool(value and value.strip())

    ###    2) Методы действий с элементами на странице:
    @allure.step('Метод клика по табу "Мой кабинет"')
    def click_tab_my_cabinet(self):
        self.click(LocatorsForAccount.TAB_PERSONAL_CABINET)
        return self

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

    @allure.step('Метод клика по табу "Личный счёт"')
    def click_tab_personal_check(self):
        self.click(LocatorsForAccount.TAB_PERSONAL_CHECK)
        return self

    @allure.step('Метод клика по табу "Заказы"')
    def click_tab_orders(self):
        self.click(LocatorsForAccount.TAB_ORDERS)
        return self

    @allure.step('Метод клика по дропдауну "Статус заказа"')
    def click_dropdown_order_status(self):
        self.click(LocatorsForAccount.DROPDOWN_STATUS_ORDER)
        return self

    @allure.step('Метод выбора параметра "Отменен" в дропдауне "Статус заказа"')
    # def select_otmena_in_dropdown_status_order(self, status_text: str):
    #     # Ждем, пока дропдаун появится, и выбираем опцию по видимому тексту
    #     element = self.find(LocatorsForAccount.FILTER_STATUS_ORDER)
    #     Select(element).select_by_visible_text(status_text)
    #     return self
    def select_otmena_in_dropdown_status_order(self):
        self.click(LocatorsForAccount.SELECT_STATUS_BY_OTMENA)
        return self

    @allure.step('Метод выбора параметра "Выполнен" в дропдауне "Статус заказа"')
    # def select_otmena_in_dropdown_status_order(self, status_text: str):
    #     # Ждем, пока дропдаун появится, и выбираем опцию по видимому тексту
    #     element = self.find(LocatorsForAccount.FILTER_STATUS_ORDER)
    #     Select(element).select_by_visible_text(status_text)
    #     return self
    def select_vypolnen_in_dropdown_status_order(self):
        self.click(LocatorsForAccount.SELECT_STATUS_BY_VYPOLNEN)
        return self

    @allure.step('Метод клика по дропдауну "Статус оплаты"')
    def click_dropdown_payment_status(self):
        self.click(LocatorsForAccount.DROPDOWN_STATUS_PAYMENT)
        return self

    @allure.step('Метод выбора параметра "Не оплачен" в дропдауне "Статус оплаты"')
    # def select_filter_status_payment(self, payment_text: str):
    #     element = self.find(LocatorsForAccount.FILTER_STATUS_PAYMENT)
    #     Select(element).select_by_visible_text(payment_text)
    #     return self
    def select_dont_payment_in_dropdown_status_payment(self):
        self.click(LocatorsForAccount.SELECT_STATUS_BY_DONT_PAYMENT)
        return self

    @allure.step('Метод клика по дропдауну "Период"')
    def click_dropdown_period(self):
        self.click(LocatorsForAccount.DROPDOWN_PERIOD)
        return self

    @allure.step('Метод выбора параметра "2026" в дропдауне "Период"')
    # def select_filter_status_payment(self, payment_text: str):
    #     element = self.find(LocatorsForAccount.FILTER_STATUS_PAYMENT)
    #     Select(element).select_by_visible_text(payment_text)
    #     return self
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

    @allure.step('Метод клика по табу "Профили заказов"')
    def click_tab_profile_orders(self):
        self.click(LocatorsForAccount.TAB_PROFILE_ORDERS)
        return self

    @allure.step('Метод клика по табу "Подписки"')
    def click_tab_subscribes(self):
        self.click(LocatorsForAccount.TAB_SUBSCRIBES)
        return self

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
