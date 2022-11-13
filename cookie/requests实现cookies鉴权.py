"""
课堂派是以cookies方式来鉴权的。
========== 第一步：登陆课堂派，获取cookies。============
登陆url: https://openapiv100.ketangpai.com//UserApi/login
请求类型：POST
请求体格式：application/json
请求数据：
   data = {"email": "15689851091",
              "password": "13550178105Zs",
              "remember": "0",
              "code": "",
              "mobile": "",
              "type": "login",
              "reqtimestamp": 1666513073437}


响应结果：
{"status":1,"code":10000,"message":"\u8bbf\u95ee\u6210\u529f","data":{"url":"","token":"7ed5b29a0f5d4829ed8b733b944c4820b4ca993439738fc9b5ddf562d430f5d9","isenterprise":0,"uid":"MDAwMDAwMDAwMLV2z92Iua9rhdtyoQ","bindWechat":false}}
cookies在响应头当中，有一个set-cookie

========== 第二步：获取用户信息 ============
接口url: https://www.ketangpai.com/UserApi/getUserInfo
请求方法：get
请求参数：无
"""

import requests

# 第一步：实例化Session对象
# s = requests.Session()
# print("登陆之前的cookies", s.cookies)
# 第二步：登陆得到cookies鉴权
login_url = "https://openapiv100.ketangpai.com//UserApi/login"
login_data = {"email": "15689851091",
              "password": "13550178105Zs",
              "remember": "0",
              "code": "",
              "mobile": "",
              "type": "login",
              "reqtimestamp": 1666513073437
              }

# s.post(login_url, data=login_data)
# print("登陆之后的cookies", s.cookies)


# 第二步获取用户信息
userinfo_url = "https://openapiv100.ketangpai.com//UserApi/getUserBasinInfo"
data = {
    "reqtimestamp": 1666796037400
}
# respon = s.get(userinfo_url)
# print(respon.json())

print("========不用session的方式获取cookies============")

# 登陆得到cookies
respon = requests.post(login_url, data=login_data)
print(respon.json())

cookies = respon.cookies
# print(cookies)


# 获取用户信息
respond = requests.get(userinfo_url, cookies=cookies)
print(respond.json())




