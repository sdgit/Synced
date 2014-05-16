import logging

ERROR = logging.ERROR
WARNING = logging.WARNING
MESSAGE = logging.INFO
DEBUG = logging.DEBUG

class ConsoleLogHandler(object):
    """docstring for ConsoleLogHandler"""
    def __init__(self):
        super(ConsoleLogHandler, self).__init__()
        self.al_log = logging.getLogger('AutoLogin')

    def log(self, toLog, logLevel=MESSAGE):
        self.al_log = logging.getLogger('AutoLogin')
        self.al_log.log(logLevel, toLog)

    def init_logging(self):
        self.al_log.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.al_log.addHandler(ch)

console_log_instance = ConsoleLogHandler();

def log(toLog, logLevel=MESSAGE):
    console_log_instance.log(toLog, logLevel)
