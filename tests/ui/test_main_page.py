import time

import allure
import pytest


from config.settings import settings
from pages.main_page import MainPage
from locators.main_page_locators import LocatorsForMainPage


@allure.feature('Главная страница')
@allure.story('Баннерная карусель')
@pytest.mark.smoke
def test_click_btn_next_banner_in_carousel(browser):
    """ Проверить, что на главной странице в баннероной карусели можно переключиться на следующий баннер """
    main = MainPage(browser)
    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    #    Предварительный шаг: Запоминаем ссылку текущего баннера
    href_before_click_next_btn = main.get_current_banner_href()#; print(f'\nСсылка ДО переключения баннера: {href_before_click_next_btn}')
    assert href_before_click_next_btn, "Не удалось получить ссылку начального баннера"

    #    1.1. Кликаем кнопку ">" (следующий слайд/баннер)
    main.click_next_banner()

    #    1.2. Проверяем, что ссылка изменилась (слайд действительно переключился)
    href_after_click_next_btn = main.get_current_banner_href()#; print(f'Ссылка ПОСЛЕ переключения баннера: {href_after_click_next_btn}')
    assert href_before_click_next_btn != href_after_click_next_btn, f'Баннер не переключился: ссылка ДО ({href_before_click_next_btn}) == ссылке ПОСЛЕ ({href_after_click_next_btn})'


@allure.feature('Главная страница')
@allure.story('Баннерная карусель')
@pytest.mark.smoke
def test_click_btn_prev_banner_in_carousel(browser):
    """ Проверить, что на главной странице в баннероной карусели можно переключиться на предыдущий баннер """
    main = MainPage(browser)
    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    #    Предварительный шаг: Переключаемся на следующий баннер и запоминаем его ссылку баннера
    href_before_click_prev_btn = main.get_current_banner_href()#; print(f'\nСсылка ДО переключения баннера: {href_before_click_prev_btn}')
    assert href_before_click_prev_btn, "Не удалось получить ссылку начального баннера"

    #    2.1. Кликаем кнопку ">" (следующий слайд/баннер)
    main.click_prev_banner()

    #    2.2. Проверяем, что ссылка изменилась (слайд действительно переключился)
    href_after_click_prevt_btn = main.get_current_banner_href()#; print(f'Ссылка ПОСЛЕ переключения баннера: {href_after_click_prevt_btn}')
    assert href_before_click_prev_btn != href_after_click_prevt_btn, f'Баннер не переключился: ссылка ДО ({href_after_click_prevt_btn}) == ссылке ПОСЛЕ ({href_after_click_prevt_btn})'


@allure.feature('Главная страница')
@allure.story('Блок "Бестселлеры"')
@pytest.mark.smoke
def test_open_catalog_page_after_click_title_in_bestseller_block(browser):
    """ Проверить клик по заголовку в блоке "Бестселлеры" открывается страница каталога"""
    main = MainPage(browser)
    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    main.click_element(LocatorsForMainPage.TITLE_BESTSELLER)
    assert "/catalog/" in browser.current_url, f'Переход на страницу каталога не произошел, текущий URL: {browser.current_url}'


@allure.feature('Главная страница')
@allure.story('Блок "Бестселлеры"')
@pytest.mark.parametrize(
    'filter_locator, tag_name, filter_name',  # tag_name -- что ожидаю увидеть в тэгах
    [
        (LocatorsForMainPage.FILTER_HIT, 'хи', 'Фильтр "Хит"'),
        (LocatorsForMainPage.FILTER_RECOMMEND, 'совет', 'Фильтр "Советуем"'),
        (LocatorsForMainPage.FILTER_NEW, 'нови', 'Фильтр "Новинка"'),
        (LocatorsForMainPage.FILTER_STOCK, 'акци', 'Фильтр "Акция"')
    ]
)
@pytest.mark.smoke
def test_filters_in_bestseller_block(browser, filter_locator, tag_name, filter_name):
    """ Проверить, что после применения фильтра в карточках есть теги с соответствующими названиями """
    main = MainPage(browser)
    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    #    Собираем названия товаров ДО фильтрации:
    tags_before_click_filter = main.get_tags_in_blocks(LocatorsForMainPage.TAG_IN_CARD_LISTING_BESTSELLER)#; print(f'\nТэги карточек товаров ДО фильтрации: {tags_before_click_filter}')

    #    Применяем фильтр:
    main.click_element(filter_locator)
    time.sleep(2)  # Жду, когда подтянутся карточки, соответствующие параметру фильтра

    #    Собираем теги товаров ПОСЛЕ фильтрации:
    tags_after_click_filter = main.get_tags_in_blocks(LocatorsForMainPage.TAG_IN_CARD_LISTING_BESTSELLER)#; print(f'Тэги карточек товаров ПОСЛЕ фильтрации: {tags_after_click_filter}')

    #    Объединяем все названия в одну строку для простоты поиска:
    all_tags_text = " ".join(tags_after_click_filter).lower()

    #    Проверяем, что хотя бы одно название содержит ключевое слово:
    assert tag_name in all_tags_text, f'Фильтр "{filter_name}" не сработал. В тэгах товаров не найдено слова "{tag_name}". Названия: {tags_after_click_filter}'


@allure.feature('Главная страница')
@allure.story('Блок "Палатки и походные печи"')
@pytest.mark.smoke
def test_open_catalog_page_after_click_title_in_pechi_block(browser):
    """ Проверить клик по заголовку в блоке "Палатки и походные печи" открывается страница каталога"""
    main = MainPage(browser)
    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    main.click_element(LocatorsForMainPage.TITLE_PECHI)
    assert "/catalog/pokhodnye-pechi/" in browser.current_url, f'Переход на страницу каталога не произошел, текущий URL: {browser.current_url}'


@allure.feature('Главная страница')
@allure.story('Блок "Палатки и походные печи"')
@pytest.mark.parametrize(
    'filter_locator, keyword, filter_name',  # keyword -- что ожидаю увидеть в названиях карточек
    [
        (LocatorsForMainPage.FILTER_ARM_PALATKI, 'армейск', 'Фильтр "Армейские палатки"'),
        (LocatorsForMainPage.FILTER_BANI, '-бан', 'Фильтр "Походные бани"'),
        (LocatorsForMainPage.FILTER_PECHI, 'печ', 'Фильтр "Походные печи"'),
        (LocatorsForMainPage.FILTER_PALATKI, 'палатк', 'Фильтр "Палатки"')
    ]
)
@pytest.mark.smoke
def test_filters_in_pechi_block(browser, filter_locator, keyword, filter_name):
    """ Проверить, что после применения фильтров в карточках присутствуют товары с соответствующими названиями """
    main = MainPage(browser)
    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    #    Собираем названия товаров ДО фильтрации:
    titles_before_click_filters = main.get_product_titles_in_block(LocatorsForMainPage.TITLE_IN_CARD_LISTING_PECHI); print(f'\nНазвания карточек товаров до фильтрации: {titles_before_click_filters}')
    #    Применяем фильтр:
    main.click_element(filter_locator)
    time.sleep(2)  # Жду, когда подтянутся карточки, соответствующие параметру фильтра

    #    Собираем названия товаров ПОСЛЕ фильтрации:
    titles_after_click_filters = main.get_product_titles_in_block(LocatorsForMainPage.TITLE_IN_CARD_LISTING_PECHI); print(f'Названия карточек товаров после фильтрации: {titles_after_click_filters}')

    #    Объединяем все названия в одну строку для простоты поиска:
    all_titles_text = " ".join(titles_after_click_filters).lower()

    #    Проверяем, что хотя бы одно название содержит ключевое слово:
    assert keyword in all_titles_text, f'Фильтр "{filter_name}" не сработал. В названиях товаров не найдено слова "{keyword}". Названия: {titles_after_click_filters}'
