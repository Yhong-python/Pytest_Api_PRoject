#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: test_demo.py
@time: 2021/11/2 15:38
@desc:
"""
from runner.api_yaml_runner import ApiRunner
from common.tools import FileDataOperate

testcases_data = FileDataOperate.read_yaml("E:\\Pytest_API_Project\\data\\testcase\\xxxmanage_api.yml")
testcases_jsonschema=1
xxxxapi_test_data = testcases_data.get("xxxxapi")


class TestXxxManager:
    def test_001(self):
        test_case1 = xxxxapi_test_data[0]
        ApiRunner.run_request(test_case1)

# def test_004():
#     ApiRunner.run_request(xxxxapi_test_data[1])

