#!/usr/bin/python
# _*_coding:utf-8 _*_
"""
@File    : logger.py
@Time    : 2020/11/23 11:39 下午
@Author  : wangyu   
@Email   : wangyu03@smartdot.com
@Software: PyCharm
"""
import os
import os.path
import socket
import logging
import logging.handlers
import time
from config.env.pathconfig import LOG_PATH

logging.basicConfig()


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class CreateLog(object):
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "crit": logging.CRITICAL
    }
    logger = logging.getLogger()

    def __init__(self, level='info'):
        host_name = socket.gethostname()
        ip = socket.gethostbyname(host_name)
        logging_msg_format = '[%(asctime)s]--[%(levelname)s]--[' + ip + ']--[%(module)s.py - line:%(lineno)d]-- %(message)s'
        logging_date_format = '%Y-%m-%d %H:%M:%S'
        logging.basicConfig(
            format=logging_msg_format, datefmt=logging_date_format)
        self.logger.setLevel(self.level_relations.get(level))
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)
        log_file = os.path.join(
            LOG_PATH,
            time.strftime('%Y-%m-%d-%H', time.localtime(time.time())) + '.log')
        file_handler = logging.handlers.TimedRotatingFileHandler(
            log_file, 'midnight', 1)
        file_handler.setFormatter(logging.Formatter(logging_msg_format))
        self.logger.addHandler(file_handler)

    def getloger(self):
        return self.logger


log = CreateLog().getloger()