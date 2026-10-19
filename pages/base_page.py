from selenium.webdriver.common.by import By    # импортировали «способ поиска»: говорим Selenium, как искать элемент: == By.CSS_SELECTOR.XPATH.ID
from selenium.webdriver.remote.webdriver import WebDriver    # импортировали з селениума WebDriver (подсказывает методы)
from selenium.common.exceptions import TimeoutException    # импортировали исключения таймаута: нужен для is_visible: если элемента нет — Selenium бросает именно это, мы его ловим и возвращаем False
from utils.logger import get_logger    # импортировали функцию логгера, прописанную в utils/logger.py: добавили логи внутри POM
from utils.waits import wait_clickable, wait_present, wait_visible    # импортировали функции-обёртки ожидания, прописанные в utils/waits.py: использовать wait_visible/wait_clickable/wait_present вместо прямого WebDriverWait


log = get_logger()    # создали/взяли уже созданный логгер: один логгер на модуль. Если убрать: в open() придётся каждый раз писать get_logger().info(...), а так мы взяли готовый в utils\logger.py


class BasePage:    # Объявляем класс, который будет шаблоном/фундаментом для всех последующих страниц
    """
       Базовый класс для всех Page Object.
       Все POM наследуются от него и НЕ вызывают driver.find_element напрямую — ВСЁ ЧЕРЕЗ waits.py
    """

    def __init__(self, driver: WebDriver):    # создаём/инициализируем конструктор, который принимает драйвер и сохраняет его в объекте
        self.driver = driver    # сохраняем драйвер в атрибут/переменную "self.driver": далее все методы класса могут/будут обращаться к "self.driver" (если убрать self.driver = driver: методы не найдут драйвер и будут падать в ошибку AttributeError)

    # ---------- 1) Навигация ----------
    # open/click/type возвращает self → можно строить цепочки: page.open(url).click(btn).type(field, "text")
    def open(self, url: str) -> "BasePage":    # Метод-обёртка над driver.get (единая точка «открыть страницу», логируется) + "BasePage" -- Аннотация возвращаемого типа (возвращаем self — можно строить цепочки) // BasePage в кавычках из-за того, что в момент определения класса сам класс ещё не полностью создан, и Python не знает тип BasePage
        log.info(f"Открываю: {url}")    # Логируем URL (в отчёте будет видно, куда/на какую страницу заходили)
        self.driver.get(url)    # Открываем страницу
        return self    # Возвращаем сам объект страницы (можно: page.open(url).click(...))

    def current_url(self) -> str:    # Возвращаем текущий URL: будет полезно для ассертов: assert page.current_url() == "..."
        return self.driver.current_url    # Значение из драйвера

    def title(self) -> str:    # Возвращаем title страницы: нужно для проверок
        return self.driver.title    # Значение из драйвера

    # ---------- 2) Работа с элементами ----------
    def find(self, locator: tuple[By, str]):    # Ищем элементы: принимаем локатор — кортеж (By.XXX, "селектор"), например: (By.ID, "username")  // tuple[By, str] -- то тип-аннотация кортежа из двух элементов. By — тип константы, str — тип селектора. Python не проверяет это в рантайме, только IDE и читатель видят структуру
        """Найти видимый элемент (с ожиданием)."""
        return wait_visible(self.driver, locator)    # ждём видимости и возвращаем элемент: позволит не падать сразу, если элемент появится только через 1–2 сек  // Почему не self.driver.find_element(*locator)? Потому что find_element ищет сразу и падает, если элемента нет, а wait_visible даёт время

    def find_all(self, locator: tuple[By, str]):
        """Найти все элементы (без ожидания)."""
        return self.driver.find_elements(*locator)

    # open/click/type возвращает self → можно строить цепочки: page.open(url).click(btn).type(field, "text")
    def click(self, locator: tuple[By, str]) -> "BasePage":    #
        """Клик с ожиданием кликабельности."""
        wait_clickable(self.driver, locator).click()
        return self

    # open/click/type возвращает self → можно строить цепочки: page.open(url).click(btn).type(field, "text")
    def type(self, locator: tuple[By, str], text: str) -> "BasePage":    #
        """Очистить и ввести текст."""
        el = self.find(locator)
        el.clear()
        el.send_keys(text)
        return self

    def get_text(self, locator: tuple[By, str]) -> str:    #
        return self.find(locator).text.strip()

    def is_visible(self, locator: tuple[By, str], timeout: int = 5) -> bool:    # is_visible возвращает bool, не падает с исключением
        """Проверка видимости без падения."""
        try:
            wait_visible(self.driver, locator, timeout=timeout)
            return True
        except TimeoutException:
            return False