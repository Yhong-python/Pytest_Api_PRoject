#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: api_yaml_runner.py
@time: 2021/11/5 15:33
@desc:
"""
import allure
from common.api_tools import ApiTools
from common.http_client import HttpClient
from common.log import logger


class ApiRunner:
    @staticmethod
    def run_request(testcase_data: dict):
        http_client = HttpClient()
        request_data = testcase_data.get('request').get('data')
        extract = testcase_data.get('extract', None)
        validate=testcase_data.get('validate',None)
        jsonschema_template=None
        expect_response=None
        if validate:
            jsonschema_template=validate.get('jsonSchemaTemplate')
            expect_response=validate.get('response')
        if testcase_data.get('case'):
            allure.dynamic.title(testcase_data.get('case'))
        # 先处理request中的headers
        headers = testcase_data.get('request').get('headers')
        if headers:
            http_client.session.headers.update(headers)

        # 处理data，data中的value以$开头则表示需要先进行参数替换
        ApiTools.prepare_variables(request_data)

        # 处理http请求
        api_request_result = http_client.send_http_request("/wwwApi/admin/selectAdvertisement", "post")

        # 处理teardown
        logger.info(
            "==================================<< Teardown Code Exec Detail >>==================================")
        logger.info(
            "==================================<< HTTP Response JSON-Schema Detail >>==================================")
        ApiTools.check_response(api_request_result,expect_response)

        # 处理extra，将值set到GlobalVariables中
        if extract:  # 当extra有值时才进行处理
            result = {"content": {"token1": "我是token1的值", "token2": "我是token2的值"}}
            ApiTools.extract_vars(extract, result)


class Validate:
    @classmethod
    def get_uniform_comparator(cls,comparator):
        """
        convert comparator alias to uniform name
        仿照httprunner
        """
        if comparator in ["eq", "equals", "==", "is"]:
            return "equals"
        elif comparator in ["lt", "less_than"]:
            return "less_than"
        elif comparator in ["le", "less_than_or_equals"]:
            return "less_than_or_equals"
        elif comparator in ["gt", "greater_than"]:
            return "greater_than"
        elif comparator in ["ge", "greater_than_or_equals"]:
            return "greater_than_or_equals"
        elif comparator in ["ne", "not_equals"]:
            return "not_equals"
        elif comparator in ["str_eq", "string_equals"]:
            return "string_equals"
        elif comparator in ["len_eq", "length_equals", "count_eq"]:
            return "length_equals"
        elif comparator in ["len_gt", "count_gt", "length_greater_than", "count_greater_than"]:
            return "length_greater_than"
        elif comparator in ["len_ge", "count_ge", "length_greater_than_or_equals", "count_greater_than_or_equals"]:
            return "length_greater_than_or_equals"
        elif comparator in ["len_lt", "count_lt", "length_less_than", "count_less_than"]:
            return "length_less_than"
        elif comparator in ["len_le", "count_le", "length_less_than_or_equals","count_less_than_or_equals"]:
            return "length_less_than_or_equals"
        else:
            return comparator
    @classmethod
    def equals(cls,data1,data2):
        if data1==data2:
            return True
        else:
            return False
    @classmethod
    def less_than(cls,data1,data2):
        if len(data1)<len(data2):
            return True
        else:
            return False


# api_yaml_runner(test_case1)
# print('===================')


# GlobalVariables.set_variables('session_token', {"12345":1})
# api_yaml_runner(xxxxapi_test_data[1])
