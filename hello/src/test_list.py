# python3 列表 list

# 访问列表中的值
list1 = ["Google", "Runoob", 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list[1:5]: ", list2[1:5])
print()

# 更新列表
print("第三个元素为：", list1[2])
list1[2] = 2001
print("更新后的第三个元素为：", list1[2])
print()

# 删除列表元素
print(list1)
del list1[2]
print("删除第三个元素：", list1)
print()

# 添加列表元素
list1.append("hello python")
print(list1)
print()

# python列表脚本操作符
print(len([1, 2, 3]))   # 列表长度
print([1, 2, 3] + [4, 5, 6])    #列表组合
print(['Hi!']*4)        # 列表重复
print(3 in [1, 2, 3])   # 判断元素是否存在列表中
for x in [1, 2, 3]: print(x, end=" ")   # 列表迭代
print()

# python列表截取与拼接
L = ['Google', 'Runoob', 'Taobao']
print(L[2])
print(L[-2])
print(L[1:])
# print(L[3]) 超出列表下标会报错
print(L + ["Hello", 2, 3])
print()

# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2]
x = [a, n]
print(x)
print(x[0][1])
print(x[1][1])  # 下标越界都会报错
print()

# python列表函数
list1 = ['Google', 'Runoob', 'Taobao']
print(len(list1))
print(max(list1))
print(min(list1))
tuple1 = ("hell0", "Python", 1)
print(list(tuple1)) # 将元组转换为列表
print()

# python列表方法
list1.append("hello")
print(list1)

list1.append("hello")
print(list1.count("hello"))

list1.extend([1, 2, 3])
print(list1)

print(list1.index("hello"))

list1.insert(2, "python")
print(list1)

print(list1.pop())  # 默认移除最后一个
print(list1)
print(list1.pop(3))
print(list1)

print(list1.remove("hello"))    # 移除列表中某个值的第一个匹配项
print(list1)

list1.reverse()
print(list1)

vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print("降序输出：", vowels)


def take_second(elem):
    return elem[1]


# define a list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=take_second)
print("排序列表：", random)

list2 = list1.copy()
print(list2)

list1.clear()
print(list1)
print(list2)
print()
