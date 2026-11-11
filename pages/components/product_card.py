import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage
from locators.components.product_card_locators import LocatorsForProductCard


class ProductCardComponent(BasePage):
    """ Компонент карточки товара в листинге (сетке_странице раздела каталога) """

    ###    1) Методы проверки элементов

    @allure.step('Метод проверки появления на странице уведомления после успешного добавления товара в сравнение')
    def check_notification_after_added_in_compare(self) -> bool:
        return self.is_visible(LocatorsForProductCard.NOTIFICATION_AFTER_ADDED_IN_COMPARE)

    @allure.step('Метод проверки появления на странице уведомления после успешного добавления товара в избранное')
    def check_notification_after_added_in_favorite(self) -> bool:
        return self.is_visible(LocatorsForProductCard.NOTIFICATION_AFTER_ADDED_IN_FAVORITE)

    @allure.step('Метод проверки появления на странице уведомления после успешного добавления товара в корзину')
    def check_notification_after_added_in_basket(self) -> bool:
        return self.is_visible(LocatorsForProductCard.NOTIFICATION_AFTER_ADDED_IN_BASKET)

    ###    2) Методы действий с элементами

    @allure.step('Метод клика по кнопке "В сравнение" в карточке товара')
    def click_button_add_cart_in_compare(self):
        self.click(LocatorsForProductCard.IN_COMPARE_BUTTON)
        return self

    @allure.step('Метод клика по кнопке "В избранное" в карточке товара')
    def click_button_add_cart_in_favorite(self):
        self.click(LocatorsForProductCard.IN_FAVORITE_BUTTON)
        return self

    @allure.step('Метод клика по кнопке "В корзину" в карточке товара')
    def click_button_add_cart_in_basket(self):
        self.click(LocatorsForProductCard.IN_BASKET_BUTTON)
        return self

    @allure.step('Метод наведения курсора на фото карточки в листинге (нужно для появления кнопки "Быстрый просмотр")')
    def hover_img_for_get_quick_view_btn(self):
        element = self.find(LocatorsForProductCard.IMG_CARD)
        ActionChains(self.driver).move_to_element(element).perform()
        return self

    @allure.step('Метод клика по кнопке "Быстрый просмотр"')
    def click_quick_view(self):
        self.click(LocatorsForProductCard.BTN_FAST_WATCH)
        return self

    # МЕТОД ДЛЯ ТЕСТИРОВАНИЯ СТРАНИЦЫ КАРТОЧКИ ТОВАРА (СМЕЖНЫЙ МЕТОД ДЛЯ СКВОЗНОГО ТЕСТИРОВАНИЯ = ПЕРЕХОД В КАРТОЧКУ ЧЕРЕЗ КАТАЛОГ)
    @allure.step('Метод перехода в карточку первого товара на странице каталога')
    def open_first_card(self):
        self.click(LocatorsForProductCard.PRODUCT_NAME)
        return self

    # В LocatorsForListing добавь QUICK_VIEW_BTN (кнопка лупы/глаза на карточке)
