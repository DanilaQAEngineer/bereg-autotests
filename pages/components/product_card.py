import allure
from selenium.webdriver.common.by import By


from pages.base_page import BasePage


class ProductCardComponent(BasePage):
    """ Компонент карточки товара в листинге (сетке_странице товаров) """

    #    В реальном проекте локаторы кнопок внутри карточки лучше выносить локаторы компонента, а не отдельной страницей в locators
    IN_FAVORITE_BUTTON = (By.CSS_SELECTOR, 'div.item-action--favorite')  # Локатор кнопки добавления товара в избранное
    IN_COMPARE_BUTTON = (By.CSS_SELECTOR, 'div.item-action--compare')  # Локатор кнопки добавления товара в сравнение
    IN_BASKET_BUTTON = (By.CSS_SELECTOR, 'span.item-action--basket')    # Локатор кнопки добавления товара в корзину


    @allure.step('Метод клика по кнопке "В избранное" в карточке товара')
    def click_button_add_cart_in_favorite(self):
        self.click(self.IN_FAVORITE_BUTTON)
        return self

    @allure.step('Метод клика по кнопке "В сравнение" в карточке товара')
    def click_button_add_cart_in_favorite(self):
        self.click(self.IN_COMPARE_BUTTON)
        return self

    @allure.step('Метод клика по кнопке "В корзину" в карточке товара')
    def click_button_add_cart_in_favorite(self):
        self.click(self.IN_BASKET_BUTTON)
        return self
