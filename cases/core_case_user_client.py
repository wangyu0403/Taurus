#!/usr/bin/python
# _*_coding:utf-8 _*_
"""
@File    : core_case_user_client.py
@Time    : 2020/11/23 10:45 下午
@Author  : wangyu   
@Email   : wangyu03@smartdot.com
@Software: PyCharm
"""

import requests
import json
import pytest

"""
根据msgtype 发送text/link通知

"""


def test_case_001():
    print("this is test_case_001")
    assert 1 in [1, 2, 3]


def test_case_002():
    print("this is test_case_002")
    assert 1 in [2, 3, 4]


def test_case_003():
    print("this is test_case_003")
    assert 1 >= 3


def test_case_004():
    print("this is test_case_004")
    assert 'test' not in 'test001'


def test_case_005():
    print("this is test_case_005")
    assert 1
