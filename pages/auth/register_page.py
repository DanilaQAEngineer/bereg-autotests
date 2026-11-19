import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from pages.base_page import BasePage
from locators.components.auth_locators import LocatorsForAuthModal


class RegisterPage(BasePage):
    """ Методы для страницы регистрации: Главная–Авторизация–Регистрация """

    # ==================================================================================================================
    # === НАВИГАЦИЯ ===
    # ==================================================================================================================
    @allure.step('Метод ввода ФИО')
    def enter_fio_in_registration_page(self, fio: str):
        self.type(LocatorsForAuthModal.INPUT_FIO_IN_REGISTRATION_PAGE, fio)
        return self

    @allure.step('Метод очистки поля "ФИО"')
    def clear_fio_field(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAuthModal.INPUT_FIO_IN_REGISTRATION_PAGE))
        element = self.find(LocatorsForAuthModal.INPUT_FIO_IN_REGISTRATION_PAGE)
        element.clear()
        return self

    @allure.step('Метод ввода E-mail')
    def enter_email_in_registration_page(self, email: str):
        self.type(LocatorsForAuthModal.INPUT_EMAIL_IN_REGISTRATION_PAGE, email)
        return self

    @allure.step('Метод ввода телефона')
    def enter_phone_in_registration_page(self, phone: str):
        self.type(LocatorsForAuthModal.INPUT_PHONE_IN_REGISTRATION_PAGE, phone)
        return self

    @allure.step('Метод ввода пароля')
    def enter_password_in_registration_page(self, password: str):
        self.type(LocatorsForAuthModal.INPUT_PASSWORD_IN_REGISTRATION_PAGE, password)
        return self

    @allure.step('Метод очистки поля "Пароль"')
    def clear_password_field(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAuthModal.INPUT_PASSWORD_IN_REGISTRATION_PAGE))
        element = self.find(LocatorsForAuthModal.INPUT_EMAIL_IN_REGISTRATION_PAGE)
        element.clear()
        return self

    @allure.step('Метод повторного ввода пароля')
    def enter_confirm_password_in_registration_page(self, confirm_password: str):
        self.type(LocatorsForAuthModal.INPUT_CONFIRM_PASSWORD_IN_REGISTRATION_PAGE, confirm_password)
        return self

    @allure.step('Метод клика по первому чекбоксу')
    def enter_checkbox_1_password_in_registration_page(self):
        self.click(LocatorsForAuthModal.CHECKBOX_1_IN_REGISTRATION_PAGE)
        return self

    @allure.step('Метод клика по второму чекбоксу')
    def enter_checkbox_2_password_in_registration_page(self):
        self.click(LocatorsForAuthModal.CHECKBOX_2_IN_REGISTRATION_PAGE)
        return self

    @allure.step('Метод клика по кнопке "Зарегистрироваться"')
    def click_submit_empty(self):
        self.click(LocatorsForAuthModal.BTN_REGISTRATION_IN_REGISTRATION_PAGE)
        return self

    # ==================================================================================================================
    # === ПРОВЕРКИ ===
    # ==================================================================================================================
    @allure.step('Метод проверки наличия значения в инпут-полях (в полях есть данные?)')
    def is_field_filled(self, locator) -> bool:
        """ Универсальная проверка любого input-поля на наличие значения """
        element = self.find(locator)
        value = element.get_attribute('value')
        return bool(value and value.strip())

    @allure.step('Проверка состояния чекбокса (флажок в чекбоксе выставлен?)')
    def is_checkbox_checked(self, locator) -> bool:
        """ Универсальная проверка любого чекбокса, что он отмечен """
        # Ищем элемент напрямую, без ожидания видимости (чекбоксы часто скрыты)
        element = self.driver.find_element(*locator)
        return element.is_selected()

    @allure.step('Метод проверки заголовка а странице "Регистрация"')
    def check_title_in_registration_page(self):
        return self.get_text(LocatorsForAuthModal.TITLE_IN_REGISTRATION_PAGE)

    @allure.step('Метод проверки_наличия ХК')
    def is_breadcrumbs_visble(self) -> bool:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsForAuthModal.BREADCRUMBS_IN_REGISTRATION_PAGE))
        return self.is_visible(LocatorsForAuthModal.BREADCRUMBS_IN_REGISTRATION_PAGE)

    @allure.step('Метод проверки_получения ошибки под полем "ФИО"')
    def check_email_notification_after_auth(self) -> str:
        return self.get_text(LocatorsForAuthModal.EMAIL_AFTER_AUTH_NOTIFICATION)
