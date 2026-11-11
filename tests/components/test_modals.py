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
        1. По клику кнопки "Быстрый просмотр" поверх страницы открывается модалка "Быстрый просмотр"
        2. В открывшейся модалке есть:
            Заголовок с названием товара
            Кнопки "Закрытие модалки, В избранное/сравнение/корзину, Купить в 1 клик, Подробнее о товаре, Следующий/Предыдущий товар"
        3. По клику на:
            3.1 Название карточки редиректит на страницу карточки этого товара
            3.2 Кнопку "В избранное" появляется уведомление об успешности добавления товара в избранное
            3.3 Кнопку "В сравнение" появляется уведомление об успешности добавления товара в сравнение
            3.4 Кнопку "В корзину" появляется уведомление об успешности добавления товара в корзину (появляются кнопки "- 1 +")
            3.5 Кнопку "Купить в 1 клик" открывается модалка "Купить в 1 клик"
            3.6 Кнопку "Подробнее о товаре" редиректит на страницу карточки этого товара
            3.7 По клику "Х" модалка закрывается
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
    #    1. По клику кнопки "Быстрый просмотр" поверх страницы открывается модалка "Быстрый просмотр"
    assert modals.is_quick_view_modal_visible(), 'Модалка "Быстрый просмотр" не появилась на странице'
    #    2. В открывшейся модалке есть: Заголовок с названием товара, Кнопки "Закрытие модалки, В избранное/сравнение/корзину, Купить в 1 клик, Подробнее о товаре, Следующий/Предыдущий товар"
    assert modals.check_title_in_modal_quick_view(), 'В модалке "Быстрый просмотр" нет заголовка с названием товара'
    assert modals.check_button_in_favorite_in_modal_quick_view(), 'В модалке "Быстрый просмотр" нет кнопки "В избранное'
    assert modals.check_button_in_compare_in_modal_quick_view(), 'В модалке "Быстрый просмотр" нет кнопки "В сравнение'
    assert modals.check_button_in_basket_in_modal_quick_view(), 'В модалке "Быстрый просмотр" нет кнопки "В корзину'
    assert modals.check_button_bye_in_one_click_in_modal_quick_view(), 'В модалке "Быстрый просмотр" нет кнопки "Купить в 1 клик'
    assert modals.check_button_close_modal_quick_view(), 'В модалке "Быстрый просмотр" нет кнопки закрытия модалки'
    assert modals.is_button_prev_btn_visible(), 'В модалке "Быстрый просмотр" нет кнопки предыдущий товар'
    assert modals.is_button_next_btn_visible(), 'В модалке "Быстрый просмотр" нет кнопки следующий товар'

    #    По клику на: 3.1 Название карточки редиректит на страницу карточки этого товара
    url_before_click_title_card = browser.current_url
    modals.click_title_in_modal_quick_view()
    url_after_click_title_card = browser.current_url

    assert url_before_click_title_card != url_after_click_title_card, 'URL не изменился после клика по названию карточки'
    browser.back()  # (вернуться на страницу каталога)
    #    Постусловие: возвращаемся на страницу каталога и повторно кликаем "Быстрый просмотр"
    (
        listing.product_card.hover_img_for_get_quick_view_btn()  # Повторно навести курсор на фото карточки товара
        .click_quick_view() # Повторно кликнуть на появившуюся кнопку "Быстрый просмотр"
    )

    #    По клику на: 3.4 Кнопку "В корзину" появляется уведомление об успешности добавления товара в корзину (появляются кнопки "- 1 +")
    modals.click_btn_in_basket_in_modal_quick_view()
    assert listing.product_card.check_notification_after_added_in_basket(), 'Уведомление об успешности добавления товара в корзину не появилось'

    #    По клику на: 3.6 Кнопку "Подробнее о товаре" редиректит на страницу карточки этого товара
    url_before_click_btn_detailed = browser.current_url
    modals.click_btn_detailed_in_modal_quick_view()
    url_after_click_btn_detailed = browser.current_url

    assert url_before_click_btn_detailed != url_after_click_btn_detailed, 'URL не изменился после клика по кнопке "Подробнее о товаре"'
    browser.back()  # (вернуться на страницу каталога)
    #    Постусловие: возвращаемся на страницу каталога и повторно кликаем "Быстрый просмотр"
    (
        listing.product_card.hover_img_for_get_quick_view_btn()  # Повторно навести курсор на фото карточки товара
        .click_quick_view()  # Повторно кликнуть на появившуюся кнопку "Быстрый просмотр"
    )