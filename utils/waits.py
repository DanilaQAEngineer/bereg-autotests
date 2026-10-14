# Файл нужен для обёртки над WebDriverWait. Все POM будут их использовать — не дублировать в каждом


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import settings


def wait_visible(driver, locator, timeout: int | None = None):
    """Ждёт, пока элемент появится и станет видимым."""
    return WebDriverWait(driver, timeout or settings.timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_clickable(driver, locator, timeout: int | None = None):
    """Ждёт, пока элемент станет кликабельным."""
    return WebDriverWait(driver, timeout or settings.timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_present(driver, locator, timeout: int | None = None):
    """Ждёт появления элемента в DOM (не обязательно видим)."""
    return WebDriverWait(driver, timeout or settings.timeout).until(
        EC.presence_of_element_located(locator)
    )
