#!/usr/bin/python

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['runoobdb']
mycol = mydb['sites']

# 查询一条数据
x = mycol.find_one()
print(x)
print()

# 查询集合中所有数据
for x in mycol.find():
    print(x)
print()

# 查询指定字段的数据(除了_id不指定为0的时候会默认显示，其他字段指定为1才会显示，不能指定为0，会报错，因为默认不指定时默认不显示)
for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
    print(x)
print()

# 当指定除了_id之外的字段为0时，其他的字段都必须为1（意思就是除_id之外，要么全指定为1，要么全指定为0）
for x in mycol.find({}, {"alexa": 0, "name": 0}):
    print(x)
print()

# 根据指定条件查询
myquery = {"name": "RUNOOB"}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)
print()

# 高级查询
# 读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据
myquery = {"name": {"$gt": "H"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
print()

# 返回指定条数记录
myresult = mycol.find().limit(3)

# 输出结果：
for x in myresult:
    print(x)
print()
