# -*- coding: utf-8 -*-

"""
通过http接口存储设备影子数据
"""

__author__ = 'stao'

import requests

url: str = "https://iot.diandeng.tech/api/v1/device/storage/object"

device: str = ""  # 设备名
token: str = ""  # 设备token


def storage():
    request_data = {
        "device": device,
        "token": token,
        "data": {
            "testKey1": "test",
            "testKey2": {
                "testKey3": "test3",
                "testKey4": "test4"
            }
        }
    }

    result = requests.post(url, json=request_data)
    response_data = result.json()
    if response_data["message"] == 1000:
        print("save ok")
    else:
        print("save error, error message is {0}".format(response_data["detail"]))


if __name__ == '__main__':
    storage()
