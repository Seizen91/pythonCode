# python算术运算符
def arithmetic_operators():
    print("==============python算术运算符===============")

    a = 21
    b = 10
    c = 0

    c = a + b
    print("1 -c 的值为：", c)

    c = a - b
    print('2 - c 的值为：', c)

    c = a * b
    print("3 - c 的值为：", c)

    c = a / b
    print("4 - c 的值为：", c)

    c = a % b
    print("5 - c 的值为：", c)

    # 修改变量 a、b、c
    a = 2
    b = 3
    c = a**b
    print("6 - c 的值为：", c)

    a = 10
    b = 5
    c = a//b
    print("7 - c 的值为：", c)
    print()

# arithmetic_operators()


# python比较运算符
def comparison_operators():

    print("===============python比较运算符==============")

    x = 21
    y = 10
    z = 0

    if(x == y):
        print("1 - x 等于 y")
    else:
        print("1 - x 不等于 y")

    if(x != y):
        print("2 - x 不等于 y")
    else:
        print("2 - x 等于 y")

    if(x > y):
        print("3 - x 大于 y")
    else:
        print("3 - x 小于等于 y")

    if(x < y):
        print("4 - x 小于 y")
    else:
        print("4 - x 大于等于 y")

    # 修改 x 和 y 的值
    x = 5
    y = 20
    if(x <= y):
        print("5 - x 小于等于 y")
    else:
        print("5 - x 大于 y")

    if(y >= x):
        print("6 - y 大于等于 x")
    else:
        print("6 - b 小于 a")

# comparison_operators()


# python赋值运算符
def assignment_operators():
    print("===============python赋值运算符====================")

    a = 21
    b = 10
    c = 0

    c = a + b
    print("1 -  c 的值为：", c)

    c += a
    print("2 - c 的值为：", c)

    c *= a
    print("3 -c 的值为：", c)

    c /= a
    print("4 - c 的值为：", c)

    c = 2
    c %= a
    print("5 - c 的值为：", c)

    c **= a
    print("6 - c 的值为：", c)

    c //= a
    print("7 - c 的值为：", c)

# assignment_operators()


# python位运算符
def bit_operators():
    print("=================python位运算符==================")

    a = 60          # 60 = 0011 1100
    b = 13          # 13 = 0000 1101
    c = 0

    c = a & b       # 12 = 0000 1100
    print("1 - c 的值为：", c)

    c = a | b       # 61 = 0011 1101
    print("2 - c 的值为：", c)

    c = a ^ b       # 49 = 0011 0001
    print("3 - c 的值为：", c)

    c = ~ a         # -61 = 1100 0011
    print("4 - c 的值为：", c)

    c = a << 2      # 240 = 1111 0000
    print("5 - c 的值为：", c)

    c = a >> 2      # 15 = 0000 1111
    print("6 - c 的值为：", c)

# bit_operators()


# python逻辑运算符
def logic_operators():
    print("===================python逻辑运算符==================")

    a = 10
    b = 20

    if(a and b):
        print("1 - 变量 a 和 b 都为true")
    else:
        print("1 - 变量 a 和 b 有一个不为true")

    if(a or b):
        print("2 - 变量 a 和 b 都为true， 或其中有一个为true")
    else:
        print("2 - 变量 a 和 b 都不为true")

    # 修改变量 a 的值
    a = 0
    if(a and b):
        print("3 - 变量 a 和 b 都为true")
    else:
        print("3 - 变量 a 和 b 有一个不为true")

    if(a or b):
        print("4 - 变量 a 和 b 都为true，或其中有一个为true")
    else:
        print("4 - 变量 a 和 b 都不为true")

    if not(a and b):
        print("5 - 变量 a 和 b 都为false，或其中有一个为false")
    else:
        print("5 - 变量 a 和 b 都为true")

# logic_operators()


# python成员运算符
def member_operators():
    print("===============python成员运算符===============")

    a = 10
    b = 20
    list = [1, 2, 3, 4, 5]

    if(a in list):
        print("1 - 变量 a 在给定的列表 list 中")
    else:
        print("1 - 变量 a 不在给定的列表 list 中")

    if(b not in list):
        print("2 - 变量 b 不在给定的列表 list 中")
    else:
        print("2 - 变量 b 在给定的列表 list 中")

    # 修改变量 a  的值
    a = 2
    if(a in  list):
        print("3 - 变量 a 在给定的列表 list 中")
    else:
        print("3 - 变量 a 不在给定的列表 list 中")

# member_operators()


# python身份运算符
def identity_operators():
    print("===============python身份运算符=================")

    a = 20
    b = 20

    if(a is b):
        print("1 - a 和 b 有相同的标识")
    else:
        print("1 - a 和 b 没有相同的标识")

    if(id(a) == id(b)):
        print("2 - a 和 b 有相同的标识")
    else:
        print("2 - a 和 b 没有相同的标识")

    # 修改变量 b 的值
    b = 30
    if(a is b):
        print("3 - a 和 b 有相同的标识")
    else:
        print("3 - a 和 b 没有相同的标识")

    if(a is not b):
        print("4 - a 和 b 没有相同的标识")
    else:
        print("4 - a 和 b 有相同的标识")

# identity_operators()

# is 与 ==区别：is 用于判断两个变量引用对象是否为同一个，==用于判断引用对象的值是否相等
a = [1, 2, 3]

b = a
print(b is a)
print(b == b)

b = a[:]
print(b)
print(b is a)
print(b == a)
