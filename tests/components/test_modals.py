import allure
import pytest
from time import sleep


from config.settings import settings
from pages.components.header import HeaderComponents
from pages.components.modals import ModalsComponent
from pages.catalog.listing_page import ListingPage


### ВАЖНО: метод клика по капче не работает: возвращает 200, но фактически она не прожимается
### (можно убедиться, воспроизводя сперва кейс с ошибками, а потом заполнение полей: под капчей сообщение об ошибке не исчезает)

@allure.feature('')
@allure.story('')
@pytest.mark.parametrize(
    'name, phone', [
        #('Данила', '79994231265'),
        ('Danila', '79994126523')
    ]
)
@pytest.mark.smoke
def test_callback_modal(browser, name, phone):
    """
    Проверить, что:
        По клику "Заказать звонок" открывается модалка с формой
        По клику кнопки "Отправить" под пустыми обязательными полями есть ошибки
        В поля "Ваше имя, Телефон, Капча(10.11 == НЕ РЕАЛИЗОВАЛ), Политика сайта" доступен ввод данных

    """
    header = HeaderComponents(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    #    1. Открыть сайт
    browser.get(settings.base_url)
    #    2. Открыть модалку с формой заказа звонка:
    (
        header.hover_phone()
        .click_call_request()
    )
    #    Проверка_1: По клику "Заказать звонок" открывается модалка с формой:
    assert modals.is_callback_modal_visible(), 'Модалка с формой заказа звонка не появилась'
    sleep(1)
    modals.click_submit_button()
    #    Проверка_2: По клику кнопки "Отправить" под пустыми обязательными полями есть ошибки:
    assert modals.check_error_message_name(), 'Под пустым полем "Ваше имя" нет сообщения с ошибкой: "Заполните это поле!"'
    assert modals.check_error_message_phone(), 'Под пустым полем "Телефон" нет сообщения с ошибкой: "Заполните это поле!"'
    assert modals.check_error_message_capcha(), 'Под пустым полем "Капча" нет сообщения с ошибкой: "Пройдите проверку"'
    assert modals.check_error_message_confidencial(), 'Под пустым полем "Согласие с политикой сайта" нет сообщения с ошибкой: "Пройдите проверку"'

    #   Проверка_3: В поля "Ваше имя, Телефон, Капча, Политика сайта" доступен ввод данных
    (
        modals.enter_name(name)
        .enter_phone(phone)
        #.click_captcha()
        #.click_confidentional()
    )
    sleep(1)

# @allure.feature('')
# @allure.story('')
# @pytest.mark.smoke
# def test_callback_modal(browser):
#     """
#     Проверить, что:
#         По клику "Заказать звонок" открывается модалка с формой
#
#     """
#
#     #    Предварительные шаги до начала тестирования:
#     header = HeaderComponents(browser)
#     listing = ListingPage(browser)
#
#     #    Предварительные шаги до начала тестирования
#     # 1. Перейти на страницу каталога
#     (
#         listing.open_page_category_with_sorting_filters()
#     )
#
#     # 2. Перейти на страницу каталога