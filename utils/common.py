#!/usr/bin/python
# -*-coding:utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2020-11-23 11:48:47
@Author  :   wangyu 
@Contact :   wangyu03@smartdot.com.cn
@Desc    :   None
"""
import yaml
from configparser import ConfigParser

def load_yml(filepath):
    """
    get data from yml
    """
    file = open(filepath, mode='r', encoding='utf-8')
    return yaml.safe_load(file)


def load_config(config_path):
    """
    get data what type is .ini form target path
    """
    cfg = ConfigParser()
    cfg.read(config_path, encoding='utf-8')
    dictionary = {}
    for section in cfg.sections():
        dictionary[section] = {}
        for options in cfg.options(section):
            dictionary[section][options] = cfg.get(section, options)
    return dictionary


if __name__ == '__main__':
    print("")