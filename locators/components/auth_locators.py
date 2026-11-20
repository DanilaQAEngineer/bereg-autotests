from selenium.webdriver.common.by import By


class LocatorsForAuthModal:
    """ Локаторы модалки "Вход в личный кабинет" """

    # ==================================================================================================================
    # МОДАЛКА "ВХОД В ЛИЧНЫЙ КАБИНЕТ"
    # ==================================================================================================================

    INPUT_LOGIN = (By.CSS_SELECTOR, 'input[name="USER_LOGIN"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[name="USER_PASSWORD"]')
    CHECKBOX_REMEMBER_ME = (By.CSS_SELECTOR, 'label[for="USER_REMEMBER_frm_64popup"]')
    FARGOT_PASSWORD = (By.CSS_SELECTOR, 'a.forgot')    # Забыли пароль?

    BTN_VITY = (By.CSS_SELECTOR, 'div.auth__bottom button.auth__bottom-btn')
    BTN_REGISTRATION = (By.CSS_SELECTOR, 'div.auth__bottom a.auth__bottom-btn')

    ERROR_MSG_LOGIN = (By.XPATH, '(//*[@class="error"])[1]')    # Ошибка под полем логина: "Заполните это поле!"
    ERROR_MSG_PASSWORD = (By.XPATH, '(//*[@class="error"])[2]')  # Ошибка под полем пароля: "Заполните это поле!"

    #    Уведомления:
    AFTER_AUTH_NOTIFICATION = (By.CSS_SELECTOR, 'div.notice__inner')    # Уведомление после успешной авторизации
    TITLE_AFTER_AUTH_NOTIFICATION = (By.CSS_SELECTOR, 'div.notice__title ')  # Заголовок уведомления после успешной авторизации: "Вы успешно авторизовались"
    EMAIL_AFTER_AUTH_NOTIFICATION = (By.CSS_SELECTOR,'div.notice__detail')    # Почта, под которой залогинились в системе (должна быть = логину)
    ERROR_NOTIFICATION = (By.CSS_SELECTOR, 'div.alert-danger')    # Ошибка под заголовком (когда логинимся с недействительными данными)

    # ==================================================================================================================
    # МОДАЛКА "РЕГИСТРАЦИЯ"
    # ==================================================================================================================
    BREADCRUMBS_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.cowl div.breadcrumbs')
    TITLE_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.topic h1#pagetitle')  # Модалка "Регистрация" > Заголовок "Регистрация"
    INPUT_FIO_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body input#input_NAME')  # Модалка "Регистрация" > Поле "ФИО"
    INPUT_EMAIL_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body input#input_EMAIL')  # Модалка "Регистрация" > Поле "E-mail"
    INPUT_PHONE_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body input#input_PERSONAL_PHONE')  # Модалка "Регистрация" > Поле "Телефон"
    INPUT_PASSWORD_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body input#input_PASSWORD')  # Модалка "Регистрация" > Поле "Пароль"
    INPUT_CONFIRM_PASSWORD_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body input#input_CONFIRM_PASSWORD')  # Модалка "Регистрация" > Поле "Подтверждение пароля"
    #CAPTCHA_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, '')
    CHECKBOX_1_IN_REGISTRATION_PAGE = (By.XPATH, '(//span[@class="form-checkbox__box form-box"])[1]')  # Модалка "Регистрация" > Чекбокс "Продолжая, вы соглашаетесь с ..."
    CHECK_CHECKBOX_1 = (By.CSS_SELECTOR, 'div.form-body input#licenses_register')  # Проверка появления флажка в первом чекбоксе
    CHECKBOX_2_IN_REGISTRATION_PAGE = (By.XPATH, '(//span[@class="form-checkbox__box form-box"])[2]')  # Модалка "Регистрация" > Чекбокс "Продолжая, вы соглашаетесь на ..."
    CHECK_CHECKBOX_2 = (By.CSS_SELECTOR, 'div.form-body input#marketing_popup_OCB')  # Проверка появления флажка во втором чекбоксе
    BTN_REGISTRATION_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-footer button[value="Регистрация"]')  # Модалка "Регистрация" > Кнопка "Зарегстрироваться"

    ERROR_MSG_UNDER_INPUT_FIO_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body label#input_NAME-error')  # Модалка "Регистрация" > Поле "ФИО" > Сообщение об ошибке: "Заполните это поле!"
    ERROR_MSG_UNDER_INPUT_EMAIL_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body label#input_EMAIL-error')  # Модалка "Регистрация" > Поле "E-mail" > Сообщение об ошибке: "Заполните это поле!; Неверный формат!"
    ERROR_MSG_UNDER_INPUT_PHONE_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body label#input_PERSONAL_PHONE-error')  # Модалка "Регистрация" > Поле "Телефон" > Сообщение об ошибке: "Номер слишком короткий; Неверный номер; Номер слишком длинный"
    ERROR_MSG_UNDER_INPUT_PASSWORD_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body label#input_PASSWORD-error')  # Модалка "Регистрация" > Поле "Пароль" > Сообщение об ошибке: "Заполните это поле!; Минимум 6 символов!"
    ERROR_MSG_UNDER_INPUT_CONFIRM_PASSWORD_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body label#input_CONFIRM_PASSWORD-error')  # Модалка "Регистрация" > Поле "Подтверждение пароля" > Сообщение об ошибке: "Заполните это поле!; Пароли не совпадают!"
    ERROR_MSG_UNDER_INPUT_CAPTCHA_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body label#-error')  # Модалка "Регистрация" > Поле "Капча" > Сообщение об ошибке: "Пройдите проверку"
    ERROR_MSG_UNDER_CHECKBOX_1_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body label#licenses_popup-error')  # Модалка "Регистрация" > Поле "Чекбокс_1" > Сообщение об ошибке: "Согласитесь с условиями"
    ERROR_MSG_UNDER_CHECKBOX_2_IN_REGISTRATION_PAGE = (By.CSS_SELECTOR, 'div.form-body label#marketing_popup-error')  # Модалка "Регистрация" > Поле "Чекбокс_2" > Сообщение об ошибке: "Заполните это поле!"

