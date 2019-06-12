# -*- coding: utf-8 -*-
# Time: 2019/6/12 22:59
# Author: laugc
# Email: hahalgc@gmail.com
# File: py82_smtp.py

from email.mime.text import MIMEText
import smtplib

"""
SMTP: Simple Mail Transfer Protocol
是发送邮件的协议
Python 对 SMTP 支持有 smtplib 和 email 两个模块，email 负责构造邮件，smtplib 负责发送邮件
"""

# plain 表示纯文本
msg = MIMEText('hello, send by Python.', ' plain', 'utf-8')
print(msg)

# 通过 SMTP 发出去
# 输入 email 地址
from_addr = input('from: ')
password = input('password: ')
# 收件人地址
to_addr = input('to: ')
# 输入 SMTP 服务器地址
smtp_server = input('SMTP server: ')
# SMTP 默认端口是 25
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
