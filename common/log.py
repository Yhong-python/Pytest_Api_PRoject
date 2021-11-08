#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: log.py
@time: 2021/11/2 14:43
@desc:
"""
import os
import time
from loguru import logger
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(project_path, 'log')
t = time.strftime("%Y-%m-%d")

class Loggings:
    """日志定义"""
    __instance = None
    logger.add(f"{log_path}/test_{t}.log", rotation="100MB", encoding="utf-8", enqueue=True,
               retention="5 days", backtrace=False)
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls,*args, **kwargs)
        return cls.__instance

loggings = Loggings()
if __name__ == '__main__':
    logger.info('111')