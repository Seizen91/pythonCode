#!/usr/bin/python

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['runoobdb']
mycol = mydb['sites']

# 对字段 alexa 按升序排列
mydoc = mycol.find().sort("alexa")
for x in mydoc:
    print(x)
print()

# # 对字段 alexa 按降序排列
mydoc = mycol.find().sort("alexa", -1)
for x in mydoc:
    print(x)
print()