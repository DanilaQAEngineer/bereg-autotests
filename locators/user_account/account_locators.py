

from selenium.webdriver.common.by import By


class LocatorsForAccount:
    """ Локаторы для личного кабинета """

    #    Табы:
    TAB_PERSONAL_CABINET = (By.CSS_SELECTOR, 'div.left_block a[href="/personal/index.php"]')  # Мой кабинет
    TAB_PERSONAL_DATA = (By.CSS_SELECTOR, 'div.left_block a[href="/personal/private/"]')  # Личные данные
    TAB_PERSONAL_CHECK = (By.CSS_SELECTOR, 'div.left_block a[href="/personal/account/"]')  # Личный счёт
    TAB_ORDERS = (By.CSS_SELECTOR, 'div.left_block a[href="/personal/orders/"]')  # Заказы
    TAB_PROFILE_ORDERS = (By.CSS_SELECTOR, 'div.left_block a[href="/personal/profiles/"]')  # Профили заказов
    TAB_SUBSCRIBES = (By.CSS_SELECTOR, 'div.left_block a[href="/personal/subscribe/"]')  # Подписки
    TAB_FAVORITE_CARDS = (By.CSS_SELECTOR, 'div.left_block a[href="/personal/favorite/"')  # Избранные товары
    TAB_HELP = (By.CSS_SELECTOR, 'div.left_block a[href="/help/faq/"]')  # Помощь

    #    Заголовки:
    TITLE_IN_TAB = (By.CSS_SELECTOR, 'div.page-top-info h1[id="pagetitle"]')  # Заголовок в табах кабинет

    #    Хлебные крошки:  (нужен для возврата в ЛК, т.к. в некоторых табах непонятно куда редиректит (не в пределах ЛК))
    BREADCRUMBS_PERSONAL_CABINET = (By.CSS_SELECTOR, 'div.cowl a[title="Личный кабинет"]')

    #    Таб "Избранные товары":
    TEXT_EMPTY_PAGE_FAVORITE = (By.CSS_SELECTOR, 'div.cabinte-page div.alert-success')  # Избранные товары > Текстовка на странице пустого раздела

    #    Кнопки:
    BTN_EXIT = (By.XPATH, '(//*[@class="dark_link top-level-link rounded-x  link-with-flag"])[8]')  # Выйти
    #BTN_WRITE_MESSAGE = (By.CLASS_NAME, 'div.rounded-x span[data-name="question"]')  # Помощь > Кнопка "Написаться сообщение"
    BTN_WRITE_MESSAGE = (By.XPATH, '(//span[text()="Написать сообщение"])')  # Помощь > Кнопка "Написаться сообщение"
    BTN_CLEAR = (By.CSS_SELECTOR, 'div.topic div.js_clear_favorits')  # Избранные товары > Кнопка "Очистить"

    #    Таб "Заказы":
    TEXT_EMPTY_PAGE_ORDERS = (By.CSS_SELECTOR, 'div.cabinte-page div.alert-warning')  # Заказы > Текстовка на странице пустого раздела (когда по фильтрам нет результатов)
    DROPDOWN_STATUS_ORDER = (By.CSS_SELECTOR, 'div.content-md div[data-name="by_status"]')  # Дропдаун "Статус заказа"
    SELECT_STATUS_BY_OTMENA = (By.XPATH, '(//span[text()="Отменен"])[1]')  # Дропдаун "Статус заказа" > Отменен
    SELECT_STATUS_BY_VYPOLNEN = (By.XPATH, '(//span[text()="Выполнен"])[1]')  # Дропдаун "Статус заказа" > Отменен
    DROPDOWN_STATUS_PAYMENT = (By.CSS_SELECTOR, 'div.content-md div[data-name="by_payed"]')  # Дропдаун "Статус оплаты"
    SELECT_STATUS_BY_DONT_PAYMENT = (By.XPATH, '(//span[text()="Не оплачен"])[1]')  # Дропдаун "Статус оплаты" > Отменен
    DROPDOWN_PERIOD = (By.CSS_SELECTOR, 'div.content-md div[data-name="by_year"]')  # Дропдаун "Период"(//span[text()="2026"])[1]
    SELECT_2026_PERIOD = (By.XPATH, '(//span[text()="2026"])[1]')  # Дропдаун "Период" > 2026
    CHECK_MESSAGE_IN_EMPTY_PAGE = (By.CSS_SELECTOR, 'div.personal__block div.alert-warning')  # Заказы > Текстовка на странице пустого раздела
    CHECK_ORDER_STATUS = (By.CSS_SELECTOR, 'div.orders__order__wrapper div.order__status__value')  # Заказы > арточка заказа > Поле "Статус"