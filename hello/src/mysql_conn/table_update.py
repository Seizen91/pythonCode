#!/usr/bin/python

"""
update data
"""
import pymysql

# connect the database
db = pymysql.connect("localhost", "root", "root", "test")

# create a cursor
cursor = db.cursor()

# the sql statement
sql = "update employee set age = age + 1 where sex = '%c'" % ('M')

try:
    # execute the sql statement
    cursor.execute(sql)

    # submit to the database to commit
    db.commit()

except:
    db.rollback()

# close the connection
db.close()
