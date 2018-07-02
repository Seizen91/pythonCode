# 导入模块
# import src.modules.support （此方法导入需要用全名去访问）
from src.modules import support

# 现在可以调用模块里包含的函数了
support.print_func("Runoob")
dir(support)

# from ... import 语句：从模块中导入指定的部分
# from fibo import fib
# fib(10)

# from ... import* 语句：把模块内容全部导入
from src.modules.fibo import*
fib(15)
print(fib2(15))

