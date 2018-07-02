import sys

# python3 迭代器与生成器


# 迭代器
# 字符串、列表或元组对象都可用于创建迭代器
def test_iterator():
    list1 = [1, 2, 3, 4]
    for x in iter(list1):
        print(x)

    print()

    # 使用next()函数
    it = iter(list1)
    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()


# test_iterator()


# 生成器：使用了yield的函数被称为生成器
def fibonacci(n):       # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)       # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()





