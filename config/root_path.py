#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: root_path.py
@time: 2021/11/4 14:19
@desc:
"""
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(ROOT_DIR, "log")
CONFIG_DIR = os.path.join(ROOT_DIR, "config")
JSONSCHEMA_DIR=os.path.join(ROOT_DIR,'data','schema')
# print(JSONSCHEMA_DIR)
