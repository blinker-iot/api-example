let hmac_sha1 = require("crypto-js/hmac-sha1");
let enc_base64 = require("crypto-js/enc-base64");
const axios = require('axios').default;

// 管理台获取accessKey、secretKey
let accessKey = ''
let secretKey = ''

// APP或管理台获取设备识别码
let deviceName = ''

// 存储数据的key
let dataKey = ''

// token过期时间
let expirationTime = parseInt(new Date().getTime() / 1000) + (60 * 60);

let url = `https://storage.diandeng.tech/api/v1/ts?e=${expirationTime}&device=${deviceName}&keyword=${dataKey}&quickDate=1h&queryType=avg`
let sign = enc_base64.stringify(hmac_sha1(url, secretKey)).replace(/\+/g, '-').replace(/\//g, '_')
let token = accessKey + ":" + sign
console.log(token);

axios.get('https://storage.diandeng.tech/api/v1/ts', {
    params: {
        "e": expirationTime, // 过期时间，unix时间戳(秒）
        "device": deviceName, // 设备名
        "keyword": dataKey, // 存储key
        "quickDate": "1h", // 快速查询码：最近1小时
        "queryType": "avg", // 查询类型：平均
        "token": token // 计算出的token
    }
}).then(resp => {
    console.log(resp.data);
})