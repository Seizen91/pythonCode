# List(列表)，可变

list1 = ['abcd', 768, 2.23, 'runoob', 70.2]
tinylist1 = [123, 'runoob']

print(list1)
print(list1[0])
print(list1[1:3])
print(list1[2:])
print(tinylist1 * 2)
print(list1 + tinylist1)

# Tuple（元组），不可变

tuple1 = ('abcd', 768, 2.23, 'runoob', 70.2)
tinytuple1 = (123, 'runoob')

print(tuple1)
print(tuple1[0])
print(tuple1[1:3])
print(tuple1[2:])
print(tinytuple1 * 2)
print(tuple1 + tinytuple1)

tup1 = ()       # 空元组
tup2 = (20,)    # 一个元素，需要在元素后添加逗号

# Set（集合），无序不重复的序列
# 使用大括号{ }或者set()函数创建集合
# 创建一个空集合必须用set()而不是{ }，因为{ }是用来创建一个空字典

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# Dictionary(字典)
# 是一种映射类型，字典用“{}”标识
# 是一个无序的键（key）：值（value）对集合
# 创建空字典使用{}
# 字典的关键字必须不可变类型，且不能重复

dict1 = {}
dict1['one'] = "1 - 菜鸟教程"
dict1[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'site': 'www.runoob.com'}

print(dict1['one'])
print(dict1[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

# 构造函数dict()可以直接从键值对系列构建字典如下：
dict2 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])

print(dict2)

dict3 = {x: x**2 for x in (2, 4, 6)}
print(dict3)

dict4 = dict(Runoob=1, Google=2, Taobao=3)
print(dict4)

print(list(dict4))
print(set(dict4))

print(chr(35))      # 整数转换为它的字符
print(ord('a'))     # 字符串转为它的整数值
print(oct(11))      # 八进制
print(hex(11))      # 十六进制

