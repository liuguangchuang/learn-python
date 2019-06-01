# -*- coding: utf-8 -*-
# Time: 2019/5/29 21:20
# Author: laugc
# Email: hahalgc@gmail.com
# File: py55_datetime.py

from datetime import datetime, timedelta, timezone

# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2019, 5, 29, 12, 12)
print(dt)

# timestamp 是一个浮点数，它没有时区的概念，而 datetime 是有时区的
# datetime 转换为 timestamp
print(dt.timestamp())

# timestamp 转换为 datetime
t = 1559103120.0
print(datetime.fromtimestamp(t))  # 本地时间
print(datetime.utcfromtimestamp(t))  # UTC 时间

# str 转换为 datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime 转换为 str
print(now.strftime('%a, %b %d %H:%M'))

print("================================")
# datetime 加减
print(now + timedelta(hours=1))
print(now - timedelta(days=1))
print(now - timedelta(days=1, hours=1))

# 本地时间转换为 UTC 时间
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区 UTC+8:00
print(now.replace(tzinfo=tz_utc_8))  # 强制设置为 UTC+8:00

print("========================")
# 时区转换
# 拿到 UTC 时间，并强制设置时区为 UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

# astimezone() 将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# astimezone() 将 bj_dt 时区为东京时间
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
