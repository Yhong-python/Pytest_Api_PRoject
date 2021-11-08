#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: log_tools.py
@time: 2021/11/2 16:32
@desc:
"""
import json
import time
from functools import wraps

from common.log import logger


def body_to_dict(body_str: str):
    body_list = body_str.split('&')
    dict_body = {}
    for i in body_list:
        temp_str_list = i.split('=')
        dict_body[temp_str_list[0]] = temp_str_list[1]
    return dict_body


def wrapper_request_log(func):
    @wraps(func)
    def collect_request_detail(*args, **kwargs):
        start_time = time.time()
        r = func(*args, **kwargs)
        total_time = (time.time() - start_time) * 1000
        total_time = "%.3f" % total_time
        logger.info("==================================<<  Request Detail  >>==================================")
        logger.info(f"URL:   {r.request.url}")
        logger.info(f"Method:   {r.request.method}")
        logger.info(f"Content-Type:   {r.request.headers.get('Content-Type')}")
        logger.info(f"Headers:   {r.request.headers}")
        params = {}
        if "?" in r.request.url:
            params_str = r.request.url.split("?")[1]
            params = json.dumps(body_to_dict(params_str), ensure_ascii=False)
        logger.info(f"Params:   {params}")
        if kwargs.get("data"):
            body = json.dumps(kwargs.get("data"), ensure_ascii=False)
            logger.info(f"Body:   {body}")
        elif kwargs.get("json"):
            Json = json.dumps(kwargs.get("json"), ensure_ascii=False)
            logger.info(f"Json:   {Json}")
        logger.info(f"Time:   {total_time}ms")
        logger.info("==================================<<  Response Detail  >>==================================")
        logger.info(f"Status_code:   {r.status_code}")
        logger.info(f"Headers:   {r.headers}")
        logger.info(f"Content:   {r.content.decode()}")
        logger.info(f"Cookies:   {r.cookies.get_dict()}")
        return r

    return collect_request_detail
