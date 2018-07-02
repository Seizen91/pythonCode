# 斐波那契（fibonacci）数列模块


def fib(n):         # 定义到n的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print()


def fib2(n):        # 返回到n的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


# __name__ 属性：仅在该模块自身运行是执行
if __name__ == '__main__':
    print("程序自身在运行")
else:
    print("我来自另一个模块")

# 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。

# 说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。

