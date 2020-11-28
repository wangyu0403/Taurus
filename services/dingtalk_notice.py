#!/usr/bin/python
# _*_coding:utf-8 _*_
"""
@File    : dingtalk_notice.py
@Time    : 2020/11/25 8:51 下午
@Author  : wangyu   
@Email   : wangyu03@smartdot.com
@Software: PyCharm
"""
import requests
import json
from utils.logger import *

"""
根据msgtype 发送text/link通知

"""


def connect_dingtalk(token,msgdata):
    ding_token = 'https://oapi.dingtalk.com/robot/send?access_token=' + token
    data = msgdata
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    rs = requests.post(url=ding_token, data=json.dumps(data), headers=headers)
    msg = rs.json()
    log.info(msg)
    return msg




if __name__ == '__main__':
    token = '21b2864cbaad0e49795062733cce2cf5aa5abe51385df20ecd6e517d736523ed'
    data_text = {"msgtype": "text","text": {"content": "测试报告：明天吃啥呀"},
        "at": {"atMobiles": ["15210187434","15210187434"],"isAtAll": 'false'}}
    data_link = {"msgtype": "link",
        "link": {
            "text": "性能测试报告",
            "title": "xxx性能测试报告",
            "picUrl": "",
            "messageUrl": "https://www.baidu.com"}}
    data_markdown = {
     "msgtype": "markdown",
     "markdown": {
         "title":"测试报告",
         "text": "#### 大佬们好 @15210187434 \n> AAAAAAA\n> ![screenshot](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1606320279134&di=270e4dccb36c0bb24cfeafed0eb961ee&imgtype=0&src=http%3A%2F%2Fa1.att.hudong.com%2F23%2F53%2F01300542749023141439532348370.jpg)\n> ###### 啦啦啦啦啦 [但是看见了的](https://www.baidu.com) \n"
     },
      "at": {"atMobiles": ["15210187434"], "isAtAll": 'True'}}
    connect_dingtalk(token, msgdata = data_markdown)