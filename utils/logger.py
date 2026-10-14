# Нужен для записи в файл и в консоль, что происходит при падении теста: логи пишутся в файл logs/test.log


import logging
import sys
from pathlib import Path
from config.settings import settings


def get_logger(name: str = "autotests") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # уже настроен

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # В файл
    settings.logs_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(settings.logs_dir / "test.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # В консоль
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
