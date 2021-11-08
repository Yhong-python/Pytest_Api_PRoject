#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: dataCheck.py
@time: 2020/5/19 12:24
@desc:
'''
from jsonschema import validate
from jsonschema.exceptions import SchemaError, ValidationError


def jsonCheck(jsondata, my_schema):
    if not isinstance(jsondata, dict):
        raise TypeError('jsondata参数必须为字典格式')
    else:
        try:
            r=validate(instance=jsondata, schema=my_schema)
        except SchemaError as e:
            print("验证模式schema出错：\n出错位置：{}\n提示信息：{}".format(" --> ".join([i for i in e.path]), e.message))
            return False
        except ValidationError as e:
            print("json数据不符合schema规定：\n出错字段：{}\n提示信息：{}".format(" --> ".join([i for i in e.path]), e.message))
            return False
        else:
            print("验证成功！")
            return True

if __name__=="__main__":
    schema={
        "type":"object",
        "properties":{
            "level1":{
                "type":"integer"
            },
            "x":{
                "type":"array"
            },
            "level1-1":{
                "type":"object",
                "properties":{
                    "level2":{
                        "type":"string"
                    },
                    "level2-2":{
                        "type":"object",
                        "properties":{
                            "level3":{
                                "type":"string"
                            },
                            "level3_1":{
                                "type":"object",
                                "properties":{
                                    "level4_1":{
                                        "type":"string"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }}
    a= {
        "level1": 0,
        "level1-1": {
            "level2": "l2_v1",
            "level2-2": {
                "level3": "l3_v1",
                "level3_1": {
                    "level4_1": "v4"
                }
            }
        },
        "x":[1,23]
    }
    jsonCheck(a,schema)