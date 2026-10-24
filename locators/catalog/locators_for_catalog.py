from selenium.webdriver.common.by import By    # импортировали «способ поиска»: говорим Selenium, как искать элемент: == By.CSS_SELECTOR.XPATH.ID



class LocatorsForCatalogPage:
    CATALOG_BUTTON = (By.XPATH, '(//*[@class="header-menu__link--only-catalog fill-use-fff btn btn-default btn--no-rippple btn-lg"])[1]')
