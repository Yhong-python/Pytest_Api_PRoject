#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: tools.py
@time: 2021/11/4 14:10
@desc:
"""
import json
import os

from genson import SchemaBuilder
from ruamel import yaml
from jsonschema import validate
from jsonschema.exceptions import SchemaError, ValidationError

class FileDataOperate:
    @staticmethod
    def read_yaml(file_path):
        print(file_path)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read().strip()
            # content = yaml.load(stream=content, Loader=yaml.SafeLoader)  #旧方法，会有警告
            y = yaml.YAML(typ='unsafe', pure=True)
            dict_content = y.load(content)
            return dict_content
        else:
            raise Exception(f"{file_path}文件不存在")

    @staticmethod
    def update_yaml(file_path, content):
        if os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                yaml.dump(content, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)
        else:
            raise Exception(f"{file_path}文件不存在")

    @staticmethod
    def read_json(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)
            return content
        else:
            raise FileNotFoundError(f"{file_path}文件不存在")

    @staticmethod
    def update_json(file_path, content):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False)


class Utils:

    @staticmethod
    def generate_jsonchema_template(dict_obj):
        """
        根据传的字段来生成一个jsonschema模板，作为参考，必须手动修改后再用来校验
        :param dict_obj:
        :return:
        """
        builder = SchemaBuilder()
        builder.add_object(dict_obj)
        jsonchema_template = builder.to_schema()
        FileDataOperate.update_json('./jsonchema_template.json', jsonchema_template)  # 默认就放在当前目录下
        return jsonchema_template



if __name__ == '__main__':
    Utils.generate_jsonchema_template({"code":200,"list":[]})
    # all=FileDataOperate.read_yaml("E:\\Pytest_API_Project\\data\\testcase\\xxxmanage_api.yml")
    # testdatas=all.get("xxxxapi")
    # print(testdatas)
    # Utils.get_testcast_data(xxxxapi)