from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from utils.logger import get_logger
from utils.waits import wait_clickable, wait_present, wait_visible


log = get_logger()


class BasePage:
    """Базовый класс для всех Page Object.
    Все POM наследуются от него и НЕ вызывают driver.find_element напрямую  — ВСЁ ЧЕРЕЗ waits.py
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # ---------- Навигация ----------

    def open(self, url: str) -> "BasePage":    # open/click/type возвращает self → можно строить цепочки: page.open(url).click(btn).type(field, "text")
        log.info(f"Открываю: {url}")
        self.driver.get(url)
        return self

    def current_url(self) -> str:
        return self.driver.current_url

    def title(self) -> str:
        return self.driver.title

    # ---------- Работа с элементами ----------

    def find(self, locator: tuple[By, str]):
        """Найти видимый элемент (с ожиданием)."""
        return wait_visible(self.driver, locator)

    def find_all(self, locator: tuple[By, str]):
        """Найти все элементы (без ожидания)."""
        return self.driver.find_elements(*locator)

    def click(self, locator: tuple[By, str]) -> "BasePage":    # open/click/type возвращает self → можно строить цепочки: page.open(url).click(btn).type(field, "text")
        """Клик с ожиданием кликабельности."""
        wait_clickable(self.driver, locator).click()
        return self

    def type(self, locator: tuple[By, str], text: str) -> "BasePage":    # open/click/type возвращает self → можно строить цепочки: page.open(url).click(btn).type(field, "text")
        """Очистить и ввести текст."""
        el = self.find(locator)
        el.clear()
        el.send_keys(text)
        return self

    def get_text(self, locator: tuple[By, str]) -> str:
        return self.find(locator).text.strip()

    def is_visible(self, locator: tuple[By, str], timeout: int = 5) -> bool:    # is_visible возвращает bool, не падает с исключением
        """Проверка видимости без падения."""
        try:
            wait_visible(self.driver, locator, timeout=timeout)
            return True
        except TimeoutException:
            return False