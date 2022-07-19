# -*- coding: utf-8 -*-

"""
通过mqtt接口存储设备影子数据
"""

__author__ = 'stao'

import json

import paho.mqtt.publish as client

deviceName = ""     # 设备名
username = ""       # mqtt用户名
password = ""       # mqtt用户密码

hostname = "broker.diandeng.tech"
topic = "/device/{0}/s".format(deviceName)


def storage():
    payload = {
        "fromDevice": deviceName,
        "toStorage": "ot",
        "data": {
            "testKey1": "test1",
            "testKey2": {
                "testKey3": "test3",
                "testKey4": "test4"
            }
        }
    }

    client.single(topic, payload=json.dumps(payload), hostname=hostname, client_id=deviceName,
                  auth={"username": username, "password": password})


if __name__ == '__main__':
    storage()
    print("save ok")
