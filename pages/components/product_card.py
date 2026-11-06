import allure
from selenium.webdriver.common.by import By


from pages.base_page import BasePage


class ProductCardComponent(BasePage):
    """ Компонент карточки товара в листинге (сетке_странице раздела каталога) """

    #    В реальном проекте локаторы кнопок внутри карточки лучше выносить локаторы компонента, а не отдельной страницей в locators
    IN_FAVORITE_BUTTON = (By.CSS_SELECTOR, 'div.item-action--favorite')  # Локатор кнопки добавления товара в избранное
    IN_COMPARE_BUTTON = (By.CSS_SELECTOR, 'div.item-action--compare')  # Локатор кнопки добавления товара в сравнение
    IN_BASKET_BUTTON = (By.CSS_SELECTOR, 'span.item-action--basket')    # Локатор кнопки добавления товара в корзину

    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.catalog-item a.dark_link')  # Локатор названия карточки (для дальнейшего перехода карточку товара)

    NOTIFICATION_AFTER_ADDED_IN_COMPARE = (By.CSS_SELECTOR, 'div.notice--link')    # Уведомление после успешного добавления товара в сравнение (сам его див)
    NOTIFICATION_AFTER_ADDED_IN_FAVORITE = (By.CSS_SELECTOR, 'div.notice__inner')    # Уведомление после успешного добавления товара в избранное (сам его див)
    NOTIFICATION_AFTER_ADDED_IN_BASKET = (By.CSS_SELECTOR, 'div.notice__inner')    # Уведомление после успешного добавления товара в корзину (сам его див)


    @allure.step('Метод клика по кнопке "В сравнение" в карточке товара')
    def click_button_add_cart_in_compare(self):
        self.click(self.IN_COMPARE_BUTTON)
        return self

    @allure.step('Метод проверки появления на странице уведомления после успешного добавления товара в сравнение')
    def check_notification_after_added_in_compare(self) -> bool:
        return self.is_visible(self.NOTIFICATION_AFTER_ADDED_IN_COMPARE)

    @allure.step('Метод клика по кнопке "В избранное" в карточке товара')
    def click_button_add_cart_in_favorite(self):
        self.click(self.IN_FAVORITE_BUTTON)
        return self

    @allure.step('Метод проверки появления на странице уведомления после успешного добавления товара в избранное')
    def check_notification_after_added_in_favorite(self) -> bool:
        return self.is_visible(self.NOTIFICATION_AFTER_ADDED_IN_FAVORITE)

    @allure.step('Метод клика по кнопке "В корзину" в карточке товара')
    def click_button_add_cart_in_basket(self):
        self.click(self.IN_BASKET_BUTTON)
        return self

    @allure.step('Метод проверки появления на странице уведомления после успешного добавления товара в корзину')
    def check_notification_after_added_in_basket(self) -> bool:
        return self.is_visible(self.NOTIFICATION_AFTER_ADDED_IN_BASKET)

    # МЕТОД ДЛЯ ТЕСТИРОВАНИЯ СТРАНИЦЫ КАРТОЧКИ ТОВАРА (СМЕЖНЫЙ МЕТОД ДЛЯ СКВОЗНОГО ТЕСТИРОВАНИЯ = ПЕРЕХОД В КАРТОЧКУ ЧЕРЕЗ КАТАЛОГ)
    @allure.step('Метод перехода в карточку первого товара на странице каталога')
    def open_first_card(self):
        self.click(self.PRODUCT_NAME)
        return self
