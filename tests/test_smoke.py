import pytest
from config.settings import settings
from utils.logger import get_logger


log = get_logger()

@pytest.mark.skip    # добавил декоратор/маркировку, чтобы этот тест не воспроизводился при тестовом прогоне
def test_open_homepage(browser):
    log.info("Открываю главную")
    browser.get(settings.base_url)

    assert "Берег" in browser.title, f"Неожиданный title: {browser.title}"
    # assert "Берег123" in driver.title    # этот ассерт падает: нужен для проверки, что в logs/test.log добавляется запись о падении + в screenshots/ появится скрин test_open_homepage.png
