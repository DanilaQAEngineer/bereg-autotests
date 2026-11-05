import allure


from config.settings import settings
from pages.base_page import BasePage
from locators.product.product_locators import ProductLocators


class ProductPage(BasePage):
    """ Методы на странице карточки товара """

    # @allure.step('Метод открытия карточки товара по прямой ссылке')    # Реализовал путём добавления метода перехода в карточку в ProductCardComponent
    # def open_directly(self, url: str):
    #     self.driver.get(f'{settings.base_url}{url}')
    #     return self

    @allure.step('Метод получения_проверки заголовка карточки товара')
    def get_title_card(self) -> str:
        return self.get_text(ProductLocators.TITLE_CARD)

    @allure.step('Метод проверки наличия хлебных крошек на странице карточки товара')
    def check_breadcrumbs(self) -> bool:
        return self.is_visible(ProductLocators.BREADCRUMBS)

    @allure.step('Метод клика по табу "Описание"')    # этот таб открыт на странице по умолчанию, так что не понадобится, возможно
    def click_tab_description(self):
        self.click(ProductLocators.TAB_DESCRIPTION)
        return self

    @allure.step('Метод клика кнопки "В корзину"')
    def click_button_in_basket(self):
        self.click(ProductLocators.BTN_IN_BASKET)
        return self

    @allure.step('Метод проверки наличия уведомления об успешности добавления товара в корзину')
    def check_notification_after_added_card_in_basket(self) -> bool:
        return self.is_visible(ProductLocators.NOTIFICATION_AFTER_ADD_BASKET)

    @allure.step('Метод проверки заголовка "В корзине" в уведомлении')
    def check_title_in_notification(self) -> str:
        return self.get_text(ProductLocators.TITLE_NOTIFICATION_AFTER_ADD_BASKET)

    @allure.step('Метод проверки названия товара в уведомлении')
    def check_name_card_in_notification(self) -> str:
        return self.get_text(ProductLocators.TEXT_NOTIFICATION_AFTER_ADD_BASKET)
