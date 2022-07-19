# -*- coding: utf-8 -*-

"""
文本时序数据存储
"""

__author__ = 'stao'

import random
import requests
import time

url: str = "https://iot.diandeng.tech/api/v1/device/storage/logs"

device: str = ""  # 设备名
token: str = ""  # 设备token


def storage():
    for index in range(5):
        request_data = {
            "device": device,
            "token": token,
            "data": [[int(time.time()), "这是第{0}条日志".format(index + 1)]]
        }

        result = requests.post(url, json=request_data)
        response_data = result.json()
        if response_data["message"] == 1000:
            print("save ok")
        else:
            print("save error, error message is {0}".format(response_data["detail"]))
            break

        time.sleep(60)


if __name__ == '__main__':
    storage()
