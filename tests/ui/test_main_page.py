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
    href_before_click_next_btn = main.get_current_banner_href(); print(f'\nСсылка ДО переключения баннера: {href_before_click_next_btn}')
    assert href_before_click_next_btn, "Не удалось получить ссылку начального баннера"

    #    1.1. Кликаем кнопку ">" (следующий слайд/баннер)
    main.click_next_banner()

    #    1.2. Проверяем, что ссылка изменилась (слайд действительно переключился)
    href_after_click_next_btn = main.get_current_banner_href(); print(f'Ссылка ПОСЛЕ переключения баннера: {href_after_click_next_btn}')
    assert href_before_click_next_btn != href_after_click_next_btn, f'Баннер не переключился: ссылка ДО ({href_before_click_next_btn}) == ссылке ПОСЛЕ ({href_after_click_next_btn})'


@allure.feature('Главная страница')
@allure.story('Баннерная карусель')
@pytest.mark.smoke
def test_click_btn_prev_banner_in_carousel(browser):
    """ Проверить, что на главной странице в баннероной карусели можно переключиться на предыдущий баннер """
    main = MainPage(browser)
    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    #    Предварительный шаг: Запоминаем ссылку текущего баннера
    href_before_click_prev_btn = main.get_current_banner_href(); print(f'\nСсылка ДО переключения баннера: {href_before_click_prev_btn}')
    assert href_before_click_prev_btn, "Не удалось получить ссылку начального баннера"

    #    2.1. Кликаем кнопку ">" (следующий слайд/баннер)
    main.click_prev_banner()

    #    2.2. Проверяем, что ссылка изменилась (слайд действительно переключился)
    href_after_click_prevt_btn = main.get_current_banner_href(); print(f'Ссылка ПОСЛЕ переключения баннера: {href_after_click_prevt_btn}')
    assert href_before_click_prev_btn != href_after_click_prevt_btn, f'Баннер не переключился: ссылка ДО ({href_after_click_prevt_btn}) == ссылке ПОСЛЕ ({href_after_click_prevt_btn})'
