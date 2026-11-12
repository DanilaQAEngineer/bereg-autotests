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
@pytest.mark.smoke
def test_check_errors_empty_inputs_callback_modal(browser):
    """
    Проверить, что:
        По клику "Заказать звонок" на странице открывается модалка с формой заказа звонка
        По клику кнопки "Отправить" под пустыми обязательными полями есть ошибки
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


@allure.feature('')
@allure.story('')
@pytest.mark.parametrize(
    'name, phone', [
        ('Данила', '79994231265'),
        ('Danila', '79994126523')
    ]
)
@pytest.mark.smoke
def test_enter_data_in_inputs_callback_modal(browser, name, phone):
    """
    Проверить, что:
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

    #   Проверка: В поля "Ваше имя, Телефон" доступен ввод данных, по полям "Капча (10.11 == НЕ РЕАЛИЗОВАЛ), Политика сайта" дуступен клик
    (
        modals.enter_name(name)
        .enter_phone(phone)
        #.click_captcha()
        .click_confidential_checkbox()
    )


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_check_visible_elements_quick_view_modal(browser):
    """
    Проверить, что:
        1. По клику кнопки "Быстрый просмотр" поверх страницы открывается модалка "Быстрый просмотр"
        2. В открывшейся модалке есть:
            2.1 Заголовок с названием товара
            2.2 Кнопка "Закрытие модалки"
            2.3 Кнопка "В избранное"
            2.4 Кнопка "В сравнение"
            2.5 Кнопка "В корзину"
            2.6 Кнопка "Купить в 1 клик"
            2.7 Кнопка "Подробнее о товаре"
            2.8 Кнопка "Следующий товар"
            2.9 Кнопка "Предыдущий товар"
    """
    listing = ListingPage(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # 1. Перейти на страницу каталога
        .product_card.hover_img_for_get_quick_view_btn()  # 2. Навести курсор на фото карточки товара
        .click_quick_view()  # 3. Кликнуть на появившуюся кнопку "Быстрый просмотр"
    )
    #    1. По клику кнопки "Быстрый просмотр" поверх страницы открывается модалка "Быстрый просмотр"
    assert modals.is_quick_view_modal_visible(), 'Модалка "Быстрый просмотр" не появилась на странице'
    #    2. В открывшейся модалке есть:
    assert modals.check_title_in_modal_quick_view(), 'В модалке "Быстрый просмотр" нет заголовка с названием товара'  # 2.1 Заголовок с названием товара
    assert modals.check_button_close_modal_quick_view(), 'В модалке "Быстрый просмотр" нет кнопки закрытия модалки'  # 2.2 Кнопка "Закрытие модалки"
    assert modals.check_button_in_favorite_in_modal_quick_view(), 'В модалке "Быстрый просмотр" нет кнопки "В избранное'  # 2.3 Кнопка "В избранное"
    assert modals.check_button_in_compare_in_modal_quick_view(), 'В модалке "Быстрый просмотр" нет кнопки "В сравнение'  # 2.4 Кнопка "В сравнение"
    assert modals.check_button_in_basket_in_modal_quick_view(), 'В модалке "Быстрый просмотр" нет кнопки "В корзину'  # 2.5 Кнопка "В корзину"
    assert modals.check_button_bye_in_one_click_in_modal_quick_view(), 'В модалке "Быстрый просмотр" нет кнопки "Купить в 1 клик"'  # 2.6 Кнопка "Купить в 1 клик"
    assert modals.is_button_detailed_visible(), 'В модалке "Быстрый просмотр" нет кнопки "Подробнее о товаре"'  # 2.7 Кнопка "Подробнее о товаре"
    assert modals.is_button_next_btn_visible() and modals.is_button_prev_btn_visible(), 'В модалке "Быстрый просмотр" нет кнопок "Следующий/Предыдущий товар"'  # 2.8_9 Кнопка "Следующий/Предыдущий товар"


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_click_title_quick_view_modal(browser):
    """
    Проверить, что:
        по клику на название карточки редиректит на страницу карточки этого товара
    """
    listing = ListingPage(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # 1. Перейти на страницу каталога
        .product_card.hover_img_for_get_quick_view_btn()  # 2. Навести курсор на фото карточки товара
        .click_quick_view()  # 3. Кликнуть на появившуюся кнопку "Быстрый просмотр"
    )
    #    по клику на: 1.1 Название карточки редиректит на страницу карточки этого товара
    url_before_click_title_card = browser.current_url
    modals.click_title_in_modal_quick_view()
    url_after_click_title_card = browser.current_url

    assert url_before_click_title_card != url_after_click_title_card, 'URL не изменился после клика по названию карточки'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_click_detailed_btn_quick_view_modal(browser):
    """
    Проверить, что:
        по клику кнопки "Подробнее о товаре" редиректит на страницу карточки этого товара
    """
    listing = ListingPage(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # 1. Перейти на страницу каталога
        .product_card.hover_img_for_get_quick_view_btn()  # 2. Навести курсор на фото карточки товара
        .click_quick_view()  # 3. Кликнуть на появившуюся кнопку "Быстрый просмотр"
    )
    #    1. По клику на: 1.1 Название карточки редиректит на страницу карточки этого товара
    url_before_click_detailed_btn = browser.current_url
    modals.click_btn_detailed_in_modal_quick_view()
    url_after_click_detailed_btn = browser.current_url

    assert url_before_click_detailed_btn != url_after_click_detailed_btn, 'URL не изменился после клика кнопки "Подробнее о товаре"'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_click_bye_in_one_click_btn_quick_view_modal(browser):
    """
    Проверить, что:
        по клику кнопки "Купить в 1 клик" открывается модалка "Купить в 1 клик"
    """
    listing = ListingPage(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # 1. Перейти на страницу каталога
        .product_card.hover_img_for_get_quick_view_btn()  # 2. Навести курсор на фото карточки товара
        .click_quick_view()  # 3. Кликнуть на появившуюся кнопку "Быстрый просмотр"
    )
    #    по клику кнопки "Купить в 1 клик" открывается модалка "Купить в 1 клик"
    modals.click_btn_bye_in_one_click_in_modal_quick_view()

    assert modals.is_bye_in_one_click_modal_visible(), 'Модалка "Купить в 1 клик" не появилась на странице'
    assert modals.check_title_in_modal_bye_in_one_click(), 'В модалке "Купить в 1 клик" нет заголовка с названием модалки'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_click_in_favorite_btn_quick_view_modal(browser):
    """
    Проверить, что:
        по клику кнопки "В избранное" появляется уведомление об успешности добавления товара в избранное
    """
    listing = ListingPage(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # 1. Перейти на страницу каталога
        .product_card.hover_img_for_get_quick_view_btn()  # 2. Навести курсор на фото карточки товара
        .click_quick_view()  # 3. Кликнуть на появившуюся кнопку "Быстрый просмотр"
    )

    #    по клику кнопки "В избранное" появляется уведомление об успешности добавления товара в избранное
    modals.click_btn_in_favorite_in_modal_quick_view()

    assert listing.product_card.check_notification_after_added_in_favorite(), 'Уведомления об успешности добавления товара в избранное не появилось'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_click_in_compare_btn_quick_view_modal(browser):
    """
    Проверить, что:
        по клику кнопки "В сравнение" появляется уведомление об успешности добавления товара в сравнение
    """
    listing = ListingPage(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # 1. Перейти на страницу каталога
        .product_card.hover_img_for_get_quick_view_btn()  # 2. Навести курсор на фото карточки товара
        .click_quick_view()  # 3. Кликнуть на появившуюся кнопку "Быстрый просмотр"
    )

    #    по клику кнопки "В сравнение" появляется уведомление об успешности добавления товара в сравнение
    modals.click_btn_in_compare_in_modal_quick_view()

    assert listing.product_card.check_notification_after_added_in_compare(), 'Уведомления об успешности добавления товара в сравнение не появилось'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_click_in_basket_btn_quick_view_modal(browser):
    """
    Проверить, что:
        по клику кнопки "В корзину" появляется уведомление об успешности добавления товара в корзину + кнопка меняется на "- 1 +"
    """
    listing = ListingPage(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # 1. Перейти на страницу каталога
        .product_card.hover_img_for_get_quick_view_btn()  # 2. Навести курсор на фото карточки товара
        .click_quick_view()  # 3. Кликнуть на появившуюся кнопку "Быстрый просмотр"
    )

    #    по клику кнопки "В корзину" появляется уведомление об успешности добавления товара в корзину + кнопка меняется на "- 1 +"
    modals.click_btn_in_basket_in_modal_quick_view()

    assert listing.product_card.check_notification_after_added_in_basket(), 'Уведомления об успешности добавления товара в корзину не появилось'
    assert modals.check_button_after_added_card_in_basket(), 'Кнопка не поменялась на "- 1 +"'


@allure.feature('')
@allure.story('')
@pytest.mark.skip
def test_click_next_card_quick_view_modal(browser):    ### ПОКА ЧТО ПАДАЕТ: там сейчас бесконечный лоадер крутится)
    """
    Проверить, что:
        по клику кнопки ">" отображается карточка следующего товара
    """
    listing = ListingPage(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # 1. Перейти на страницу каталога
        .product_card.hover_img_for_get_quick_view_btn()  # 2. Навести курсор на фото карточки товара
        .click_quick_view()  # 3. Кликнуть на появившуюся кнопку "Быстрый просмотр"
    )

    #    по клику кнопки ">" отображается карточка следующего товара

    title_before_click_next_card_btn = modals.check_title_in_modal_quick_view(); print(f'Название в модалке ДО клика >: {title_before_click_next_card_btn}')
    modals.click_btn_next_card_visible()
    title_after_click_next_card_btn = modals.check_title_in_modal_quick_view(); print(f'Название в модалке ПОСЛЕ клика >: {title_after_click_next_card_btn}')

    assert title_before_click_next_card_btn != title_after_click_next_card_btn, 'В модалке отображается карточка того же товара, что и до клика кнопки >'


@allure.feature('')
@allure.story('')
@pytest.mark.skip
def test_click_perv_card_quick_view_modal(browser):    ### ПОКА ЧТО ПАДАЕТ: там сейчас бесконечный лоадер крутится)
    """
    Проверить, что:
        по клику кнопки "<" отображается карточка предыдущего товара
    """
    listing = ListingPage(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # 1. Перейти на страницу каталога
        .product_card.hover_img_for_get_quick_view_btn()  # 2. Навести курсор на фото карточки товара
        .click_quick_view()  # 3. Кликнуть на появившуюся кнопку "Быстрый просмотр"
    )

    #    по клику кнопки "<" отображается карточка предыдущего товара

    title_before_click_perv_card_btn = modals.check_title_in_modal_quick_view(); print(f'Название в модалке ДО клика >: {title_before_click_perv_card_btn}')
    modals.click_btn_prev_card_visible()
    title_after_click_perv_card_btn = modals.check_title_in_modal_quick_view(); print(f'Название в модалке ПОСЛЕ клика >: {title_after_click_perv_card_btn}')

    assert title_before_click_perv_card_btn != title_after_click_perv_card_btn, 'В модалке отображается карточка того же товара, что и до клика кнопки <'


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_click_btn_close_quick_view_modal(browser):
    """
    Проверить, что:
        по клику кнопки "Х" модалка закрывается
    """
    listing = ListingPage(browser)
    modals = ModalsComponent(browser)

    #    Предварительные шаги до начала тестирования:
    (
        listing.open_page_category_with_sorting_filters()  # 1. Перейти на страницу каталога
        .product_card.hover_img_for_get_quick_view_btn()  # 2. Навести курсор на фото карточки товара
        .click_quick_view()  # 3. Кликнуть на появившуюся кнопку "Быстрый просмотр"
    )

    #    по клику кнопки "Х" модалка закрывается
    (
        modals.click_btn_close_in_modal_quick_view()
        .wait_for_quick_view_modal_to_close()  # Жду, когда модалка полностью исчезнет со страницы
    )
    assert not modals.is_quick_view_modal_visible(), 'Модалка "Быстрый просмотр" не закрылась'
