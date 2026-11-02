import allure
from selenium.webdriver.common.by import By


from pages.base_page import BasePage


class ProductCardComponent(BasePage):
    """ Компонент карточки товара в листинге (сетке товаров) """

    #    В реальном проекте локаторы кнопок внутри карточки лучше выносить локаторы компонента, а не отдельной страницей в locators
    BUTTON_ADD_CART_IN_FAVORITE = (By.CSS_SELECTOR, 'div.item-action.item-action--vertical.item-action--favorite')  # Локатор кнопки добавления товара в избранное
    BUTTON_ADD_CART_IN_COMPARE = (By.CSS_SELECTOR, 'div.item-action.item-action--vertical.item-action--compare')  # Локатор кнопки добавления товара в сравнение
    BUTTON_ADD_CART_IN_BASKET = (By.CSS_SELECTOR, 'span.btn.btn-default')    # Локатор кнопки добавления товара в корзину


    @allure.step('Метод клика по кнопке "В избранное" в карточке товара')
    def click_button_add_cart_in_favorite(self):
        self.click(self.BUTTON_ADD_CART_IN_FAVORITE)
        return self

    @allure.step('Метод клика по кнопке "В сравнение" в карточке товара')
    def click_button_add_cart_in_favorite(self):
        self.click(self.BUTTON_ADD_CART_IN_COMPARE)
        return self

    @allure.step('Метод клика по кнопке "В корзину" в карточке товара')
    def click_button_add_cart_in_favorite(self):
        self.click(self.BUTTON_ADD_CART_IN_BASKET)
        return self

