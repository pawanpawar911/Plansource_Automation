import logging
import os

class LogGenerate:
    @staticmethod
    def logger_file():
        os.makedirs("./logs", exist_ok=True)
        logging.basicConfig(
            filename=f".\\logs\\test.log",
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%d-%m-%Y %H:%M:%S',
            level=logging.INFO,
            encoding='utf-8', 
            force=True
        )

        logger = logging.getLogger()
        return logger