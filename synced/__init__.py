from util import logger

__version__ = 1.0

def initialize(logging=True):
    if(logging):
        logger.console_log_instance.init_logging()

def version():
    return __version__
