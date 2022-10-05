import logging

# Конфигурация
logger = logging.getLogger("MyLogger")
logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.FileHandler("data/log.txt"))
# logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.CRITICAL)
logger.setLevel(logging.INFO)

# Использование логгера
logger.debug("It is debug")
logger.info("It is info")
logger.warning("It is warning")
logger.error("It is error")
logger.critical("It is critical")

