#!/usr/bin/python3

# 导入模块
import os
import http.cookies
if 'HTTP_COOKIE' in os.environ:
	cookie_string = os.environ.get("HTTP_COOKIE")
	c = Cookie.SimpleCookie()
	c.load(cookie_string)
	
	try:
		data = c['name'].value
		#print("cookie data:" + data +"<br>")
	expect KeyError:
		#print("cookie 没有设置或者已过去<br>")
		
print("Content-type:text/html")
print()
print("""
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<h1>读取cookie信息</h1>
<p>%s</p>
</body>
</html>
""" % (date,))