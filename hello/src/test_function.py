# python3 函数

"""
参数：
    1、必须参数
    2、关键字参数
    3、默认参数
    4、不定长参数
"""


# 必须参数
def printme(str):
    "打印任何输入的字符串"
    print(str)
    return


printme("hello python")     # 调用函数时必须输入参数，否则会报错

# 关键字参数
printme(str="菜鸟教程")


def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字：", name)
    print("年龄：", age)
    return


printinfo(age=50, name="runoob")


# 默认参数
def printinfo1(name, age=34):
    print("名字：", name)
    print("年龄：", age)
    return


printinfo1(age=50, name="runoob")
print("===============")
printinfo1(name="runoob")


# 不定长参数
def printinfo2(arg1, *vartuple):
    print("输出：")
    print(arg1)
    for var in vartuple:
        print("var= ", var)
    return


printinfo2(10)
printinfo2(50, 23, 12)


# 声明函数时，参数中星号（*）可以单独出现
# 用法：星号（*）后的参数必须用关键字传入
def f(a, b, *, c):
    return a + b + c


print(f(1, 2, c=3))


# 匿名函数
sum = lambda agr1, arg2: agr1 + arg2
print("相加后的值为：", sum(10, 20))
print("相加后的值为：", sum(20, 20))


# return语句
def sum(arg1, arg2):
    total = arg1 + arg2
    print("函数内：", total)
    return total


total = sum(10, 20)
print("函数外：", total)


# 全局变量和局部变量，变量访问顺序由内而外
# global和nonlocal关键字
# 当内部作用域想修改外部作用域的变量是，就要用到global和nonlocal关键字
num = 1
def fun1():
    global num      # 需要使用global关键字声明
    print(num)
    num = 123
    print(num)


fun1()
print(num)


# 如果要修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量则需要nonlocal关键字
def outer():
    num1 = 10

    def inner():
        nonlocal num1            # nonlocal关键字
        num1 = 100
        print(num1)
    inner()
    print(num1)


outer()
