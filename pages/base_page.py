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
    def find(self, locator: tuple[By, str]):    # Ищем ОДИН элемент по локатору — кортеж (By.XXX, "селектор"), например: (By.ID, "username")  // tuple[By, str] -- то тип-аннотация кортежа из двух элементов. By — тип константы, str — тип селектора. Python не проверяет это в рантайме, только IDE и читатель видят структуру
        """Найти видимый элемент (с ожиданием)."""
        return wait_visible(self.driver, locator)    # ждём видимости и возвращаем элемент: позволит не падать сразу, если элемент появится только через 1–2 сек  // Почему не self.driver.find_element(*locator)? Потому что find_element ищет сразу и падает, если элемента нет, а wait_visible даёт время

    def find_all(self, locator: tuple[By, str]):    # Ищем ВСЕ элементы по локатору: для списков карточек, ссылок, опций
        """Найти все элементы (без ожидания)."""
        return self.driver.find_elements(*locator)    # Распаковываем кортеж в позиционные аргументы: (By.CSS_SELECTOR, ".item") → find_elements(By.CSS_SELECTOR, ".item")

    # open/click/type возвращает self → можно строить цепочки: page.open(url).click(btn).type(field, "text")
    def click(self, locator: tuple[By, str]) -> "BasePage":    # Добавил метод клика с такой же распаковкой локатора на поз.аргументы: ищем на странице локатор и обращаемся к нему
        """Клик с ожиданием кликабельности."""
        wait_clickable(self.driver, locator).click()    # Жду, когда элемент станет кликабельным (кнопка может быть видимой, но заблокированной → клик упадёт) + Добавил метод клика  // Разница между wait_visible и wait_clickable: visible — элемент в DOM и не скрыт CSS, clickable — элемент и видимый и не задизейбленный, до него можно доскроллить
        return self    # Возвращаю страницу

    # open/click/type возвращает self → можно строить цепочки: page.open(url).click(btn).type(field, "text")
    def type(self, locator: tuple[By, str], text: str) -> "BasePage":    # Добавил метод ввода данных в поля с такой же распаковкой локатора на поз.аргументы: ищем на странице локатор и обращаемся к нему
        """Очистить и ввести текст."""
        el = self.find(locator)    # Ищу на странице видимый элемент
        el.clear()    # Предварительно очищаю инпут-поле от данных (текст может добавиться к старому (в поле может быть placeholder/автозаполнение))  // без очищения повторный запуск теста может «склеить» данные: "user1user2"
        el.send_keys(text)    # Ввожу свои данные
        return self    # Возврат цепочки

    def get_text(self, locator: tuple[By, str]) -> str:    # Добавил метод получения/взятия текста на странице
        return self.find(locator).text.strip()    # Ищу элемент по локатору + Добавил метод видимого текста элемента (.text) + Убираю возможные пробелы и переносы по краям (.strip()): иначе " Палатка " != "Палатка" в ассерте

    # Добавляю метод проверки видимости элемента без падения
    def is_visible(self, locator: tuple[By, str], timeout: int = 5) -> bool:    # Добавил метод проверки видимости элемента на странице + В аргументах распаковываю кортеж локатора в поз.аргументы + Выставляю время ожидания 5 сек
        """Проверка видимости без падения."""
        try:    # Говорю "жди"
            wait_visible(self.driver, locator, timeout=timeout)    # Жду, когда искомый элемент станет видимым на странице
            return True    # Элемент найден!
        except TimeoutException:    # Ловлю тип исключения "TimeoutException": не глушу все ошибки, а только «не дождались» (если тест стопарится на "ищу элемент Nсек и не могу найти его на странице")
            return False    # Элемент НЕ найден!
