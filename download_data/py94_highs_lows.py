# -*- coding: utf-8 -*-
# author: laugc
# email: hahalgc@gmail.com
# time: 2019/7/14 21:40
# file: py94_highs_lows.py

import csv
from matplotlib import pyplot as plt
from datetime import datetime

"""

"""

# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'

# 获取最高气温
with open(filename)as f:
    # 创建阅读器
    reader = csv.reader(f)
    # 读取第一行
    header_row = next(reader)
    # print(header_row)

    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    print(highs)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

# 绘图
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置图形的格式
title = 'daily high and low temperature - 2014\nDeath Valley CA'
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
