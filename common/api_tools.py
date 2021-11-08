#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: api_tools.py
@time: 2021/11/8 12:13
@desc:
"""
import os

import jsonpath
from common.tools import FileDataOperate
from common.log import logger
from common.variables import GlobalVariable
from config.root_path import JSONSCHEMA_DIR
from jsonschema import validate
from jsonschema.exceptions import SchemaError, ValidationError

class ApiTools:

    @staticmethod
    def prepare_variables(request_data: dict):
        """
        处理data中的value以$开头变量，需要先进行参数替换
        :param testcase_data:

        """
        logger.info(
            "==================================<<  SetUp Code Exec Detail  >>==================================")
        for key, value in request_data.items():
            if isinstance(value, str) and value.startswith('$'):  # 需要替换的值一定是str类型的
                request_data[key] = GlobalVariable.get_variables(value[1:])
                if hasattr(GlobalVariable, value[1:]):  # 截掉字符串前面的$
                    logger.info(
                        f"Variable substritution successfully,from GlobalVariable:> {value} ==>{request_data[key]}")
                else:
                    logger.warning(f"Variable {value[1:]} not in GlobalVariable or this variable is None")
                    logger.warning(f"Dependent testcase's extra maybe get error,Please check it.")

    @staticmethod
    def extract_vars(testcase_extra_data: dict, api_result: dict):
        logger.info("==================================<<  Extra Detail  >>==================================")
        for key, value in testcase_extra_data.items():
            target_extra_result = jsonpath.jsonpath(obj=api_result, expr=value)
            if target_extra_result:  # jsonpath匹配上了会返回列表，没匹配成功返回False
                target_extra_data_value = target_extra_result[0]
                GlobalVariable.set_variables(key, target_extra_data_value)
                logger.info(f"Variable saved successfully ==> {key} :> {target_extra_data_value}")
            else:
                logger.error(f'Extra data from apiResult return False.Current jsonpath expr is {value}')

    @staticmethod
    def check_response(api_request_result,expect_response:list):
        print(expect_response)
        for check_data in expect_response:
            for k,v in check_data.items():
                pass
                #k是比较的符号，如eq代表==，
    @staticmethod
    def validate_and_check_jsonschema(jsonSchema_template,api_request_result:dict):
        """

        :param jsonSchema_template:
        :param api_request_result:
        :return:
        """
        filename,key = jsonSchema_template.split('.')[0] + ".json", jsonSchema_template.split('.')[1]
        path = os.path.join(JSONSCHEMA_DIR, filename)
        my_chema=FileDataOperate.read_json(path).get(key)
        if not isinstance(my_chema, dict):
            logger.error('jsondata pattern is not a dict object')
            raise TypeError
        try:
            validate(instance=api_request_result, schema=my_chema)
        except SchemaError as e:
            logger.error("验证模式schema出错：出错位置：{} 提示信息：{}".format(" --> ".join([i for i in e.path]), e.message))
            return False
        except ValidationError as e:
            logger.error("api_request_result数据不符合schema规定：出错字段：{} 提示信息：{}".format(" --> ".join([i for i in e.path]), e.message))
            return False
        else:
            logger.info("JSON-Schema validate success！")
            return True

if __name__ == '__main__':
    # ApiTools.prepare_variables({'name':"1"})
    # testcase_extra_data = {"session_token1": "content.token1", "session_token2": "content.token2"}
    # api_result={"content":{"token1":"我是token1的值","token2":"我是token2的值"}}
    # api_result = {"code": 200, "list": []}
    # ApiTools.extract_vars(testcase_extra_data, api_result)
    ApiTools.validate_and_check_jsonschema("xxxmanager_api.api1",{"code":200,"list":[]})
