# -*- coding: utf-8 -*-

import pytest


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
    assert 'test' in 'test001'


def test_case_005():
    print("this is test_case_005")
    assert 1 < 1


# def func(x):
#     return x + 2
#
#
# def test_answer():
#     assert func(3) == 4

# def test_f1():
#     print('+++++f1 called: ')
#
#
# def test_f2():
#     print('+++++f2 called: ')
#
# def test_f3(func):
#     def inner():
#         print('----权限验证----')
#         func()
#
#     return inner

"""
列表去重
"""

# def test_f4():
#     list_1 = [1,3,4,5,12,3,2,5,7]
#     # list_2 = []
#     # for x in list:
#     #     if x not in list_2:
#     #         list_1.append(x)
#     # print(list_2)
#     list_1 = list(set(list_1))
#     print(list_1)


# def test_f5():
#     list1 = ['Google', 'Runoob', 'Taobao', 'Baidu','Taobao']
#     # list1.remove('Taobao')
#     list1.pop()
#     print("列表现在为 : ", list1)
#     # list1.remove('Baidu')
#     print("列表现在为 : ", list1)

# def test_f6():
#     x = is_instance()
#     print(x)
#
# class is_instance(a, b):
#     def test_f6(a, b):
#         return (isinstance(a, b))


if __name__ == '__main__':
    pytest.main("-s cases_run_test.py")
