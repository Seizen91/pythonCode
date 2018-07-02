#!/usr/bin/python

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['runoobdb']
mycol = mydb['sites']

myquery = {"alexa": "100000"}
newvalues = {"$set": {"alexa": "12345"}}

# 修改一条
mycol.update_one(myquery, newvalues)

for x in mycol.find():
    print(x)
print()

# 修改多条
mycol.update_many(myquery, newvalues)
for x in mycol.find():
    print(x)
print()