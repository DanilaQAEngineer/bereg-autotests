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

    @allure.step('Метод клика по табу "Помощь"')
    def click_tab_help(self):
        self.click(LocatorsForAccount.TAB_HELP)
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