import allure
from selenium.webdriver.common.by import By


from pages.base_page import BasePage
from locators.components.auth_locators import LocatorsForAuthModal

class AuthModalComponent(BasePage):
    """ Методы модалки авторизации """

    @allure.step('Метод ввода логина')
    def enter_login(self, email: str):
        self.type(LocatorsForAuthModal.INPUT_LOGIN, email)
        return self

    @allure.step('Метод проверки сообщения с ошибкой под полем "Логин"')
    def check_error_message_login(self) -> bool:
        return self.is_visible(LocatorsForAuthModal.ERROR_MSG_LOGIN)

    @allure.step('Метод ввода пароля')
    def enter_password(self, password: str):
        self.type(LocatorsForAuthModal.INPUT_PASSWORD, password)
        return self

    @allure.step('Метод проверки сообщения с ошибкой под полем "Пароль"')
    def check_error_message_password(self) -> bool:
        return self.is_visible(LocatorsForAuthModal.ERROR_MSG_PASSWORD)

    @allure.step('Метод клика чекбокса "Запомнить меня"')
    def click_checkbox_remember_me(self):
        self.click(LocatorsForAuthModal.CHECKBOX_REMEMBER_ME)
        return self

    @allure.step('Метод клика кнопки "Войти"')
    def click_auth_button(self):
        self.click(LocatorsForAuthModal.BTN_VITY)
        return self

    @allure.step('Метод проверки уведомления об ошибке при авторизации с недействительными данными')
    def check_error_notification(self) -> bool:
        return self.is_visible(LocatorsForAuthModal.ERROR_NOTIFICATION)
