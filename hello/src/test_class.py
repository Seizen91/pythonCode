"""
类对象：
    支持两种操作：属性引用和实例化
"""


class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类中的方法输出为：", x.f())
print()


# 将对象创建为有初始状态的
# 类的方法与普通的函数只有一个特别的区别：就是必须有一个额外的第一个参数名称，一般写成self
# self代表类的实例，而非类，self不是关键字，用其他的字符也是一样
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -5.4)
print(x.r, x.i)
print()


# 使用def关键字来定义一个方法，与一般函数定义不同，类方法中必须包含参数self，self代表的是类的实例
# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0

    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说：我 %d 岁。" %(self.name, self.age))


# 类实例化
people = People('runoob', 10, 30)
people.speak()
print()


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的函数
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆盖父类的方法
    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d 年纪。" %(self.name, self.age, self.grade))


student = Student('ken', 10, 60, 3)
student.speak()
print()


class Speaker:
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s， 我是一个演说家，我演讲主题是 %s" %(self.name, self.topic))


# 多继承
# 多继承需要注意括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索
# 即方法在子类中未找到时，从左至右查找父类中是否包含方法

# 多重继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


sample = Sample("Tim", 25, 80, 4, "Python")
sample.speak()      # 方法相同，默认调用的是在括号中排前的父类的方法
print()


# 方法重写：
# 如果父类方法的功能不能满足要求，可以再子类中重写父类的方法
class Parent:       # 定义父类

    def myMethod(self):
        print("调用父类方法")


class Child(Parent):        # 定义子类
    def myMethod(self):
        print("调用子类方法")


child = Child()         # 子类实例
child.myMethod()        # 子类调用重写方法
super(Child, child).myMethod()      # 用子类对象调用父类已被覆盖的方法
print()


# 类属性与方法：
# 类的私有属性：__private_attrs
# 类的方法：def定义，必须有第一个参数为self（约定写self）
#  类的私有方法：__private_method
class JustCounter:
    __secretCount = 0   # 私有变量
    publicCount = 0     # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print("私有变量：", self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)        # 报错，实例不能访问私有变量
print()


# 类的私有方法
class Site:
    def __init__(self, name, url):
        self.name = name        # public
        self.__url = url        # private

    def who(self):
        print("name: ", self.name)
        print("url: ",self.__url)

    def __foo(self):            # 私有方法
        print("这是私有方法")

    def foo(self):              # 公共方法
        print("这是公共方法")
        self.__foo()


site = Site("菜鸟教程", "www.runoob.com")
site.who()
site.foo()
# site.__foo()    # 报错
print()


# 运算符重载
# 可以对类的专有方法进行重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
print()
