import logging

class Logger():
    def __init__(self, module_name: str=__name__) -> None:
        LOGGER = logging.getLogger(module_name)
        LOGGER.propagate = False
        LOGGER.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        LOGGER.addHandler(console_handler)
        self.LOGGER = LOGGER

    def get_logger(self) -> logging.Logger:
        return self.LOGGER
