#!/usr/bin/python

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['runoobdb']
mycol = mydb['sites']

mydict = {"name": "RUNOOB", "alexa": "100000", "url": "https://www.runoob.com"}

# x = mycol.insert_one(mydict)    # 插入一条
# print(x)
# print(x.inserted_id)

# 插入多个文档
mylist = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"},
]

# x = mycol.insert_many(mylist)
# print(x.inserted_ids)

# 插入指定 _id 的多个文档
mycol = mydb["site2"]

mylist = [
    {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
    {"_id": 2, "name": "Google", "address": "Google"},
    {"_id": 3, "name": "Facebook", "c_name": "脸书"},
    {"_id": 4, "name": "Taobao", "c_name": "淘宝"},
    {"_id": 5, "name": "Zhihu", "c_name": "知乎"}
]

# x = mycol.insert_many(mylist)
# print(x.inserted_ids)