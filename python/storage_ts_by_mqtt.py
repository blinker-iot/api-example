# -*- coding: utf-8 -*-

"""
通过mqtt接口存储数值时序数据
"""

__author__ = 'stao'

import json
import random
import time

import paho.mqtt.publish as client

deviceName = ""  # 设备名
username = ""  # mqtt用户名
password = ""  # mqtt用户密码

hostname = "broker.diandeng.tech"
topic = "/device/{0}/s".format(deviceName)


def storage():
    payload = json.dumps({
        "fromDevice": deviceName,
        "toStorage": "ts",
        "data": {
            "humi": [[int(time.time()), random.randint(1, 300)]],
            "temp": [[int(time.time()), random.randint(1, 300)]],
            "pm25": [[int(time.time()), random.randint(1, 300)]],
            "pm10": [[int(time.time()), random.randint(1, 300)]]
        }
    })

    client.single(topic, payload=payload, hostname=hostname, client_id=deviceName,
                  auth={"username": username, "password": password})


if __name__ == '__main__':
    while True:
        storage()
        print("save ok")
        time.sleep(60)
