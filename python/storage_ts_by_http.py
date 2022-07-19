# -*- coding: utf-8 -*-

"""
通过http接口存储数值时序数据
"""

__author__ = 'stao'

import random
import requests
import time

url: str = "https://iot.diandeng.tech/api/v1/device/storage/ts"

device: str = ""  # 设备名
token: str = ""  # 设备token


def storage():
    while True:
        storage_data = {
            "humi": [[int(time.time()), random.randint(1, 300)]],
            "temp": [[int(time.time()), random.randint(1, 300)]],
            "pm25": [[int(time.time()), random.randint(1, 300)]],
            "pm10": [[int(time.time()), random.randint(1, 300)]],
        }

        request_data = {
            "device": device,
            "token": token,
            "data": storage_data
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
