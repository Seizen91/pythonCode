#!/usr/bin/python

"""
fetchone(): 该方法获取下一个查询结果。结果集是一个对象
fetchall(): 接收全部的返回结果行
rowcount(): 这是一个只读属性，并返回执行execute()方法后影响的行数
"""

import pymysql

# open the connection to mysql
db = pymysql.connect("localhost", "root", "root", "test")

# use the function of cursor to get a cursor
cursor = db.cursor()

# sql statemnet
sql = "select * from employee \
        where income > '%d'" % (1000)

try:
    # execute the sql statement
    cursor.execute(sql)

    # get the result lists
    results = cursor.fetchall()
    for row in results:
        fname = row[1]
        lname = row[2]
        age = row[3]
        sex = row[4]
        income = row[5]

        # print the result
        print("fname=%s, lname=%s, age=%d, sex=%s, income=%d" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# close the connection
db.close()