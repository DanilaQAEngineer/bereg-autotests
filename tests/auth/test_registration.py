import allure
import pytest


from config.settings import settings
from pages.base_page import BasePage
from pages.components.header import HeaderComponents
from pages.components.auth_modal import AuthModalComponent
from pages.auth.register_page import RegisterPage
from locators.components.auth_locators import LocatorsForAuthModal


@allure.feature('')
@allure.story('')
@pytest.mark.smoke
def test_open_registration_page(browser):
    """ Проверить, что ... """
    header = HeaderComponents(browser)
    auth = AuthModalComponent(browser)
    reg = RegisterPage(browser)

    browser.get(settings.base_url)  # Переходим на главную страницу сайта

    header.click_voity_button()  # Жмём кнопку "Войти" в хедере

    url_before_click_reg_btn = browser.current_url#; print(f'Ссылка до клика кнопки "Регистрация": {url_before_click_reg_btn}')
    auth.click_register_link()  # В модалке "Вход в личный кабинет" жмём кнопку "Регистрация"
    url_after_click_reg_btn = browser.current_url#; print(f'Ссылка после клика кнопки "Регистрация": {url_after_click_reg_btn}')

    assert url_before_click_reg_btn != url_after_click_reg_btn, 'Ссылка не изменилась'
    assert reg.is_breadcrumbs_visble(), 'Хлебных крошек на странице нет'
    page_title = reg.check_title_in_registration_page()#; print(f'Заголовок на странице раздела: {page_title}')
    assert "регистрация" in page_title.lower(), f'Ожидали заголовок про регистрация, получили: "{page_title}"'
