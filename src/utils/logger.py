import logging

from src.config.conf import log_level

logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s', level=log_level)

logger = logging.getLogger("om_task")
