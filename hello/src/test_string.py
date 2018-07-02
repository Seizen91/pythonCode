# python字符串运算符

a = "Hello"
b = "Python"

print("a + b : ", a + b)
print("a * 2 : ", a * 2)
print("a[1] : ", a[1])
print("a[1:4] : ", a[1:4])

if("H" in a):
    print("H in a")
else:
    print("H not in a")

if("M" not in a):
    print("M not in a")
else:
    print("M in a")

print(r'\n')
print(R'\n')

# python字符串格式化
print("============python字符串格式化===========")
print("我 叫 %s 今年 %d 岁！" % ('小明', 10))

# python三引号
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB( \t )。
也可以使用换行符 [ \n ]。    
"""
print(para_str)


# python字符串内建函数
print("=========python字符串内建函数===========")

str = "this is string example."

# 该方法返回一个首字母大写的字符串
print("str.capitalize() : ", str.capitalize())

# str.center(width[, fillchar])返回一个指定宽度居中的字符串，如果width小于字符串则直接返回字符串，否则用fillchar去填充
print("str.center(40, '*') : ", str.center(40, '*'))

sub = 'i'
# 返回sub在str中出现的次数
print("str.count(sub) : ", str.count(sub))
print("str.count('i', 0, 10) : ", str.count(sub, 0, 10))

# bytes.decode()方法以指定的编码格式解码bytes对象
str = "菜鸟教程"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8编码：", str_utf8)
print("GBK编码：", str_gbk)

print("UTF-8解码：", str_utf8.decode("UTF-8", "strict"))
print("GBK解码：", str_gbk.decode("GBK", "strict"))

# endswith()方法用于判断字符串是否以指定后缀结尾，可指定字符串的开始于结束位置
Str = 'Runoob example....wow!!!'
suffix = '!!'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 20))
suffix = 'run'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 0, 19))

# expandtabs()方法把字符串中的tab符号（'\t'）转换为空格，默认空格数是8
str = 'this is\tstring example....wow!!!'

print("原始字符串：" + str)
print("替换\\t符号：" + str.expandtabs())
print("使用16个空格替换\\t符号：" + str.expandtabs(16))

# find()方法检测字符串中是否包含子字符串
# index()方法和find()一样，只不过如果str不在字符串中会报一个异常
str1 = "Runoob example....wow!!!"
str2 = "exam"

print(str1.find(str2))
print(str1.find(str2, 5))
print(str1.find(str2, 10))
print(str1.find(str2, 8, 13))

print("================")
str1 = "www.runoob.com111"
str2 = "Hello"
str3 = "12333"
str4 = ""

# 判断字符串中字符都是字母或数字
print(str1.isalnum())
print(str2.isalnum())
print(str3.isalnum())
print(str4.isalnum())
print()

# 判断字符串中字符都是字母
print(str1.isalpha())
print(str2.isalpha())
print(str3.isalpha())
print()

# 判断字符串中都是数字
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())
print('------------')
print(str1.isnumeric())
print(str2.isnumeric())
print(str3.isnumeric())
print()

# 判断字符串中字母都是小写字母
print(str1.islower())
print(str2.islower())
print(str3.islower())
print()

# 判断字符串中只包含空白
print(str1.isspace())
str4 = " "
print(str4.isspace())
print()

# 判断字符串是否是标题，即每个单词首字母大写
str1 = "hello python"
str2 = "Hello Python"
print(str1.istitle())
print(str2.istitle())
print()

# 判断字符串中字母都是大写
str1 = "PYTHON"
str2 = "Python"
print(str1.isupper())
print(str2.isupper())
print()

# 以指定字符串作为分隔符，合并成一个新的字符串
str = "==="
print(str.join(str2))
print(str2.join(str))
print()

# 返回字符串长度
str = "this is example"
print(len(str))
print()

# 返回一个原字符串左对齐
print(str.ljust(50, "*"))
print(str.ljust(10, "-"))
print()

# 转换字符串中所有大写字符为小写
str = "Python World!!"
print(str.lower())
print()

# 截掉字符串左边的空格或指定字符
str = "    22222Hello Python"
str1 = "22222Hello Python"
print(str.lstrip())
print(str1.lstrip("22222"))
print()

# 将字符串中指定字符组成的字符串换为相应的映射字符的字符串
intab = "aeiou"
outtab = "12345"
str = "this is string example....wow!!!"
trantab = str.maketrans(intab, outtab)

print(str.translate(trantab))
print()

# 返回字符串str中最大和最小的字符
str = "Hello Python1"
print(max(str))
print(min(str))
print()

# 新旧字符串替换，可设置替换的次数
str = "this is string example, this is string example"
print(str.replace("is", "was"))
print(str.replace("is", "was", 3))
print()
