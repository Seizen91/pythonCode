#!/usr/bin/python

import pymysql

# connect the database
db = pymysql.connect("localhost", "root", "root", "test")

# use the function cursor() to get cursor
cursor = db.cursor()

# the sql statement:insert
sql = """
    insert into employee(first_name, last_name, age, sex, income) 
    values ("Mac", "Mohen", 20, "M", 2000)
"""

sql1 = "insert into employee(first_name, last_name, age, sex, income) \
        values ('%s', '%s', '%d', '%c', '%d')" % \
       ('Mama', 'Mama', 20, 'M', 1000)

try:
    # execute the sql statement
    cursor.execute(sql1)

    # submit to database to execute
    db.commit()
except ConnectionError:
    # if occur to error, it need to rollback
    db.rollback()

# close the connection
db.close()
