

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
    BTN_EXIT = (By.XPATH, '(//*[@class="dark_link top-level-link rounded-x  link-with-flag"])[8]')  # Выйти

    #    Заголовки:
    TITLE_IN_TAB = (By.CSS_SELECTOR, 'div.page-top-info h1[id="pagetitle"]')  # Заголовок в табах кабинет

    #    Хлебные крошки:  (нужен для возврата в ЛК, т.к. в некоторых табах непонятно куда редиректит (не в пределах ЛК))
    BREADCRUMBS_PERSONAL_CABINET = (By.CSS_SELECTOR, 'div.cowl a[title="Личный кабинет"]')