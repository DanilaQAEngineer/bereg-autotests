import pytest


from config.settings import settings
from pages.base_page import BasePage
from pages.components.header import HeaderComponents


@pytest.mark.smoke
def test_header_city_modal(browser):
    """Проверка, что по клику логотипа ведет на главную страницу"""

    # Предварительные шаги до начала тестирования:
    browser.get(f'{settings.base_url}/catalog/')     # Сперва открываю любую страницу
    header = HeaderComponents(browser)

    url_before_click_logo = browser.current_url#; print(f'\nURL`а до клика по лого: {url_before_click_logo}')

    header.click_logo()

    url_after_click_logo = browser.current_url#; print(f'URL`а после клика по лого: {url_after_click_logo}')

    assert url_before_click_logo != url_after_click_logo, 'УРЛ не изменился'
