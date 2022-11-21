import logging

from loguru import logger
from .config import Settings

logger.add(Settings.logs_path, level='INFO', colorize=False,
           format="{time} | {level} | {message}")


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_logger(level="DEBUG", ignored=""):
    logging.basicConfig(handlers=[InterceptHandler()], level=logging.getLevelName(level))

    for ignore in ignored:
        logger.disable(ignore)
