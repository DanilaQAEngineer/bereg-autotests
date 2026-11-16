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


    ###    2) Методы действий с элементами на странице:
    @allure.step('Метод клика по табу "Мой кабинет"')
    def click_tab_my_cabinet(self):
        self.click(LocatorsForAccount.TAB_PERSONAL_CABINET)
        return self

    @allure.step('Метод клика по табу "Личные данные"')
    def click_tab_personal_data(self):
        self.click(LocatorsForAccount.TAB_PERSONAL_DATA)
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
