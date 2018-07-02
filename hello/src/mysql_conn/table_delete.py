#!/usr/bin/python

"""
the operation: delete
"""

import pymysql

# conncet to database
db = pymysql.connect("localhost", "root", "root", "test")

# create a cursor
cursor = db.cursor()

# the sql statement
sql = "delete from employee where age > '%d'" % (20)

try:
    # execute the sql
    cursor.execute(sql)

    # submit to database to execute
    db.commit()
except:
    # if occur to error, it need to rollback
    db.rollback()

# close the connection
db.close()