#!/usr/bin/python
# _*_coding:utf-8 _*_
"""
@File    : notice.py
@Time    : 2020/11/23 11:25 下午
@Author  : wangyu   
@Email   : wangyu03@smartdot.com
@Software: PyCharm
"""

from dingtalkchatbot.chatbot import DingtalkChatbot
from config.env.pathconfig import API_YML_PATH
from utils.common import load_yml
from utils.logger import log
from utils.DB import DB
import requests


# https://oapi.dingtalk.com/robot/send?access_token=4ac24fa17f005f25754d3c55a692e106668dca9af72827bdf04c33532a0ffe7a
# 默认galaxy群内机器人通知

def notice_ding(message,
                api='https://oapi.dingtalk.com/robot/send?access_token=0dc8aeedecfac05837f12a03a77f2bea8d76111db8cb454d75ac0f781fb79afb',
                at_mobiles=[]):
    if isinstance(at_mobiles, list):
        payload = {
            'msgtype': 'text',
            'text': {
                'content': message  # 需要提醒的内容
            },
            'at': {
                'atMobiles': at_mobiles,  # 需要艾特的个人电话
                'isAtAll': False  # 是否艾特所有人，Fasle代表否
            },
        }
        r = requests.post(api, headers={'Content-Type': 'application/json'}, json=payload)
        return r.status_code
    else:
        log.error('at_mobiles 的类型不是列表;{0}'.format(at_mobiles))
        return 'at_mobiles 的类型不是列表'


# jenkins钉钉通知
# default_token = '560cfa0139ef6e7287ce1c7145d2ed80ae34205552836dbfee425ce9cc048750'
# # test_token = '688adf0686c1b9455e133abc1dbf978f9d01def5d74ec10b5252107e2acad01e'
default_token = 'e012eef0b1fbbafe148d233a142a8e802e5d52bf09d2602ad4565a4bec408040'


def ding_notice(token=default_token):
    ding_token = 'https://oapi.dingtalk.com/robot/send?access_token=' + token
    return DingtalkChatbot(ding_token)


class Notice(object):

    def __init__(self):
        self.db = DB().init()
        self.sql_datas = load_yml(API_YML_PATH)

    def send_notice(self, **kwargs):
        if 'msg' not in kwargs.keys():
            log.error("请传入消息内容")
            return
        emails = self.get_noice_receiver(**kwargs)
        if emails:
            self.send_message(emails, kwargs['msg'], title=kwargs.get('title'), job_url=kwargs.get('job_url'))
        else:
            log.warn('没有消息接收人，找猫哥改下。')

    # 获取消息接收人
    def get_noice_receiver(self, **kwargs):
        emails = []
        # 添加case维护人
        service = kwargs.get('service')
        if service:
            if isinstance(service, list):
                for temp in service:
                    responsibility = self.get_responsibility(temp)
                    emails = emails + responsibility
            elif isinstance(service, str):
                responsibility = self.get_responsibility(service)
                emails = emails + responsibility

        # 添加 jenkins_job 执行人
        if kwargs.get('jenkins_user_email'):
            emails.append(kwargs.get('jenkins_user_email').split('@')[0])

        # 添加任务创建人
        if kwargs.get('task_id'):
            username = self.get_user_name(kwargs.get('task_id'))
            if username:
                emails.append(username)

        # 添加Taurus当前登录人
        if kwargs.get('parm'):
            emails.append(kwargs.get('parm'))

        return emails

    def get_responsibility(self, service):
        responsibility = []
        sql = self.sql_datas['get_responsibility'].format(service=service)
        es = self.db.query_all(sql)
        if es:
            responsibility = es[0]['responsibility'].split(',')
        return responsibility

    def get_user_name(self, task_id):
        sql = self.sql_datas['get_task_creator'].format(id=task_id)
        username = self.db.query_all(sql)[0]['username']
        return username

    def send_message(self, emails, msg, title=None, job_url=None):
        if isinstance(emails, list):
            emails = ','.join(set(emails))
        if not title:
            title = '自动化执行结果'
        url = "xxx"
        data = {"title": title, "user": emails, "content": [msg]}
        if job_url:
            data['url'] = job_url
        try:
            res = requests.post(url, headers={'Content-Type': 'application/json'}, json=data)
            if res.json()['message'] != 'success':
                log.error('发送异常:{}'.format(res.json()))

        except Exception as e:
            log.error('钉钉发送地址异常: {}'.format(e))
