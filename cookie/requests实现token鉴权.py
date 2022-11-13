"""
第一步：获取登陆请求返回当中的token值。
第二步：拿着第一步的token值，去发送其它的请求。
注意：每一次登陆生成的token都不一样。再次登陆后，上一次的token就直接失效。以最新的token为准

前程贷项目，标准请求头要求：
 headers = {"X-Lemonban-Media-Type": "lemonban.v2",
                    "Content-Type": "application/json"}

========== 第一步：登陆前程贷，获取token值============
登陆url: url = "http://api.lemonban.com/futureloan/member/login"
请求类型：post
请求数据：
    datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}

响应数据中获取token值：token = resp.json()["data"]["token_info"]["token"]


========== 第二步：给上一步用户进行充值操作，请求头当中，Authorization中设置为Bearer {token}============
充值url：http://api.lemonban.com/futureloan/member/recharge
请求类型：post
请求数据：datas = {"member_id": 200119, "amount": 2000}
"""
import json

import requests

url_login = "http://api.lemonban.com/futureloan/member/login"
login_data = {"mobile_phone": "15689851091", "pwd": "123456789"}
headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
resp = requests.post(url_login, json=login_data, headers=headers)
# for key, value in resp.json().items():
#     print(key, value)
print(resp.json())
token_dict = resp.json()
token = token_dict["data"]["token_info"]["token"]
print(token)

print("========== 第二步：给上一步用户进行充值操作，请求头当中，Authorization中设置为Bearer {token}============")

headers["Authorization"] = "Bearer {}".format(token)
# headers["Authorization"] = "Bearer {}".format(token)
print(headers)
datas_rech = {"member_id": 178334, "amount": 100, "Content-Type": "application/json"}
url_recha = "http://api.lemonban.com/futureloan/member/recharge"
resp = requests.post(url_recha, json=datas_rech, headers=headers)
print(resp.json())

