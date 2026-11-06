import allure


from config.settings import settings
from pages.base_page import BasePage
from locators.product.product_locators import ProductLocators


class ProductPage(BasePage):
    """ Методы для страницы карточки товара """

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

    @allure.step('Метод клика по табу "Описание"')  # этот таб открыт на странице по умолчанию, так что не понадобится, возможно
    def click_tab_description(self):
        self.click(ProductLocators.TAB_DESCRIPTION)
        return self

    @allure.step('Метод проверки содержания таба "Описание"')
    def check_text_in_tab_description(self) -> bool:
        return self.is_visible(ProductLocators.CONTENT_TAB_DESCRIPTION)

    @allure.step('Метод клика по табу "Отзывы"')
    def click_tab_otz(self):
        self.click(ProductLocators.TAB_OTZ)
        return self

    @allure.step('Метод проверки содержания таба "Отзывы"')
    def check_text_in_tab_otz(self) -> bool:
        return self.is_visible(ProductLocators.CONTENT_TAB_OTZ)

    @allure.step('Метод клика по табу "Оплата"')
    def click_tab_opl(self):
        self.click(ProductLocators.TAB_OPL)
        return self

    @allure.step('Метод проверки содержания таба "Оплата"')
    def check_text_in_tab_opl(self) -> bool:
        return self.is_visible(ProductLocators.CONTENT_TAB_OPL)

    @allure.step('Метод клика по табу "Доставка"')
    def click_tab_dost(self):
        self.click(ProductLocators.TAB_DOST)
        return self

    @allure.step('Метод проверки содержания таба "Доставка"')
    def check_text_in_tab_dost(self) -> bool:
        return self.is_visible(ProductLocators.CONTENT_TAB_DOST)

    @allure.step('Метод клика по табу "Вопросы о товаре"')
    def click_tab_vopr(self):
        self.click(ProductLocators.TAB_VOPR)
        return self

    @allure.step('Метод проверки содержания таба "Вопросы о товаре"')
    def check_text_in_tab_vopr(self) -> bool:
        return self.is_visible(ProductLocators.CONTENT_TAB_VOPR)
