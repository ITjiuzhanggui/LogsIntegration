import logging
from logging.handlers import RotatingFileHandler

from conf import ConfManagement


class DevelopmentConfig(object):
    DEBUG = ConfManagement("default").get_ini("DEBUG")
    LOG_LEVEL = logging.DEBUG


class SetLog(object):

    def setup_log(e):
        logging.basicConfig(level=DevelopmentConfig.LOG_LEVEL)
        file_log_handler = RotatingFileHandler(
            "../logs/project.log", maxBytes=1024 * 1024 * 100, backupCount=10)
        # formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_log_handler.setFormatter(formatter)
        logging.getLogger().addHandler(file_log_handler)


    def __getattr__(self, e):
        self.setup_log()
        log_match = {
            "info": logging.info,
            "debug": logging.debug,
            "error": logging.error,
            "warning": logging.warning
        }
        if e in log_match.keys():
            return log_match.get(e)
