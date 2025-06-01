from logging import Logger, Formatter, StreamHandler
import logging

def setup_logger() -> Logger:
    logger: Logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    ch: StreamHandler = StreamHandler()
    ch.setLevel(logging.INFO)

    formatter: Formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger


logger: Logger = setup_logger()