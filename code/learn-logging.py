# coding:utf-8

"""
    @version:  python2.7
    @date:     2017/3/21 下午11:20
    @file:     learn-logging.py
    @software: PyCharm
    @auther:   Aesthetic92
"""

from __future__ import unicode_literals
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='../data/log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# use logging
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')