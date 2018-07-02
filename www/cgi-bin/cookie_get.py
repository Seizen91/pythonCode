#!/usr/bin/python3

# 导入模块
import os
import http.cookies

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<title>菜鸟教程(runoob.com)</title>")
print("</head>")
print("<body>")
print("<h1>读取cookie信息</h1>")
if 'HTTP_COOKIE' in os.environ:
	cookie_string = os.environ.get("HTTP_COOKIE")
	c = Cookie.SimpleCookie()
	c.load(cookie_string)
	
	try:
		data = c['name'].value
		print("cookie data:" + data +"<br>")
	expect KeyError:
		print("cookie 没有设置或者已过去<br>")
print("</body>")
print("</html>")




