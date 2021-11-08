#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: variables.py
@time: 2021/11/5 15:50
@desc:
"""
class GlobalVariable:
    variables={}
    def __new__(cls, *args, **kwargs):
        if not hasattr(GlobalVariable, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance
    @classmethod
    def set_variables(cls,name,value):
        cls.variables[name]=value
    @classmethod
    def get_variables(cls,name):

        return cls.variables.get(name)