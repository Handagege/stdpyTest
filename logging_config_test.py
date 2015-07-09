#!/usr/bin/python
import logging
import logging.config

logging.config.fileConfig("logging_config_test.conf")
logger = logging.getLogger("example01")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')

