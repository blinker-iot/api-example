# -*- coding: utf-8 -*-
import hmac
import time
import requests
from base64 import urlsafe_b64encode

# 管理台获取accessKey、secretKey
accessKey = ''
secretKey = ''

# APP或管理台获取设备识别码
deviceName = ''

# 存储数据的key
dataKey = ''

# token过期时间
expirationTime = int(time.time()) + 60 * 60

url = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(
    expirationTime, deviceName, dataKey)

sign = urlsafe_b64encode(
    hmac.new(secretKey.encode("utf-8"),
             url.encode("utf-8"), digestmod='sha1').digest()
).decode("utf-8")
token = accessKey + ":" + sign
print(token)

respson = requests.get(url + "&token="+token)
print(respson.json())
