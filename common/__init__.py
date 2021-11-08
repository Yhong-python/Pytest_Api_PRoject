#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: __init__.py.py
@time: 2021/11/2 14:42
@desc:
"""
# import jsonpath
# print(jsonpath.jsonpath({"content":[{"token1":123},{"token2":312312}]},"content[0].token1"))
# x={
#     "success": True,
#     "errorKey": None,
#     "results": {
#         "payments": [
#             {
#                 "name": "current",
#                 "all": {
#                     "revenue": 390.32,
#                     "count": 1
#                 }
#             },
#             {
#                 "name": "sameYesterday",
#                 "all": {
#                     "revenue": 613.24,
#                     "count": 4
#                 }
#             },
#             {
#                 "name": "yesterday",
#                 "all": {
#                     "revenue": 613.24,
#                     "count": 3
#                 }
#             }
#         ]
#     }
# }
# print(jsonpath.jsonpath(x,"results.payments[1]"))