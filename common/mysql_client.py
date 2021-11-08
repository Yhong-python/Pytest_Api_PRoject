#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: mysql_client.py
@time: 2021/11/4 13:54
@desc:
"""
import pymysql

from common.log import logger


class MysqlClient:
    db_config = None  # 通过conftest来赋值

    def __new__(cls, *args, **kwargs):
        if not hasattr(MysqlClient, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __del__(self):
        self.cur.close()
        self.conn.close()

    @classmethod
    def connect_db(cls, db_config):
        cls.db_config = db_config
        if hasattr(MysqlClient, 'cur'):  # 多次调用时，先把上一个连接关掉
            cls.cur.close()
        cls.conn = pymysql.connect(**db_config)
        cls.cur = cls.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def select_db(self, sql, dbname=None):
        if dbname and self.db_config['db'] != dbname:  # 这个参数传值且与原值不相同时则表示要切换数据库连接
            self.db_config['db'] = dbname
            self.connect_db(self.db_config)
        self.conn.ping()
        if sql.upper().startswith("UPDATE") or sql.upper().startswith("INSERT") or sql.upper().startswith("DELETE"):
            try:
                self.cur.execute(sql)
                self.conn.commit()
            except Exception as e:
                logger.error(f"操作Mysql时出现异常，报错:{e}")
                self.conn.rollback()
        else:
            self.cur.execute(sql)
            data = self.cur.fetchall()
            return data

if __name__ == '__main__':
    a = MysqlClient()
    a.connect_db(
        {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'passwd': '123456', 'db': 'yhtest', 'charset': 'utf8'})
    # print(a.select_db("SELECT VERSION()"))
    sql = "SELECT VERSION()"

    print(a.select_db("SHOW TABLES"))
    print(a.select_db("SHOW TABLES", 'test'))
    print(a.select_db("UPDATE aaaa SET name ='都是' WHERE id=1"))
    print(a.select_db("SHOW TABLES", 'test'))

    # a.select_test()
    # a.connect_db({'host': '61.130.9.155', 'port': 13306, 'user': 'root', 'passwd': 'cJp35%Yf4=9U', 'db': 'qp_itfin2',
    #               'charset': 'utf8'})
    # a.select_test()
