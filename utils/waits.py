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

#    08.11: Добавил ожидание полной загрузки страницы
def wait_page_loaded(driver, timeout=20):
    """Ждём, когда страница полностью загрузится (DOM + ресурсы)."""
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

#    08.11: Добавил ожидание "исчезновения" лоадеров (Часто на сайтах после клика появляется спиннер/лоадер. Нужно ждать его исчезновения.)
def wait_invisible(driver, locator, timeout=10):
    """Ждём, когда элемент станет невидимым."""
    return WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(locator)
    )