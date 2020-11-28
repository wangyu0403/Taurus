#!/usr/bin/python
# -*-coding:utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2020-11-23 11:48:47
@Author  :   wangyu 
@Contact :   wangyu03@smartdot.com.cn
@Desc    :   None
"""

import pymysql

from utils.logger import log
from config.env.pathconfig import ENV_CONFIG_PATH
from utils.common import load_config


class DB(object):
    _pool = None

    @staticmethod
    def init():
        db = DB()
        return db

    def __init__(self, env=''):
        if env == '':
            db_info = load_config(ENV_CONFIG_PATH)['db']
        else:
            db_info = load_config(ENV_CONFIG_PATH)[env]
        # 数据库初始化
        self.host = db_info['host']
        self.port = int(db_info['port'])
        self.user = db_info['user']
        self.passwd = db_info['passwd']
        self.database = db_info['database']
        self.con = None
        self.active = False

    def _start(self):
        if not self.active:
            self.connect()

    def connect(self):
        # 连接数据库
        try:
            connection = pymysql.connect(
                host=self.host,
                port=int(self.port),
                user=self.user,
                passwd=self.passwd,
                database=self.database,
                cursorclass=pymysql.cursors.DictCursor,
                charset='utf8',
                use_unicode=True)
            log.info('{0} :database is connecting successful'.format(
                self.host))
            self.con = connection
        except Exception as e:
            log.error('{0} :database is connecting failed : {1}'.format(
                self.host, e))

    def query_one(self, sql):
        # 查询一个
        self._start()
        cursors = self.con.cursor()
        log.info('execute query one sql: {0}'.format(sql))

        try:
            cursors.execute(sql)
            result = cursors.fetchone()
            return result

        except Exception as e:
            log.error('query is error: {0}'.format(e))
            return None

    def query_all(self, sql):
        # 查询所有
        self._start()
        cursors = self.con.cursor()
        log.info('execute query all sql: {0}'.format(sql))
        try:
            cursors.execute(sql)
            result = cursors.fetchall()
            log.info('query all result: {0}'.format(result))
            return result
        except Exception as e:
            log.error('query is error: {0}'.format(e))
            return None

    def change_datas(self, sql):
        # 增，删，改
        self._start()
        cursors = self.con.cursor()
        log.info('inert into sql: {0}'.format(sql))
        try:
            result = cursors.execute(sql)
            cursors.close()
            self.con.commit()
            log.info('inert into reault: {0}'.format(result))
            return result
        except Exception as e:
            log.error('inert into error: {0}'.format(e))
            return None

    def batch_insert(self, sql, values):
        try:
            self._start()
            cursors = self.con.cursor()
            result = cursors.executemany(sql, values)
            cursors.close()
            self.con.commit()
            return result
        except Exception as err:
            log.error('import failed with error: {0}'.format(err))
            return None

    def closes(self):
        # 关闭数据库连接
        self._start()
        try:
            self.active = False
            self.con.close()
            log.info('database is closed: {0}'.format(self.host))
        except Exception as e:
            self.active = False
            log.error('database is closed error: {0}'.format(e))
            raise 'server is error {0}'.format(e)

