from selenium.webdriver.common.by import By


class LocatorsForAuthModal:
    """ Локаторы модалки "Вход в личный кабинет" """

    INPUT_LOGIN = (By.CSS_SELECTOR, 'input[name="USER_LOGIN"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[name="USER_PASSWORD"]')
    CHECKBOX_REMEMBER_ME = (By.CSS_SELECTOR, 'label[for="USER_REMEMBER_frm_64popup"]')
    FARGOT_PASSWORD = (By.CSS_SELECTOR, 'a.forgot')    # Забыли пароль?

    BTN_VITY = (By.CSS_SELECTOR, 'button.auth__bottom-btn')
    BTN_REGISTRATION = (By.CSS_SELECTOR, 'a.auth__bottom-btn')

    ERROR_MSG_LOGIN = (By.XPATH, '(//*[@class="error"])[1]')    # Ошибка под полем логина: "Заполните это поле!"
    ERROR_MSG_PASSWORD = (By.XPATH, '(//*[@class="error"])[2]')  # Ошибка под полем пароля: "Заполните это поле!"

    ERROR_NOTIFICATION = (By.CSS_SELECTOR, 'div.alert-danger')    # Ошибка под заголовком (когда логинимся с недействительными данными)