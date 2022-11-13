"""
基于项目做定制化封装
1、鉴权：token
2、项目通用的请求头  headers = {"X-Lemonban-Media-Type": "lemonban.v2",
                    "Content-Type": "application/json"}
3、请求体格式
"""
import json

import requests


def handle_header(token=None):
    # 得到请求头
    headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers


def send_requests(method, url, data=None, token=None):
    headers = handle_header(token)
    # 根据请求类型，调用请求方法。
    method = method.upper()
    if method == "GET":
        resp = requests.get(url, data=data, headers=headers)
    elif method == "POST":
        resp = requests.post(url, json=data, headers=headers)
    return resp


if __name__ == '__main__':
    url_login = "http://api.lemonban.com/futureloan/member/login"
    login_data = {"mobile_phone": "15689851091", "pwd": "123456789"}
    # headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
    resp1 = send_requests("POST", url_login, login_data)
    print(resp1.json())







