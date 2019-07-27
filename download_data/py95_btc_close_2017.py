# -*- coding: utf-8 -*-
# author: laugc
# email: hahalgc@gmail.com
# time: 2019/7/15 22:06
# file: py95_btc_close_2017.py

from __future__ import (absolute_import, division, print_function, unicode_literals)

try:
    # python 2.x 版本
    from urllib2 import urlopen
except ImportError:
    # python 3.x 版本
    from urllib.request import urlopen

import requests
import math
import pygal
import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)
# 读取数据
req = response.read()
# 将数据写入文件
with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)

file_urllib = json.loads(req)
print(file_urllib)
print('=============================================')
req = requests.get(json_url)
# 将数据写入文件
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)

file = req.json()
print(file)
print(file == file_urllib)
print('=============================================')
dates = []
months = []
weeks = []
weekdays = []
close = []
# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价(￥)'
line_chart.x_labels = dates
# 每 20 天显示一次
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('收盘价', close_log)
line_chart.render_to_file('收盘价折线图(￥).svg')
