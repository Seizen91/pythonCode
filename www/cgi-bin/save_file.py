#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# 获取文件名
fileitem = form['filename']

# 检测文件是否上传
if fileitem.filename:
	# 设置文件路径
	fn = os.path.basename(fileitem.filename)
	open('F:/code/pythonCode/www/tmp/' + fn, 'wb').write(fileitem.file.read())
	
	message = '文件 "' + fn + '" 上传成功'
	
else:
	message = '文件没有长传'

print("""\
	Content-type:text/html\n
	<html>
	<head>
	<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
		<p>%s</p>
	</body>
	</html>
""" % (message,))
	