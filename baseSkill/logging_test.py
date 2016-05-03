#!/usr/bin/python

import logging


#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',filename='logging_test.log',filemode='w')

logger = logging.getLogger('MyTestLogger')

logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('logging_test.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')
