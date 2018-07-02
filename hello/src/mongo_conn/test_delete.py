#!/usr/bin/python

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['runoobdb']
mycol = mydb['sites']

myquery = {"name": "Taobao"}

mycol.delete_one(myquery)

# 删除后输出
for x in mycol.find():
    print(x)
print()

# 删除多个文档
# 删除所有name字段中以F开头的文档
myquery = {"name": {"$regex": "^F"}}

x = mycol.delete_many(myquery)

print(x.deleted_count, "个文档已经删除")

# 删除集合中所有文档
x = mycol.delete_many({})
print(x.deleted_count, "个文档已经删除")

# 删除集合
mycol.drop()
collist = mydb.collection_names()
if "sites" in collist:
    print("sites集合已存在！")
else:
    print("sites集合不存在！")
