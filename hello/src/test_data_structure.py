# python3 数据结构

# 列表 list
a = [66.25, 333, 333, 1, 1234.5]

# 返回元素在列表中出现的次数
print(a.count(66.25), a.count(333), a.count(2))

# 在指定位置插入元素
a.insert(2, -1)
print(a)

# 把一个元素添加到列表的结尾，相当于a.insert(len(a), x)
a.append(333)
print(a)

# 返回列表中第一次出现该元素的位置
print(a.index(333))

# 移除列表中的第一个这样的元素
a.remove(333)
print(a)

# 列表反转
a.reverse()
print(a)

# 列表排序
a.sort()
print("正序：", a)
a.sort(reverse=True)
print("倒序：", a)
print()


"""
将列表当作堆栈使用（后进先出）
    用append()方法可以把一个元素添加到堆栈顶，
    用不指定索引的pop()方法可以把一个元素从堆栈顶释放出来
"""

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)
print()


"""
将列表当作队列使用（先进先出）
    用列表当作队列效率不高，在列表的最后添加或者弹出元素速度最快，
    在列表里插入或者从头部弹出速度却不快
"""
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

print(queue.popleft())
print(queue.popleft())
print(queue)
print()

"""
列表推导式：
    1、列表推导式提供了从序列创建列表的简单途径
    2、通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，
        或根据确定的判定条件创建子序列
"""
vec = [2, 4, 6]
print([3*x for x in vec])
print([[x, x**2] for x in vec])
print()

freshfruit = ['   banana', '   loganberry', '   passion fruit']
print([weapon.strip() for weapon in freshfruit])
print()

print([3*x for x in vec if x > 3])
print([3*x for x in vec if x < 2])
print()

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])
print()


"""
嵌套列表解析
"""
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print([[row[i] for row in matrix] for i in range(4)])
print()

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
print()


"""
del语句
"""
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]    # 删除列表中的所有元素
print(a)
del a       # 删除表的所有元素及表a的定义


"""
元组和序列
"""

t = 1234, 54321, 'hello!'
print(t[0])
print(t)
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
print()

"""
集合
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

# 以下演示了两个集合的操作
a = set('abracadabra')
b = set('alacazam')
print(a)            # a中唯一的字母
print(a - b)        # 在 a 中的字母，但不在b中
print(a | b)        # 在 a 或 b 中的字母
print(a & b)        # 在 a 和 b 中都有的字母
print(a ^ b)        # 在 a 或 b中的字母，但不同时在 a 和 b 中

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
print()

"""
字典
"""
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)
print()


"""
遍历技巧
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
print()

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
print()

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions,  answers):
    print("What is your {0}? It is {1}。".format(q, a))
print()

for i in reversed(range(1, 10, 2)):
    print(i)
print()

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(basket)
for f in sorted(basket):
    print(f)
print()

for f in sorted(set(basket)):
    print(f)
print()























