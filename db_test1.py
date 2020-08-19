#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

if __name__ == '__main__':
    connect = pymysql.connect(host='139.224.10.77', user='root', password='123456', database='db_test1', charset='utf8')

    try:
        with connect.cursor() as cursor:
            splStr = """
                INSERT INTO `table_test1`(`id`, `name`) VALUES (1,'张三');
                """
            execute = cursor.execute(splStr)
            print(execute)
            connect.commit()

    finally:
        connect.close()
