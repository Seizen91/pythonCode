# while 循环

n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为：%d" % (n, sum))


# 无限循环
def unlimit_cycle():
    var = 1
    while var == 1:
        num = int(input("输入一个数字："))
        print("你输入的数字是：", num)

    print("Good bye!")


# unlimit_cycle()

# while循环使用else语句
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")


# for 语句
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

for i in range(3):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(0, 10, 3):
    print(i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

print(list(range(5)))


# break 语句
def test_break():
    for letter in 'Runoob':
        if letter == 'b':
            break
        print("当前字母：", letter)

    var = 10
    while var > 0:
        print("当前变量值为：", var)
        var = var - 1
        if var == 5:
            break

    print("Good bye!")


# test_break()


# continue语句
def test_continue():
    for letter in "Runoob":
        if letter == "o":
            continue
        print("当前字母：", letter)

    var = 10
    while var > 0:
        var = var - 1
        if var == 5:
            continue
        print("当前变量值：", var)
    print("Good bye!")


# test_continue()


# pass 语句：空语句，是为了保持程序结构的完整性，不做任何事情，一般用做占位字符
def test_pass():
    for letter in "Runoob":
        if letter == 'o':
            pass
            print("执行 pass 块")
        print("当前字母：", letter)

    print("Good bye!")


test_pass()

