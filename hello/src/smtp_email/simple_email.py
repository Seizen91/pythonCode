#!/usr/bin/python
# 授权码：dbscmyqjsqfxgehb   czydfjhtbmgbgcjb
# zhaoxin：xwzvdollopoobhjf

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "zhaoxin.zm@qq.com"  # 用户名
mail_pass = "xwzvdollopoobhjf"    # 口令

sender = "zhaoxin.zm@qq.com"
receivers = ['1475795224@qq.com']  # 接收邮件，可设置为你的QQ邮箱或其他邮箱

# 三个参数：第一个为文本内容，第二个plain设置文本格式，第三个 utf-8设置编码
message = MIMEText('Python邮件发送测试。。。。你会收到吗?', 'plain', 'utf-8')
message['From'] = Header("亲密测试", "utf-8")   # 发送者
message['To'] = Header("seizen", "utf-8")           # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    # smtpObj = smtplib.SMTP('localhost')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25为SMTP端口号
    smtpObj.login(mail_user, mail_pass)

    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
    print(e.args)
