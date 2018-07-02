# python3 元组

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"   # 不需要括号也可以
print(type(tup3))

tup1 = ()   # 创建空元组

tup1 = (50) # 不加逗号，类型为整型
print(type(tup1))

tup1 = (50, )    # 元组只包含一个元素时，需要在元素后面添加逗号
print(type(tup1))

# 访问元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 修改元组 （元组是不可修改的，但可以进行连接组合）
tup1 = (12, 34.45)
tup2 = ('abc', 'xyz')

# tup1[0] = 100 此操作是非的

tup3 = tup1 + tup2
print(tup3)
print()

# 删除元组，元组中的元素不允许删除，但是可以删除整个元组
print(tup1)
del tup1
# print("删除后的元组 tup1：", tup1)    # 此时报tup1 is not defined

# 元组运算符
print(len((1, 2, 3)))
print((1, 2, 3,) + (4, 5, 6))
print(("Hi!",) * 4)
print(3 in (1, 2, 3))
for x in (1, 2, 3): print(x, end=" ")
print()

# 元组索引、截取
tup1 = ('Google', 'Runoob', 1997, 2000)
print(tup1[2])
print(tup1[-2])
print(tup1[1:])
print()

# 元组内置函数
print("=============")
tup1 = (12, 54.4, 1)
print(len(tup1))
print(max(tup1))
print(min(tup1))

list1 = [1, 3, "hello"]
print(tuple(list1))     # 将列表转换为元组

