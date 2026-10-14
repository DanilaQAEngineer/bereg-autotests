# Нужен для фикстуры driver + скриншот при падении + браузер через параметр


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config.settings import settings
from utils.logger import get_logger


log = get_logger()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=settings.browser,
        help="Браузер: chrome / firefox",
    )
    parser.addoption(
        "--headless",
        action="store",
        default=str(settings.headless),
        help="Запуск без UI: true / false",
    )


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless").lower() == "true"

    log.info(f"Запуск браузера: {browser}, headless={headless}")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        d = webdriver.Chrome(options=options)
    elif browser == "firefox":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        d = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser}")

    d.implicitly_wait(0)  # используем только явные ожидания
    yield d

    log.info("Закрытие браузера")
    d.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Скриншот при падении теста."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            settings.screenshots_dir.mkdir(exist_ok=True)
            name = f"{item.name}.png"
            path = settings.screenshots_dir / name
            try:
                driver.save_screenshot(str(path))
                log.error(f"Скриншот падения: {path}")
            except Exception as e:
                log.error(f"Не удалось сохранить скриншот: {e}")
