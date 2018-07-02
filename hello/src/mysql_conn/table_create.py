#!/usr/bin/python

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "test")

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行sql，如果表存在则删除
cursor.execute("drop table if exists employee")

# 使用预处理语句建表
sql = """
    create table employee(
    id int primary key,
    first_name char(20) not null,
    last_name char(20),
    age int,
    sex char(1),
    income float )
"""

cursor.execute(sql)

# 关闭数据库连接
db.close()