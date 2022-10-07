import logging

# Конфигурация
logger = logging.getLogger("MyLogger")
logger.addHandler(logging.StreamHandler())
file_handler = logging.FileHandler("data/log.txt")
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)-10s %(message)s"))
logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.CRITICAL)
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    # Использование логгера (просто демонстрация)
    logger.debug("It is debug")
    logger.info("It is info")
    logger.warning("It is warning")
    logger.error("It is error")
    logger.critical("It is critical")

