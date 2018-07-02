# python3 数字（Number）

"""
1、数据类型是不允许改变的，这就意味着改变数字数据类型的值，将重新分配内存空间
三种不同的数值类型：
    1、int（整型）
    2、float（浮点型）
    3、complex（复数）

"""

"""
python 数字类型转换:
    1.int(x):将x转换为一个整数
    2.float(x):将x转换带一个浮点数
    3.complex(x):将x转换到一个复数，实属部分为x，虚数部分为0
    4.complex(x,y):将x和y转换到一个复数，实数部分为x，虚数部分为y
"""
a = 1.2
print(int(a))

b = 20
print(float(b))

print(complex(a))

print(complex(a, b))

"""
python 数字运算
    1、除法 / 总是返回一个浮点数
    2、// 得到的是整数，但是它跟分子分母的数据类型有关系
"""
print(7//2)
print(7.0//2)
print(7//2.0)
