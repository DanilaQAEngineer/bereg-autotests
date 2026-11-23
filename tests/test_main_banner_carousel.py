import allure
import pytest


from config.settings import settings
from pages.main_page import MainPage
from locators.main_page_locators import LocatorsForMainPage


@allure.feature('Главная страница')
@allure.story('Баннерная карусель')
@pytest.mark.smoke
def test_banner_carousel_switch(browser):
    """ Проверка переключения баннеров на главной """
    main = MainPage(browser)

    #    Переходим на главную страницу сайта
    browser.get(settings.base_url)
