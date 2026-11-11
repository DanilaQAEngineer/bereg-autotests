import time

import allure
import pytest
from time import sleep


from config.settings import settings
from pages.components.header import HeaderComponents
from pages.components.modals import ModalsComponent
from pages.catalog.listing_page import ListingPage


### ВАЖНО: метод клика по капче не работает: возвращает 200 (тест проходит), но фактически она не прожимается
### (можно убедиться, воспроизводя сперва кейс с ошибками, а потом последовательное заполнение полей: под капчей сообщение об ошибке не исчезает)


@allure.feature('')
@allure.story('')
@pytest.mark.parametrize(
    'name, phone', [
        ('Данила', '79994231265'),
        ('Danila', '79994126523')
    ]
)
@pytest.mark.smoke
def test_callback_modal(browser, name, phone):
    """
    Проверить, что:
        По клику "Заказать звонок" на странице открывается модалка с формой заказа звонка
        По клику кнопки "Отправить" под пустыми обязательными полями есть ошибки
        В поля "Ваше имя, Телефон" доступен ввод данных, по полям "Капча (10.11 == НЕ РЕАЛИЗОВАЛ), Политика сайта" дуступен клик

    """
    header = HeaderComponents(browser)
    modals = ModalsComponent(browser)

    #        Предварительные шаги до начала тестирования:
    browser.get(settings.base_url)  # 1. Открыть сайт
    (
        header.hover_phone()  # 2. Навести курсор на номер телефона в хедере
        .click_call_request()  # 3. Нажать кнопку "Заказать звонок" в открывшемся дропдауне
    )

    #    Проверка_1: По клику "Заказать звонок" на странице открывается модалка с формой заказа звонка:
    assert modals.is_callback_modal_visible(), 'Модалка с формой заказа звонка не появилась'

    modals.click_submit_button()

    #    Проверка_2: По клику кнопки "Отправить" под пустыми обязательными полями есть ошибки:
    assert modals.check_error_message_name(), 'Под пустым полем "Ваше имя" нет сообщения с ошибкой: "Заполните это поле!"'
    assert modals.check_error_message_phone(), 'Под пустым полем "Телефон" нет сообщения с ошибкой: "Заполните это поле!"'
    assert modals.check_error_message_capcha(), 'Под пустым полем "Капча" нет сообщения с ошибкой: "Пройдите проверку"'
    assert modals.check_error_message_confidencial(), 'Под пустым полем "Согласие с политикой сайта" нет сообщения с ошибкой: "Согласитесь с условиями"'

    #   Проверка_3: В поля "Ваше имя, Телефон" доступен ввод данных, по полям "Капча (10.11 == НЕ РЕАЛИЗОВАЛ), Политика сайта" дуступен клик
    (
        modals.enter_name(name)
        .enter_phone(phone)
        #.click_captcha()
        #.click_confidentional()
    )


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_quick_view_modal(browser):
    """
    Проверить, что:
        1. По клику "Быстрый просмотр" открывается модалка
        2. Есть заголовок с названием товара
        По клику кнопки "В корзину" появляются:
            уведомление об успешности добавления товара в корзину
        По клику кнопки "Сравнить" появляются:
            уведомление об успешности добавления товара в сравнение
        По клику кнопки "В избранное" появляются:
            уведомление об успешности добавления товара в избранное

    """

    header = HeaderComponents(browser)
    listing = ListingPage(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # 1. Перейти на страницу каталога
        .product_card.hover_img_for_get_quick_view_btn()  # 2. Навести курсор на фото карточки товара
        .click_quick_view()  # 3. Кликнуть на появившуюся кнопку "Быстрый просмотр"
    )
    #    1. По клику "Быстрый просмотр" открывается модалка
    assert modals.is_quick_view_modal_visible(), 'Модалка "Быстрый просмотр" не появилась на странице'
    #    2. Есть заголовок с названием товара
    title_in_modal_quick_view = modals.check_title_in_modal_quick_view()
    print(f'Заголовок в названии модалки: {title_in_modal_quick_view}')
    assert title_in_modal_quick_view, 'В модалке "Быстрый просмотр" нет заголовка с названием товара'
