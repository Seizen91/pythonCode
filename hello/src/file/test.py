
# open a file
f = open("test.txt", "w")

f.write("Python 是一个非常好的语言。\n 是的， 的确非常好！！\n")

# close the file
f.close()


f = open("test.txt", "r")
str1 = f.read()
print(str1)
f.close()
print()


f = open("test.txt", "r")
str1 = f.readline()
print(str1)
f.close()

f = open("test.txt", "r")
str1 = f.readlines()
print(str1)
f.close()
print()


f = open("test.txt", "r")
for line in f:
    print(line, end="")
f.close()


f = open("test.txt", "w")

num = f.write("Python 是一个非常好的语言。\n 是的， 的确非常好！！\n")
print(num)      # 返回写入的字符数
f.close()


# 如果要写入一些不是字符串的东西，将需要先进行转换
f = open("foo.txt", "w")
value = ('www.runoob.com', 14)
s = str(value)
f.write(s)
f.close()
print()

f = open("foo.txt", "rb+")
f.write(b'0123456789abcdef')
print(f.seek(5))
print(f.read(1))
print(f.seek(-3, 2))
print(f.read(1))
f.close()
print()

with open("foo.txt", 'r') as f:
    read_data = f.read()
    print(read_data)
print(f.closed)

