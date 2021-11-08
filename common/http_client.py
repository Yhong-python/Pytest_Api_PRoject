#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: http_client.py
@time: 2021/11/2 15:03
@desc:
"""
import threading

import requests

from common.log import logger
from common.log_tools import wrapper_request_log


class HttpClient():
    _instance_lock = threading.Lock()
    session=requests.session()
    api_root_url= "http://testfdv2.gold-cloud.com:82"

    def __new__(cls, *args, **kwargs):
        # 可被继承的单例类
        if not hasattr(cls, "instance_dict"):
            cls.instance_dict = {}
        if str(cls) not in cls.instance_dict.keys():
            with cls._instance_lock:
                _instance = super().__new__(cls, *args, **kwargs)
                cls.instance_dict[str(cls)] = _instance
        return cls.instance_dict[str(cls)]

    # def __call__(self,*args,**kwargs):
    #     return self.send_http_request(*args,**kwargs)

    def set_base_url(self, option):
        if option == "test":
            print("设置测试环境参数")
        elif option == "prod":
            print("设置生产环境参数")
        else:
            raise ValueError(f"读取环境参数异常,当前参数为:{option}")

    def update_headers(self, headers: dict):
        self.session.headers.update(headers)

    def update_cookies(self, new_cookies: dict):
        for k, v in new_cookies.items():
            # 删除指定cookie时将v的值设置为None
            self.session.cookies.set(k, str(v))

    @wrapper_request_log
    def send_http_request(self, api_url, request_method, verify=False, **kwargs):
        request_url = self.api_root_url + api_url
        if request_method.lower() in ['get', 'post', 'put', 'delete']:
            r = self.session.request(url=request_url, method=request_method.lower(), verify=verify, **kwargs)
        else:
            logger.error(f"请求方法错误,当前的请求方法为：{request_method}")
            raise Exception()
        return r


if __name__ == '__main__':
    a1 = HttpClient()
    # print(a1.send_http_request("/wwwApi/admin/selectAdvertisement", "post"))
    # a1.update_headers({"sss": "111"})
    # a1.update_cookies({"name": "yh", "age": 1})
    # a1.send_http_request("/wwwApi/admin/selectAdvertisement", "post")
    r=a1.send_http_request("/adminApi/admin/sys/login","post",data={'username': '19999999999',
                                                                    'password': '999999',
                                                                    'captcha': '1111'})
    # print(r.json())
    content=a1.send_http_request("/adminApi/tblCoupon/couponDown?id=235&num=5",'get')
    # name=content.headers
    # for k,v in content.headers.items():
    #     print(k,v.encode('gb2312)
    # import json
    # try:
    #     print(content.json())
    # except json.decoder.JSONDecodeError:
    #     print('error')
    # a1.send_http_request("/",'get')
    # print(b'\xe6\x96\xe5\xbb\xba'.decode())