"""
python3 正则表达式
"""
import re

# re.match 函数：尝试从字符串的其实位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
print(re.match("www", "www.runoob.com"))     # 在起始位置匹配
print(re.match("www", "www.runoob.com").span())     # 在起始位置匹配
print(re.match("com", "www.runoob.com"))            # 不在起始位置匹配
print()

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group(): ", matchObj.group())
    print("matchObj.group(1): ", matchObj.group(1))
    print("matchObj.group(2): ", matchObj.group(2))
else:
    print("No match!!")
print()


# re.search()方法：扫描整个字符串并返回第一个成功的匹配
print(re.search("www", "www.runoob.com"))     # 在起始位置匹配
print(re.search("www", "www.runoob.com").span())     # 在起始位置匹配
print(re.search("com", "www.runoob.com"))
print(re.search("com", "www.runoob.com").span())# 不在起始位置匹配
print()


# re.sub(a, b, c, d) 用于替换字符串中的匹配项
# 参数：a为正则中的模式字符串，b为替换的字符串，也可为一个函数
# c为要被查找替换的原始字符串，d为模式匹配后替换的最大次数，默认0表示替换所有的匹配
phone = '2004-959-559 # 这是一个电话号码'

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码：", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码：", num)
print()


# 当替换的字符串为函数时
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = "A23G4HFD567"
print(re.sub('(?P<value>\d+)', double, s))


# compile 函数：用于编译正则表达式，生成一个正则表达式对象，供match和search使用
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)        # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print(m)        # 匹配成功，返回一个Match对象
print(m.group(0))       # 返回匹配成功的整个子串
print(m.span(0))        # 返回匹配成功的整个子串的索引
print(m.group(1))       # 返回第一个分组匹配成功的子串
print(m.span(1))        # 返回第一个分组匹配成功的子串的索引
print(m.group(2))       # 返回第二个分组匹配成功的子串
print(m.span(2))        # 返回第二个分组匹配成功的子串的索引

print(m.groups())       # 等价于(m.group(1), m.group(2), ...)
print()


# findall : 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
# 注意：match和search是匹配一次，findall是匹配所有
pattern = re.compile(r'\d+')        # 用于匹配至少一个数字
string = 'runoob 1123 google 456'
result1 = pattern.findall(string)
result2 = pattern.findall(string, 0, 10)        # 指定起始位置

print(result1)
print(result2)

print(pattern.match(string))
print(pattern.search(string).span())
print()


# re.finditer 与 re.findall类似，只不过是作为一个迭代器返回
it = re.finditer(r'\d+', "12a32bc43jf3")
for match in it:
    print(match.group(), end=", ")
print()


# re.split方法按照能够匹配的子串将字符串分割后返回列表
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', 'runoob, runoob, runoob.'))
print(re.split('\W+', 'runoob, runoob, runoob.', 1))    # 分割一次

#print(re.split('a*', 'hello world'))    # 对于找不到匹配的字符串，split不会对其作出分割
print()
