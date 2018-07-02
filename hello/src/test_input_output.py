"""
python3 输入和输出
"""

s = "Hello, Runoob"
print(s)
print(str(s))

print(repr(s))
print(str(1/7))
print()

x = 10 * 3.25
y = 200 * 200
s = 'x 的值为：' + repr(x) + '， y 的值为：' + repr(y) + '...'
print(s)
print()

# repr() 函数 可以转义字符串中的额特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hello)
print(hellos)

# repr() 的参数可以是Python的任何对象
print(repr((x, y, ('Google', 'Runoob'))))
print()

# rjust将字符串靠右，并在左边填充空格，ljust()和center()方法类似
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=" ")
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))
print()

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print()

# zfill()，它会在数字的左边填充0
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))
print()

# str.format()的基本使用
print('{}网址："{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
print('{name}网址： {site}'.format(name="菜鸟教程", site="www.runoob.com"))
print('站点列表 {0}，{1} 和 {other}'.format('Google', 'Runoob', other="Taobao"))