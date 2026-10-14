import pytest
from config.settings import settings
from utils.logger import get_logger


log = get_logger()

@pytest.mark.smoke    # добавил декоратор/маркировку, что этот тест относится к смоукам
def test_open_homepage(driver):
    log.info("Открываю главную")
    driver.get(settings.base_url)

    assert "Берег" in driver.title, f"Неожиданный title: {driver.title}"
    # assert "Берег123" in driver.title    # этот ассерт падает: нужен для проверки, что в logs/test.log добавляется запись о падении + в screenshots/ появится скрин test_open_homepage.png
