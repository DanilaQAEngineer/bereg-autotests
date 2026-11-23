import allure
import pytest


from config.settings import settings
from pages.main_page import MainrPage
from locators.main_page_locators import LocatorsForMainPage


@allure.feature('Главная страница')
@allure.story('Баннерная карусель')
@pytest.mark.smoke
def test_check_subscribes_in_footer(browser):
    """ Проверить, что (Берем ссылку активного баннера -> жмем → -> ждем, пока ссылка изменится -> проверяем, что она стала другой) """
    main = MainrPage(browser)

    #    Переходим на главную страницу сайта
    browser.get(settings.base_url)