"""
python 3 字典
    1、键必须是唯一的，但值则不必
    2、值可以取任何数据类型，但键必须不可变，如字符串，数字或元组
"""

# 访问字典里的值
print("=======访问字典里的值=====")
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(dict1['Name'])
print(dict1['Age'])
# print(dict1['Alice'])       # 如果访问的键不存在，则会报错
print()

# 修改字典
print("=======修改字典=======")
dict1['Age'] = 8        # 更新Age
dict1['School'] = "菜鸟教程"        # 添加信息
print(dict1['Age'])
print(dict1['School'])
print()

# 删除字典元素
print("========删除字典元素=======")
del dict1['Name']
print(dict1)

dict1.clear()
print(dict1)
print()

del dict1
# print(dict1)        # 删除字典后，会报dict1 is not defined

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict2 = dict1.copy()
print(dict2)
print()

dict1.clear()
print(dict1)
print(dict2)
print()

seq = ('name', 'age', 'sex')
dict1 = dict.fromkeys(seq)
print(dict1)
print(dict.fromkeys(seq, 10))
print()

dict1 = {'Name': 'Runoob', 'Age': 27}
print("Age 值为：s%", dict1.get('Age'))
print("Sex 值为：s%", dict1.get('Sex', "NA"))
print()

print('Age' in dict1)
print('Sex' in dict1)
print()

print(dict1.keys())
print(dict1.values())
print()

for item in dict1.items():
    print(item)
print()

dict1.setdefault('Age', None)
dict1.setdefault('Sex', None)
print(dict1)
print()

dict2 = {'School': 'www.com', 'Address': 'http'}
print(dict2)
print(dict1.update(dict2))
print(dict1)
print()

print(dict1.pop('Address'))
print(dict1)
print()

print(dict1.popitem())
print(dict1)
print()