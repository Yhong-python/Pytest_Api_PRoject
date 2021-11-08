#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: conftest.py
@time: 2021/11/2 15:37
@desc:
"""
import os

import pytest

from common.http_client import HttpClient
from common.mysql_client import MysqlClient
from common.tools import FileDataOperate
from config.root_path import CONFIG_DIR


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store",
                     default='test',
                     choices=['test', 'prod'],
                     help="将命令行参数--cmdopt添加到pytest配置中")


@pytest.fixture(scope="session")
def cmdopt(request):
    cmdopt_value = request.config.getoption("--cmdopt")
    return cmdopt_value


@pytest.fixture(scope='session', autouse=True)
def set_envirment_base_params(cmdopt):
    # 设置数据库和接口请求根路径参数
    setting_path = os.path.join(CONFIG_DIR, "setting.yml")
    setting_data = FileDataOperate.read_yaml(setting_path).get("environment").get(cmdopt)
    # 将接口请求根路径和数据库连接信息赋值给各自类的类属性里
    HttpClient.api_root_url = setting_data.get("root_url")
    db_conf = setting_data.get("db_config")
    # Mysql_client.db_config=db_conf
    MysqlClient.connect_db(db_conf)  #把连接信息赋值给类变量，连接其他数据库时只需要改一下db的名称就行
    # Mysql_client().select_test()

    # Mysql_client().select_test()
    # Mysql_client().select_test()
