#!/usr/bin/python
# _*_coding:utf-8 _*_
"""
@File    : test_cla.py
@Time    : 2020/11/28 2:44 下午
@Author  : wangyu   
@Email   : wangyu03@smartdot.com
@Software: PyCharm
"""
from utils.logger import *


class testClass(object):
    def __init__(self, name, gender):
        self.Name = name
        self.gender = gender
        logging.info('hello')

testman = testClass('111','22')
logging.info(testman.Name)

