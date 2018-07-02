#!/usr/bin/python

# 访问mongo数据库

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

dblist = myclient.list_database_names()
print(dblist)
if "runoobdb" in dblist:
    print("数据库已存在！")
else:
    mydb = myclient['runoobdb']
    collist = mydb.collection_names()
    if "sites" in collist:
        print("sites集合已存在！")
    else:
        print("sites集合不存在！")
